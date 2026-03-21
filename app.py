from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/api_health")
def health():
    return {"message": "API is running!"}
