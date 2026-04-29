import pathlib
import wave
from typing import Dict, List

import yfinance as yf
from google import genai
from google.adk.tools import ToolContext
from google.genai import types
from pydantic import BaseModel, Field


class NewsStory(BaseModel):
    """A single news story with its context."""

    company: str = Field(
        description="Company name associated with the story (e.g., 'Nvidia', 'OpenAI'). Use 'N/A' if not applicable."
    )
    ticker: str = Field(
        description="Stock ticker for the company (e.g., 'NVDA'). Use 'N/A' if private or not found."
    )
    summary: str = Field(description="A brief, one-sentence summary of the news story.")
    why_it_matters: str = Field(
        description="A concise explanation of the story's significance or impact."
    )
    financial_context: str = Field(
        description="Current stock price and change, e.g., '$950.00 (+1.5%)'. Use 'No financial data' if not applicable."
    )
    source_domain: str = Field(
        description="The source domain of the news, e.g., 'techcrunch.com'."
    )
    process_log: str = Field(
        description="populate the `process_log` field in the schema with the `process_log` list from the `google_search` tool's output."
    )


class AINewsReport(BaseModel):
    """A structured report of the latest AI news."""

    title: str = Field(
        default="AI Research Report", description="The main title of the report."
    )
    report_summary: str = Field(
        description="A brief, high-level summary of the key findings in the report."
    )
    stories: List[NewsStory] = Field(
        description="A list of the individual news stories found."
    )


def get_financial_context(tickers: List[str]) -> Dict[str, str]:
    """
    Fetches the current stock price and daily change for a list of stock tickers
    using the yfinance library.

    Args:
        tickers: A list of stock market tickers (e.g., ["GOOG", "NVDA"]).

    Returns:
        A dictionary mapping each ticker to its formatted financial data string.
    """
    financial_data: Dict[str, str] = {}
    for ticker_symbol in tickers:
        try:
            # Create a Ticker object
            stock = yf.Ticker(ticker_symbol)

            # Fetch the info dictionary
            info = stock.info

            # Safely access the required data points
            price = info.get("currentPrice") or info.get("regularMarketPrice")
            change_percent = info.get("regularMarketChangePercent")

            if price is not None and change_percent is not None:
                # Format the percentage and the final string
                change_str = f"{change_percent * 100:+.2f}%"
                financial_data[ticker_symbol] = f"${price:.2f} ({change_str})"
            else:
                # Handle cases where the ticker is valid but data is missing
                financial_data[ticker_symbol] = "Price data not available."

        except Exception:
            # This handles invalid tickers or other yfinance errors gracefully
            financial_data[ticker_symbol] = "Invalid Ticker or Data Error"

    return financial_data


def save_news_to_markdown(filename: str, content: str) -> Dict[str, str]:
    """
    Saves the given content to a Markdown file in the current directory.

    Args:
        filename: The name of the file to save (e.g., 'ai_news.md').
        content: The Markdown-formatted string to write to the file.

    Returns:
        A dictionary with the status of the operation.
    """
    try:
        if not filename.endswith(".md"):
            filename += ".md"
        current_directory = pathlib.Path.cwd()
        file_path = current_directory / filename
        file_path.write_text(content, encoding="utf-8")
        return {
            "status": "success",
            "message": f"Successfully saved news to {file_path.resolve()}",
        }
    except Exception as e:
        return {"status": "error", "message": f"Failed to save file: {str(e)}"}


def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    """Helper function to save audio data as a wave file"""
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)


async def generate_podcast_audio(
    podcast_script: str, tool_context: ToolContext, filename: str = "'ai_today_podcast"
) -> Dict[str, str]:
    """
    Generates audio from a podcast script using Gemini API and saves it as a WAV file.

    Args:
        podcast_script: The conversational script to be converted to audio.
        tool_context: The ADK tool context.
        filename: Base filename for the audio file (without extension).

    Returns:
        Dictionary with status and file information.
    """
    try:
        client = genai.Client()
        prompt = (
            f"TTS the following conversation between Joe and Jane:\n\n{podcast_script}"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                        speaker_voice_configs=[
                            types.SpeakerVoiceConfig(
                                speaker="Joe",
                                voice_config=types.VoiceConfig(
                                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                        voice_name="Kore"
                                    )
                                ),
                            ),
                            types.SpeakerVoiceConfig(
                                speaker="Jane",
                                voice_config=types.VoiceConfig(
                                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                        voice_name="Puck"
                                    )
                                ),
                            ),
                        ]
                    )
                ),
            ),
        )

        data = response.candidates[0].content.parts[0].inline_data.data

        if not filename.endswith(".wav"):
            filename += ".wav"

        # ** BUG FIX **: This logic now runs for all cases, not just when the extension is added.
        current_directory = pathlib.Path.cwd()
        file_path = current_directory / filename
        wave_file(str(file_path), data)

        return {
            "status": "success",
            "message": f"Successfully generated and saved podcast audio to {file_path.resolve()}",
            "file_path": str(file_path.resolve()),
            "file_size": len(data),
        }

    except Exception as e:
        error_msg = str(e)[:200]
        return {"status": "error", "message": f"Audio generation failed: {error_msg}"}
