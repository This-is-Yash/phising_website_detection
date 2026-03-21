# # Use official Python slim image
# FROM python:3.11-slim

# # Set working directory
# WORKDIR /app

# # Copy backend code
# COPY . /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libglib2.0-0 \
#     && rm -rf /var/lib/apt/lists/*

# # Install Python dependencies
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir fastapi uvicorn[standard] pandas numpy scikit-learn tensorflow pydantic python-multipart

# # Expose the port your app will run on
# EXPOSE 8080

# # Start FastAPI directly with uvicorn
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", $PORT, "--reload"]

FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install --no-cache-dir fastapi uvicorn[standard] pandas numpy scikit-learn tensorflow pydantic python-multipart

EXPOSE 8080

CMD uvicorn app:app --host 0.0.0.0 --port $PORT
