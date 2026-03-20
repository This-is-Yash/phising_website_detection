import numpy as np
import re

def entropy(url):
    prob = [float(url.count(c)) / len(url) for c in dict.fromkeys(list(url))]
    return -sum([p * np.log2(p) for p in prob])

def get_url_features(url):
    features = []

    features.append(len(url))                     # length
    features.append(url.count("."))               # dots
    features.append(url.count("-"))               # hyphens
    features.append(url.count("/"))               # slashes
    features.append(sum(c.isdigit() for c in url))# digits
    features.append(1 if "@" in url else 0)       # @
    features.append(1 if "https" in url else 0)   # https
    features.append(entropy(url))                 # entropy

    # suspicious keywords
    keywords = ["login", "secure", "verify", "bank", "update", "free"]
    features.append(sum(1 for k in keywords if k in url.lower()))

    return features