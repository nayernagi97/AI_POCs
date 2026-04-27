FROM nvcr.io/nvidia/pytorch:24.08-py3

# Instantly pull official binaries instead of running slow curl scripts
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY --from=ollama/ollama:latest /bin/ollama /usr/local/bin/ollama

ARG DEV_USER_NAME=devuser

# Prevent interactive prompts during apt installations
ENV DEBIAN_FRONTEND=noninteractive

# Install Zsh, essential utilities, and modern CLI tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    curl \
    git \
    zsh \
    locales \
    bat \
    nano \
    zstd \
    && rm -rf /var/lib/apt/lists/*

# ---> ADD THIS LINE to install 'just' <---
RUN curl --proto '=https' --tlsv1.2 -fsSL https://just.systems/install.sh | bash -s -- --to /usr/local/bin/

# Set up locale for proper Zsh and terminal rendering
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# Create a non-root user and set Zsh as the default shell
RUN useradd -m -s /bin/zsh -G sudo ${DEV_USER_NAME} && \
    echo "${DEV_USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/${DEV_USER_NAME} && \
    chmod 0440 /etc/sudoers.d/${DEV_USER_NAME}

# Switch to the new user
USER ${DEV_USER_NAME}
WORKDIR /home/${DEV_USER_NAME}

# Set up ZimFW (Zsh plugin manager)
ENV ZIM_HOME="/home/${DEV_USER_NAME}/.zim"
RUN mkdir -p ${ZIM_HOME} && \
    curl -fsSL -o ${ZIM_HOME}/zimfw.zsh https://github.com/zimfw/zimfw/releases/latest/download/zimfw.zsh && \
    chmod +x ${ZIM_HOME}/zimfw.zsh

# Bring in your local dotfiles (Assumes they are in the same directory as the Dockerfile)
COPY --chown=${DEV_USER_NAME}:${DEV_USER_NAME}  scripts/* /home/${DEV_USER_NAME}/

# Add local bin to PATH
ENV PATH="/home/${DEV_USER_NAME}/.local/bin:${PATH}"

ENTRYPOINT [ "/bin/zsh" ]
