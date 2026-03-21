FROM python:3.11-slim

WORKDIR /app

COPY backend /app

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn[standard] pandas numpy scikit-learn pydantic python-multipart

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]

# FROM python:3.11-slim

# WORKDIR /app

# COPY backend /app

# RUN pip install fastapi uvicorn

# CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
