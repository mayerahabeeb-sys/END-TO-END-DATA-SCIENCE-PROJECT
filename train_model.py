import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

df = pd.read_csv("spam.tsv", sep="\t", header=None, names=["label", "message"])
print(f"Dataset loaded: {df.shape[0]} messages")
print(df["label"].value_counts())

X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

preds    = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, preds)
print(f"\nAccuracy: {accuracy*100:.2f}%")
print(classification_report(y_test, preds))

with open("model.pkl",      "wb") as f: pickle.dump(model,      f)
with open("vectorizer.pkl", "wb") as f: pickle.dump(vectorizer, f)

print("Model saved as model.pkl")
print("Vectorizer saved as vectorizer.pkl")