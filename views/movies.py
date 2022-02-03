from flask_restx import Resource, Namespace
from flask import request
from models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        rs = db.session.query(Movie).all()
        res = MovieSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)

        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        r = db.session.query(Movie).get(mid)
        sm_d = MovieSchema().dump(r)
        return sm_d, 200

    def put(self, mid: int):
        movie = Movie.query.get(mid)
        req_json = request.json
        movie.title = req_json.get("name")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, mid: int):
        movie = Movie.query.get(mid)

        if not movie:
            return "", 404

        db.session.delete(movie)
        db.session.commit()

        return "", 204
