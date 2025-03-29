# Use a lightweight Python image
FROM python:slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -e .

# Run training pipeline
RUN python pipeline/training_pipline.py

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "application.py"]
