#!/bin/bash
echo "🚀 Starting FastAPI URL Legitimacy Checker..."
exec uvicorn app:app --host 0.0.0.0 --port 8080
