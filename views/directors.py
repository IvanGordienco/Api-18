from flask_restx import Resource, Namespace

from models import Director, DirectorSchema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = db.session.query(Director).all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        r = db.session.query(Director).get(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
