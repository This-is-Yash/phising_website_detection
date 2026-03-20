# import os
# import pickle
# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, LSTM, Dense
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from scraper import get_url_features  # your function that extracts features

# # --- Load dataset ---
# DATA_FILE = "data/urls_dataset.csv"
# df = pd.read_csv(DATA_FILE)

# # --- ML features ---
# ml_features = [list(get_url_features(url).values()) for url in df['url']]
# X_ml = np.array(ml_features)
# y = df['label'].values

# # Scale
# scaler = StandardScaler()
# X_ml = scaler.fit_transform(X_ml)

# # Train RandomForest
# ml_model = RandomForestClassifier(n_estimators=200)
# ml_model.fit(X_ml, y)

# os.makedirs("model", exist_ok=True)
# pickle.dump(ml_model, open("model/ml_model.pkl", "wb"))
# print("ML model saved!")

# # --- DL features (LSTM) ---
# tokenizer = Tokenizer(char_level=True)
# tokenizer.fit_on_texts(df['url'])
# sequences = tokenizer.texts_to_sequences(df['url'])
# max_len = max(len(seq) for seq in sequences)
# X_dl = pad_sequences(sequences, maxlen=max_len)
# y_dl = y

# vocab_size = len(tokenizer.word_index) + 1
# dl_model = Sequential()
# dl_model.add(Embedding(vocab_size, 16, input_length=max_len))
# dl_model.add(LSTM(32))
# dl_model.add(Dense(1, activation='sigmoid'))
# dl_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# dl_model.fit(X_dl, y_dl, epochs=5, batch_size=64)

# dl_model.save("model/dl_model.h5")
# pickle.dump(tokenizer, open("model/tokenizer.pkl", "wb"))
# print("DL model and tokenizer saved!")
import pandas as pd
import numpy as np
import pickle
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from feature_extractor import get_url_features

# Load dataset
df = pd.read_csv("data/urls_dataset.csv")

# --- ML FEATURES ---
X = np.array([get_url_features(url) for url in df['url']])
y = df['label'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train ML
ml_model = RandomForestClassifier(n_estimators=300)
ml_model.fit(X_train, y_train)

y_pred = ml_model.predict(X_test)
print("ML Accuracy:", accuracy_score(y_test, y_pred))

os.makedirs("model", exist_ok=True)
pickle.dump(ml_model, open("model/ml_model.pkl", "wb"))

# --- DL MODEL ---
tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(df['url'])

sequences = tokenizer.texts_to_sequences(df['url'])
max_len = 100
X_dl = pad_sequences(sequences, maxlen=max_len)

model_dl = Sequential([
    Embedding(len(tokenizer.word_index)+1, 32, input_length=max_len),
    LSTM(64),
    Dense(1, activation='sigmoid')
])

model_dl.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model_dl.fit(X_dl, y, epochs=5, batch_size=64)

model_dl.save("model/dl_model.h5")
pickle.dump(tokenizer, open("model/tokenizer.pkl", "wb"))

print("✅ Models trained successfully")