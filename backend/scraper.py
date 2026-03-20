# import tldextract
# import re
# from urllib.parse import urlparse
# import requests

# def extract_features(url):
#     features = []

#     # URL length
#     features.append(len(url))

#     # Number of dots
#     features.append(url.count("."))

#     # Presence of @
#     features.append(1 if "@" in url else 0)

#     # Number of subdirectories
#     path = urlparse(url).path
#     features.append(path.count("/"))

#     # Presence of https
#     features.append(1 if url.startswith("https") else 0)

#     # Domain age, extension, WHOIS features could be added
#     ext = tldextract.extract(url).suffix
#     features.append(len(ext))

#     return features

# # DL requires sequence, simple one-hot / embedding style
# def features_to_sequence(url):
#     import numpy as np
#     max_len = 75
#     ascii_vals = [ord(c) for c in url[:max_len]]
#     if len(ascii_vals) < max_len:
#         ascii_vals += [0]*(max_len-len(ascii_vals))
#     return np.array([ascii_vals])
import requests
import pandas as pd
from bs4 import BeautifulSoup
import whois
import ssl
import socket
from datetime import datetime
import os
import numpy as np

DATA_FILE = "data/urls_dataset.csv"

# --- URL Sources ---
BLACKLIST_FEEDS = [
    "https://openphish.com/feed.txt",
    "https://data.phishtank.com/data/online-valid.csv"
]

BENIGN_URLS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org"
]

def fetch_blacklist():
    urls = []
    for feed in BLACKLIST_FEEDS:
        try:
            response = requests.get(feed, timeout=10)
            if feed.endswith(".txt"):
                urls.extend(response.text.splitlines())
            else:
                df = pd.read_csv(feed)
                if 'url' in df.columns:
                    urls.extend(df['url'].tolist())
        except:
            continue
    return pd.DataFrame({"url": urls, "label": 1})

def fetch_benign():
    return pd.DataFrame({"url": BENIGN_URLS, "label": 0})

def save_dataset(df):
    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_FILE, index=False)

def update_dataset():
    print("Fetching dataset...")
    df_blacklist = fetch_blacklist()
    df_benign = fetch_benign()
    df = pd.concat([df_blacklist, df_benign], ignore_index=True)
    save_dataset(df)
    print(f"Dataset updated: {len(df)} URLs")

# --- Feature Engineering ---
def get_url_features(url):
    features = {}
    features["url_length"] = len(url)
    features["num_dots"] = url.count(".")
    features["num_hyphens"] = url.count("-")
    features["num_slashes"] = url.count("/")
    features["has_at"] = 1 if "@" in url else 0
    features["entropy"] = -sum([(url.count(c)/len(url)) * (0 if url.count(c)==0 else np.log2(url.count(c)/len(url))) for c in set(url)])
    
    # WHOIS / Domain info
    try:
        domain_info = whois.whois(url)
        features["domain_age"] = (datetime.now() - domain_info.creation_date[0]).days if isinstance(domain_info.creation_date, list) else 0
    except:
        features["domain_age"] = 0
    
    # SSL certificate validity
    try:
        hostname = url.split("//")[-1].split("/")[0]
        cert = ssl.get_server_certificate((hostname, 443))
        features["ssl_valid"] = 1
    except:
        features["ssl_valid"] = 0

    return features

if __name__ == "__main__":
    update_dataset()