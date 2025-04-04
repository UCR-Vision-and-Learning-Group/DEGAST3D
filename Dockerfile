# Use an official PyTorch base image with CUDA support
FROM pytorch/pytorch:2.5.1-cuda12.1-cudnn9-runtime

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    unzip \
    ffmpeg \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the environment file
COPY environment.yml /app/environment.yml

# Install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/conda && \
    rm /miniconda.sh

ENV PATH="/opt/conda/bin:$PATH"

# Create and activate the Conda environment
RUN conda env create -f /app/environment.yml && conda clean -afy
ENV PATH="/opt/conda/envs/plant/bin:$PATH"

# Set the default shell to bash with Conda activated
SHELL ["/bin/bash", "-c"]

# Copy the project files
COPY . /app

# Expose necessary ports (if needed for visualization)
EXPOSE 8888 5000

# Define the default command
CMD ["bash"]
