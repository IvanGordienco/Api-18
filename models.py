from marshmallow import Schema, fields
from setup_db import db


class Genre(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int
    name = fields.Str


class Director(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int
    name = fields.Str


class Movie(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))


class MovieSchema(Schema):
    id = fields.Int
    title = fields.Str
    description = fields.Str
    trailer = fields.Str
    year = fields.Int
    rating = fields.Float
    genre_id = fields.Int
    director_id = fields.Int
