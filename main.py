from flask import Flask, jsonify, request
import csv

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
did_not_watch = []

app = Flask(__name__)
@app.route('/get-article')

def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_movie():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    article = all_articles[0]
    all_article = all_article[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()
