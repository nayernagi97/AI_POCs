# AI_POCs

Collection of AI Proof of Concepts including Google ADK multi-agent conversational news research system

## Projects

### ADK (Agent Development Kit) - AI News Podcast Generator
A multi-agent conversational system that researches the latest AI news for NASDAQ-listed companies, generates a structured report, and produces a podcast audio file.

## ADK Project Structure

```
ADK/
├── app_06/
│   ├── agent.py          # Agent definitions (podcaster_agent, root_agent)
│   ├── state.py          # Pydantic schemas for news report structure
│   ├── tools.py          # Custom tools (financial data, markdown save, audio generation)
│   ├── call_back.py      # Tool callbacks (news filtering, freshness, process log)
│   ├── __init__.py       # Package init
│   └── .env              # Environment configuration
├── main.py               # Application entry point
├── pyproject.toml        # Project dependencies
├── .python-version       # Python version (3.12)
└── README.md             # Project documentation
```

## ADK - AI News Podcast Generator

### Overview
This project uses Google's Agent Development Kit (ADK) to create a multi-agent system that:
1. Searches for the latest AI news related to NASDAQ-listed US companies
2. Filters results to trusted tech news sources
3. Extracts company information and stock tickers
4. Enriches stories with real-time financial data using yfinance
5. Generates a structured Markdown report
6. Creates a conversational podcast script
7. Produces an audio file using Gemini's TTS with multi-speaker voices

### Features
- **Multi-Agent Architecture**: Root agent orchestrates research, report generation, and audio creation
- **Source Filtering**: Only uses whitelisted tech news domains (TechCrunch, VentureBeat, The Verge, etc.)
- **Freshness Guarantee**: Automatically filters for news from the last week
- **Financial Enrichment**: Real-time stock price and change data for mentioned companies
- **Structured Output**: Pydantic schemas ensure consistent report format
- **Audio Generation**: Multi-speaker podcast with Joe (enthusiastic) and Jane (analytical) voices
- **Error Resilience**: Continues processing even when some data is unavailable

### Agents

#### 1. Podcaster Agent
- **Model**: gemini-2.5-flash
- **Role**: Converts text scripts into multi-speaker audio
- **Tools**: generate_podcast_audio

#### 2. Root Agent (AI News Researcher)
- **Model**: gemini-3.1-flash-live-preview
- **Role**: Orchestrates the complete workflow
- **Tools**: google_search, get_financial_context, save_news_to_markdown, podcaster_agent
- **Output Schema**: AINewsReport (Pydantic)

### Workflow

1. **Acknowledge**: Responds to user with acknowledgment message
2. **Search**: Uses google_search with whitelisted domains and time filter
3. **Extract**: Identifies companies and stock tickers from search results
4. **Enrich**: Fetches current stock prices using yfinance
5. **Structure**: Builds AINewsReport using Pydantic schemas
6. **Save**: Writes Markdown report to file
7. **Script**: Creates conversational podcast script
8. **Generate**: Produces audio file with multi-speaker TTS
9. **Confirm**: Reports completion to user

### Installation

```bash
cd ADK
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### Usage

```bash
python main.py
```

### Dependencies

- google-adk >= 1.31.1
- yfinance >= 1.3.0
- google-genai
- pydantic

### Project Structure Details

- **agent.py**: Defines the podcaster_agent and root_agent with their instructions, tools, and callbacks
- **state.py**: Pydantic models (NewsStory, AINewsReport) for structured data
- **tools.py**: Custom tools for financial data, file operations, and audio generation
- **call_back.py**: Tool callbacks for query modification, freshness enforcement, and process logging

### Key Design Patterns

1. **Resilience by Design**: Graceful handling of missing data with placeholder values
2. **Tool Callbacks**: Pre and post-processing of tool outputs for enhanced control
3. **Schema-First**: Pydantic models ensure type safety and structure
4. **Modular Tools**: Each tool has a single, well-defined responsibility
5. **Multi-Agent Coordination**: Specialized agents for different tasks (research, audio)
