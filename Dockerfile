# ---------------------------------------------
# Base image
# ---------------------------------------------
FROM python:3.12-slim

# Avoid interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# ---------------------------------------------
# Install system tools
# ---------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    nano \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------
# Workspace
# ---------------------------------------------
WORKDIR /workspace

# ---------------------------------------------
# Python dependencies
# ---------------------------------------------
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# ---------------------------------------------
# No default CMD — the container will NOT
# automatically start anything.
# ---------------------------------------------