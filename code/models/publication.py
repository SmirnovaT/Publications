from db import db

class PublicationModel(db.Model):
    __tablename__ = 'publications'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(500))

    rubric_id = db.Column(db.Integer, db.ForeignKey('rubrics.id'))
    rubric = db.relationship('RubricModel')

    def __init__(self, id, title, content, rubric_id):
        self.id = id
        self.title = title
        self.content = content
        self.rubric_id = rubric_id

    def json(self):
        return {'id': self.id, 'title': self.title, 'content': self.content, 'rubric_id': self.rubric_id}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
