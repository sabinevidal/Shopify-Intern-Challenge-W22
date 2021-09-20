"""Data models."""
from . import db

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, Boolean
from sqlalchemy.orm import relationship, backref
from config import Config

class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'users'
    id = Column(
        Integer,
        primary_key=True
    )
    username = Column(
        String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = Column(
        String(80),
        index=True,
        unique=True,
        nullable=False
    )
    bio = Column(
        String
    )
    password = Column(
        String(200),
        primary_key=False,
        unique=False,
        nullable=False
    )
    admin = Column(
        Boolean,
        index=False,
        unique=False,
        nullable=False
    )
    images = relationship('Image', backref='users', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    description = db.Column(db.String)
    tags = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Image {}>'.format(self.description)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
