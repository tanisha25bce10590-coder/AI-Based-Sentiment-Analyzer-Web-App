from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


def analyze_sentiment(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    prob = model.predict_proba(vec).max() * 100
    return prediction, round(prob, 2)


def smart_response(sentiment):
    sentiment = sentiment.lower()

    if sentiment == "Positive":
        return "😊💓 You seem very happy and radiant! Keep shining!"
    
    elif sentiment == "Negative":
        return "💜🥺 I understand. pls Take a break, breathe, and talk to people."
    
    elif sentiment == "Neutral":
        return "🌿⚖️ You're feeling balanced. Stay steady and focused."
    
    else:
        return "😔😵 Emotion not stable, but take care of yourself!"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None
    response = None

    if request.method == "POST":
        text = request.form.get("text")

        if text:
            result, confidence = analyze_sentiment(text)
            response = smart_response(result)

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)
