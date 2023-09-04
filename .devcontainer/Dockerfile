# # Use the mcr.microsoft.com/devcontainers/python:0-3.11 image as the base image
FROM mcr.microsoft.com/devcontainers/python:0-3.11

ARG VENV_PATH="/home/vscode/venv"

COPY requirements.txt /tmp/
RUN su vscode -c "python -m venv /home/vscode/venv" \
   && su vscode -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt" \
   && rm -rf /tmp/requirements.txt