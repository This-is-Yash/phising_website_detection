# Use official Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy backend code
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir fastapi uvicorn[standard] pandas numpy scikit-learn tensorflow pydantic python-multipart

# Expose port
EXPOSE 8001

# Copy and give execution permissions to run script
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Default command
CMD ["/app/run.sh"]
