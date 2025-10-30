FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install system build deps required by some Python packages (lxml, cryptography, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    git \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Copy project files and install editable with dev extras
COPY pyproject.toml pyproject.toml
COPY src src
COPY tests tests
COPY README.md README.md

RUN python -m pip install --upgrade pip setuptools wheel \
 && pip install -e '.[dev]'

CMD ["bash"]
