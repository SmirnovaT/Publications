import sqlite3
from flask_restful import Resource, reqparse


class Publication(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('content',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, title):
        pulication = self.find_by_title(title)
        if pulication:
            return pulication
        return {'message': 'Publication not found'}, 404

    @classmethod
    def find_by_title(cls, title):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM publications WHERE title=?"
        result = cursor.execute(query, (title,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'publication': {'id': row[0], 'title': row[1], 'content': row[2]}}

    def post(self, title):
        if self.find_by_title(title):
            return {'message': "An publication with title '{}' already exists".format(title)}, 400

        data = Publication.parser.parse_args()

        publication = {'id': data['id'], 'title': title, 'content': data['content']}

        try:
            self.insert(publication)
        except:
            return {"message": "An error occurred inserting the publication."}, 500

        return publication, 201

    @classmethod
    def insert(cls, publication):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO publications VALUES (?, ?, ?)"
        cursor.execute(query, (publication['id'], publication['title'], publication['content']))

        connection.commit()
        connection.close()

    def delete(self, title):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM publications WHERE title=?"
        cursor.execute(query, (title,))

        connection.commit()
        connection.close()

        return {'message': 'Publication deleted'}

    def put(self, title):
        data = Publication.parser.parse_args()

        publication = self.find_by_title(title)
        update_publication = {'id': data['id'], 'title': title, 'content': data['content']}

        if publication is None:
            try:
                self.insert(update_publication)
            except:
                return {"message": "An error occurred inserting the publication."}, 500

        else:
            try:
                self.update(update_publication)
            except:
                return {"message": "An error occurred updating the publication."}, 500
        return update_publication

    @classmethod
    def update(cls, publication):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE publications SET id=?, content=? WHERE title=?"
        cursor.execute(query, (publication['id'], publication['title'], publication['content']))

        connection.commit()
        connection.close()

class PublicationList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM publications"
        result = cursor.execute(query)
        publications = []
        for row in result:
            publications.append({'id': row[0], 'title': row[1], 'content': row[2]})

        connection.close()

        return {'publications': publications}
