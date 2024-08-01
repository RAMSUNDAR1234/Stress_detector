from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    compound_score = sentiment_score['compound']
    return compound_score

def detect_stress(sentiment_score):
    if sentiment_score < -0.1:
        return "Your stress level is High,,reach out to  psychiatrist and have therapy sessions"
    elif sentiment_score < 0.1:
        return " Your stress level is Moderate , undergo yoga and meditation"
    else:
        return "Your stresss level is Low & your mental heath is awesome"

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_route():
    data = request.get_json()
    feelings = data['feelings']
    sentiment_score = analyze_sentiment(feelings)
    stress_level = detect_stress(sentiment_score)
    return jsonify({'stress_level': stress_level})

if __name__ == '__main__':
    app.run(debug=True)
