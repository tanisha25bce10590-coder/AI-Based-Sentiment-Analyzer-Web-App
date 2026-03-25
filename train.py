import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset
data = pd.DataFrame({
    "text": [
        "I am very very happy today",
        "I feel sad and very lonely",
        "This is so amazing",
        "I am stressed about exams",
        "I am angry right now",
        "Life is awesome",
        "I feel tired and very upset"
    ],
    "label": [
        "Positive",
        "Negative",
        "Positive",
        "Negative",
        "Negative",
        "Positive",
        "Negative"
    ]
})

X = data["text"]
y = data["label"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)

model = MultinomialNB()
model.fit(X_train, y_train)

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model Trained")
