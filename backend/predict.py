import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from feature_extractor import get_url_features

# Load models
ml_model = pickle.load(open("model/ml_model.pkl", "rb"))
dl_model = load_model("model/dl_model.h5")
tokenizer = pickle.load(open("model/tokenizer.pkl", "rb"))

def predict_url(url):
    # ML
    features = np.array(get_url_features(url)).reshape(1, -1)
    ml_score = ml_model.predict_proba(features)[0][1]

    # DL
    seq = tokenizer.texts_to_sequences([url])
    seq = pad_sequences(seq, maxlen=100)
    dl_score = dl_model.predict(seq)[0][0]

    # Ensemble
    final_score = 0.6 * ml_score + 0.4 * dl_score

    if final_score > 0.7:
        label = "MALICIOUS"
    elif final_score > 0.4:
        label = "SUSPICIOUS"
    else:
        label = "SAFE"

    return label, final_score


# TEST
if __name__ == "__main__":
    test_urls = [
        "http://secure-login-paypal.com",
        "https://www.google.com",
        "http://free-money-win-now.xyz"
    ]

    for url in test_urls:
        label, score = predict_url(url)
        print(f"{url} → {label} ({score:.2f})")