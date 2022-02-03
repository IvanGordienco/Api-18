from flask_restx import Resource, Namespace

from models import Director, DirectorSchema
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = db.session.query(Director).all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@genre_ns.route('/<int:did>')
class GenreView(Resource):
    def get(self, did: int):
        r = db.session.query(Director).get(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
