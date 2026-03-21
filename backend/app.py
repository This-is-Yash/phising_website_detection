
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# import os


# app = FastAPI(title="URL Legitimacy Checker")

# frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
# app.mount("/static", StaticFiles(directory=frontend_path), name="static")
# # app = FastAPI(title="URL Legitimacy Checker")

# # frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")

# # app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# # -------------------- CORS --------------------
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://this-is-yash.github.io"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# # -------------------- Models --------------------
# class URLRequest(BaseModel):
#     url: str

# # -------------------- Routes --------------------

# # Serve index.html at root
# @app.get("/", response_class=HTMLResponse)
# def root():
#     index_path = os.path.join(frontend_path, "index.html")
#     with open(index_path, "r", encoding="utf-8") as f:
#         return f.read()

# # URL prediction endpoint
# @app.post("/check_url")
# def check_url(request: URLRequest):
#     url = request.url
#     # -------- Dummy logic for testing --------
#     # Replace this with your predict_url(url) function
#     is_safe = url.endswith("google.com")
#     confidence = 99.9 if is_safe else 12.3

#     return {
#         "url": url,
#         "prediction": "SAFE" if is_safe else "MALICIOUS",
#         "confidence": confidence
#     }

# # Simple health check
# @app.get("/api_health")
# def health():
#     return {"message": "API is running!"}

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# app = FastAPI(title="URL Legitimacy Checker")

# # -------------------- CORS --------------------
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://this-is-yash.github.io"],  # only your GitHub Pages
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# # -------------------- Models --------------------
# class URLRequest(BaseModel):
#     url: str

# # -------------------- API --------------------
# @app.post("/check_url")
# def check_url(request: URLRequest):
#     url = request.url
#     # Dummy logic
#     is_safe = url.endswith("google.com")
#     confidence = 99.9 if is_safe else 12.3
#     return {
#         "url": url,
#         "prediction": "SAFE" if is_safe else "MALICIOUS",
#         "confidence": confidence
#     }

# @app.get("/api_health")
# def health():
#     return {"message": "API is running!"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="URL Legitimacy Checker")

# Allow only your GitHub Pages origin
origins = ["https://this-is-yash.github.io"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

@app.post("/check_url")
def check_url(request: URLRequest):
    url = request.url
    # Dummy prediction
    is_safe = url.endswith("google.com")
    confidence = 99.9 if is_safe else 12.3
    return {"url": url, "prediction": "SAFE" if is_safe else "MALICIOUS", "confidence": confidence}

@app.get("/api_health")
def health():
    return {"message": "API is running!"}

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"status": "running"}

# @app.get("/api_health")
# def health():
#     return {"message": "API is running!"}
