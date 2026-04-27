# ~/.zshrc


#========================================================== ZIMFW configurations
zstyle ':zim:zmodule' use 'degit'
ZIM_HOME=~/.zim

# Download zimfw plugin manager if missing.
if [[ ! -e ${ZIM_HOME}/zimfw.zsh ]]; then
  curl -fsSL --create-dirs -o ${ZIM_HOME}/zimfw.zsh \
      https://github.com/zimfw/zimfw/releases/latest/download/zimfw.zsh
fi

# Install missing modules, and update ${ZIM_HOME}/init.zsh if missing or outdated.
# Only run if we have network connectivity (for development containers)
if [[ ! ${ZIM_HOME}/init.zsh -nt ${ZDOTDIR:-${HOME}}/.zimrc ]] && command -v curl >/dev/null 2>&1; then
  if curl -s --connect-timeout 5 https://api.github.com >/dev/null 2>&1; then
    source ${ZIM_HOME}/zimfw.zsh init -q
  fi
fi

# Source init.zsh if it exists, otherwise continue with basic shell
[[ -f ${ZIM_HOME}/init.zsh ]] && source ${ZIM_HOME}/init.zsh
#===============================================================================


#============================================================ ZSH configurations
# command history
HISTFILE=${HOME}/.zhistory  # file to save command history
SAVEHIST=10000  # number of history entries to save to HISTFILE
HISTSIZE=10000  # number of history entries to keep in memory
setopt APPEND_HISTORY  # appends to the history file instead of overwriting it.
setopt HIST_EXPIRE_DUPS_FIRST  # expires duplicates first when the history file is full.
setopt EXTENDED_HISTORY  # stores timestamps in the history file.
setopt HIST_FIND_NO_DUPS  # does not display duplicates when searching the history.
setopt HIST_IGNORE_DUPS  # does not enter immediate duplicates into the history.
setopt HIST_IGNORE_ALL_DUPS  # removes all previous duplicates when a command is entered again.
setopt HIST_IGNORE_SPACE  # removes commands from the history that begin with a space.
setopt HIST_VERIFY  # doesn't execute the command directly upon history expansion.

# changing directories
setopt AUTO_CD  # performs cd to a directory if the typed command is invalid, but is a directory.
setopt CD_SILENT  # does not print the working directory after a cd.
setopt AUTO_PUSHD  # makes cd push the old directory to the directory stack.
setopt PUSHD_IGNORE_DUPS  # does not push multiple copies of the same directory to the stack.
setopt PUSHD_SILENT  # does not print the directory stack after pushd or popd.
setopt PUSHD_TO_HOME  # has pushd without arguments act like pushd ${HOME}

# job control
setopt LONG_LIST_JOBS  # lists jobs in verbose format by default.
setopt NO_BG_NICE  # prevents background jobs being given a lower priority.

# miscellaneous options
setopt INTERACTIVE_COMMENTS  # allows comments starting with # in the shell.
WORDCHARS=${WORDCHARS//[\/]}  # Remove path separator from WORDCHARS
ZSH_AUTOSUGGEST_MANUAL_REBIND=1  # Disable automatic widget re-binding on each precmd
ZSH_AUTOSUGGEST_STRATEGY=(history completion)  # Use both history and completion for suggestions

# key bindings
bindkey -e  # Set editor default keymap to emacs
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
# Only bind terminfo keys if they exist
[[ -n "$terminfo[kcuu1]" ]] && bindkey "$terminfo[kcuu1]" history-substring-search-up
[[ -n "$terminfo[kcud1]" ]] && bindkey "$terminfo[kcud1]" history-substring-search-down

# editors
export EDITOR='nano'
export VISUAL='code --wait'

# colors
export TERM="xterm-256color"

alias ls='eza --color=auto --group-directories-first'  # Enhanced ls with colors and grouping
alias l='ls -al'                                       # List all files, long format
alias ll='ls -l'                                       # List files, long format
alias la='ls -a'                                       # List all files, including hidden
alias cl='clear'                                       # Clear terminal
alias cll='clear && exec zsh'                          # Clear and reload zshrc
alias bat='/usr/bin/batcat'                            # Use batcat as bat
#===============================================================================

#======================================================================== Python
export PATH="${HOME}/.local/bin:${PATH}" # pip packages' binaries are installed here
#===============================================================================


#=========================================================================== NVM
# Add nvm to PATH
export NVM_DIR="${HOME}/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
#===============================================================================


#============================================================================ uv
export UV_KEYRING_PROVIDER=subprocess
eval "$(uv generate-shell-completion zsh)" || true
eval "$(uvx --generate-shell-completion zsh)" || true
#===============================================================================


#========================================================================== just
eval "$(just --completions zsh)" || true
#===============================================================================


#===================================================== p10k theme configurations
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
#===============================================================================
