import csv

from flask import Flask, json, jsonify, request

all_movies = []


with open('movies.csv') as f:

    csv_reader = csv.reader(f)

    data = list(csv_reader)

    all_movies = data[1:]

liked_movies = []

disliked_movies = []

unwatched = []



app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        'data':all_movies[0],
        'message': "success"
    })

@app.route("/liked-movie", methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
         'message':"success"
    }), 201


@app.route("/unliked-movie", methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
         'message':"success"
    }), 201



@app.route("/unwatched-movie", methods = ["POST"])
def unwatched():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unwatched.append(movie)
    return jsonify({
         'message':"success"
    }), 201


if (__name__ == "__main__"):
   app.run() 