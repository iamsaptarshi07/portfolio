# Base image to build upon
FROM python:3.12-slim

# Install build dependencies
RUN sudo apt-get update \
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

# Sets the directory to /app.
WORKDIR /app

# Copies requirements.txt from Host machine to /app directory
COPY requirements.txt .

# Installs dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copies everything from host machine to /app directory
COPY . .

#Informs Docker that the container will listen on port 8501 at runtime.
EXPOSE 8501

# Command to run the container
CMD ["streamlit", "run", "app.py"] 