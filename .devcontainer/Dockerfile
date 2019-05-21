FROM jetblackpope/vscode-python-dev-container:library

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIPENV_SHELL_FANCY 1
ENV PIPENV_MAX_SUBPROCESS 32

COPY .devcontainer/settings.remote.json /home/riker/.vscode-remote/data/Machine/settings.json

RUN sudo chown -R riker:riker /home/riker/.vscode-remote

RUN mkdir -p /home/riker/workspace
WORKDIR /home/riker/workspace

RUN python -m pip install black pipenv rope twine