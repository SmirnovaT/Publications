from db import db

class PublicationModel(db.Model):
    __tablename__ = 'publications'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(500))

    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def json(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
