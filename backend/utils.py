# import requests

# def check_domain_api(url):
#     """
#     Simple external check using Safe Browsing API / VirusTotal or custom list.
#     For demo, random 0/1
#     """
#     # For demo, mark suspicious if url contains certain keywords
#     suspicious_keywords = ["login", "secure", "paypal", "bank"]
#     for word in suspicious_keywords:
#         if word in url.lower():
#             return 1
#     return 0
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from scraper import get_url_features
import os

ML_MODEL_PATH = "backend/model/ml_model.pkl"
DL_MODEL_PATH = "backend/model/dl_model.h5"

ml_model = pickle.load(open(ML_MODEL_PATH, "rb"))
dl_model = load_model(DL_MODEL_PATH)

def url_to_features(url):
    features = get_url_features(url)
    # Convert dict to numpy array in correct order
    feature_vector = np.array(list(features.values())).reshape(1, -1)
    return feature_vector

def predict_url(url):
    features = url_to_features(url)
    ml_pred = ml_model.predict_proba(features)[0][1]
    dl_pred = dl_model.predict(features)[0][0]  # assuming binary 0/1 output
    # Weighted ensemble
    final_score = 0.5*ml_pred + 0.4*dl_pred
    label = "SAFE" if final_score < 0.5 else "MALICIOUS"
    return {"url": url, "score": final_score, "label": label}