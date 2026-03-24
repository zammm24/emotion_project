import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv("data.csv")

texts = data["text"]
labels = data["emotion"]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Prediction function
def predict_emotion(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)
    return prediction[0]