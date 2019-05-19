FROM jetblackpope/vscode-python-dev-container:library

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIPENV_SHELL_FANCY 1
ENV PIPENV_MAX_SUBPROCESS 32

COPY .devcontainer/settings.remote.json /root/.vscode-remote/data/Machine/settings.json

RUN mkdir /workspace
WORKDIR /workspace

RUN python -m pip install black pipenv rope twine

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*