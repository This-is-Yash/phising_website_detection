# #!/bin/bash

# while true
# do
#     echo "Running scraper..."
#     python scraper.py

#     echo "Training model..."
#     python train.py

#     echo "Sleeping for 1 hour..."
#     sleep 3600
# done
#!/bin/bash

echo "✅ Starting URL Legitimacy Checker API..."

# Optional: Preload models if you want to warm them up
if [ -f "model/ml_model.pkl" ]; then
    echo "ML model found."
else
    echo "ML model not found, please train it before deploying."
fi

if [ -f "model/dl_model.h5" ] && [ -f "model/tokenizer.pkl" ]; then
    echo "DL model and tokenizer found."
else
    echo "DL model/tokenizer not found, please train them before deploying."
fi

# Start FastAPI
exec uvicorn app:app --host 0.0.0.0 --port 8001 --reload
