from db import db


class LikeModel(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publications.id'))

    users = db.relationship('UserModel')
    publications = db.relationship('PublicationModel')

    def __init__(self, user_id, publication_id):
        self.user_id = user_id
        self.publication_id = publication_id

    def json(self):
        return {'id': self.id, 'user_id': self.user_id, 'publication_id': self.publication_id}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
