#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

# Update the VARIANT arg in devcontainer.json to pick a Python version: 3, 3.8, 3.7, 3.6 
# To fully customize the contents of this image, use the following Dockerfile instead:
# https://github.com/microsoft/vscode-dev-containers/tree/v0.128.0/containers/python-3/.devcontainer/base.Dockerfile
ARG VARIANT="3"
# FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}
# FROM nvidia/cuda:10.2-base
FROM tensorflow/tensorflow:latest-gpu

RUN apt update \
  && apt install -y sudo python3.8 python3-pip python3.8-venv python3.8-dev curl \
  && cp $(which python3.8) /usr/bin/python \
  && cp $(which python3.8) /usr/bin/python3 \
  && useradd -m vscode \
  && adduser vscode sudo \
  && echo 'vscode ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER vscode
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/1.0.9/get-poetry.py | python3.8 \
  && echo '. $HOME/.poetry/env' >> $HOME/.bashrc \
  && . $HOME/.poetry/env

  # && poetry completions bash > /etc/bash_completion.d/poetry.bash-completion

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
#
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional packages.
#
# RUN apt-get update \
#     && export DEBIAN_FRONTEND=noninteractive \
#    && apt-get -y install --no-install-recommends <your-package-list-here>

