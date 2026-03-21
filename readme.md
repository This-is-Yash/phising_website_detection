# 🔐 Phishing URL Detection System

## 🚀 Overview

This project is a **Phishing URL Detection System** that uses **Machine Learning (ML) + Deep Learning (DL)** to classify URLs as:

* ✅ SAFE
* ⚠️ SUSPICIOUS
* ❌ MALICIOUS

It combines:

* 🌲 Random Forest (ML)
* 🧠 LSTM Neural Network (DL)
* ⚖️ Ensemble Learning for better accuracy

---

## 🌐 Live Demo

* 🔗 Frontend (GitHub Pages):
  https://this-is-yash.github.io/phising_website_detection/


---

## 🧠 How It Works

```
User Input URL
      ↓
Feature Extraction (ML)
      ↓
Tokenizer + Padding (DL)
      ↓
ML Model + DL Model
      ↓
Ensemble Scoring
      ↓
Prediction Output
```

---

## 📁 Project Structure

```
phishing_detection/
│
├── backend/
│   ├── app.py                # FastAPI backend
│   ├── predict.py            # Prediction logic
│   ├── feature_extractor.py  # Feature extraction
│   ├── model/
|              └──models.pkl              # Trained models
|               └──tokenizer.pkl
|               └──dl_model.h5.pkl
|   ├── train_models.py           # Model training
|   ├── scraper.py
|   ├── utils.py
|   ├── requirements.txt
|   ├──Dockerfile 
|   ├── data/
│           └── urls_dataset.csv      # Dataset
|
├── docs/
│   ├── index.html
│   ├── css/style.css
│   └── js/script.js
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Features

* 🔍 Detect phishing URLs in real-time
* 🤖 ML + DL hybrid model
* 🌐 Live web interface
* 🔄 Scalable and deployable backend
* 📊 Feature-based + sequence-based detection

---

## 🧪 Steps of Implementation

### 1. Data Collection

* Phishing URLs from OpenPhish & PhishTank
* Benign URLs from trusted websites

### 2. Data Preprocessing

* Remove duplicates
* Normalize URLs
* Clean dataset

### 3. Feature Extraction

Extracted features include:

* URL length
* Number of dots (`.`)
* Presence of `@`, `-`, `/`
* Digit count

### 4. Model Selection

* Random Forest (ML)
* LSTM (DL)

### 5. Model Training

* Train ML model on extracted features
* Train DL model on character sequences

### 6. Prediction

* Combine ML + DL outputs
* Generate final classification

---

## ⚡ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/phishing-detection.git
cd phishing-detection
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Collect Dataset

```
python scraper.py
```

### 4. Train Models

```
python train_models.py
```

### 5. Run Backend

```
uvicorn backend.app:app --host 0.0.0.0 --port 8080
```

---

## 🌍 Deployment

* **Frontend** → GitHub Pages
* **Backend** → Railway
* **CORS Enabled** for cross-origin requests

---
## 🖼️ Screen shot
<img width="1918" height="887" alt="image" src="https://github.com/user-attachments/assets/274ebf46-c190-440f-bb80-cf5425bd6c87" />

---

## ⚠️ Known Issues

* CORS issues may occur if backend is misconfigured
* Dataset imbalance can affect accuracy
* DL model requires proper sequence input

---

## 🚀 Future Improvements

* 🔄 Continuous learning from user inputs
* 🗄️ Database integration
* 📊 Dashboard for analytics
* ⚡ Faster inference optimization

---

## 👨‍💻 Author

**Yash**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🚀 Contribute

---
