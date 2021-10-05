from db import db


class RubricModel(db.Model):
    __tablename__ = 'rubrics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    publications = db.relationship('PublicationModel', lazy='dynamic')

    def __init__(self, name, rubric_id):
        self.name = name
        self.rubric_id = rubric_id

    def json(self):
        return {'name': self.name, 'publications': [publication.json() for publication in self.publications.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
