import sqlite3
from flask_restful import Resource, reqparse
from models.publication import PublicationModel

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
        pulication = PublicationModel.find_by_title(title)
        if pulication:
            return pulication.json()
        return {'message': 'Publication not found'}, 404


    def post(self, title):
        if PublicationModel.find_by_title(title):
            return {'message': "An publication with title '{}' already exists".format(title)}, 400

        data = Publication.parser.parse_args()

        publication = PublicationModel(title, data['id'], data['content'])

        try:
            publication.insert()
        except:
            return {"message": "An error occurred inserting the publication."}, 500

        return publication.json(), 201


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

        publication = PublicationModel.find_by_title(title)
        update_publication = PublicationModel(title, data['id'], data['content'])

        if publication is None:
            try:
                update_publication.insert()
            except:
                return {"message": "An error occurred inserting the publication."}, 500

        else:
            try:
                publication.update()
            except:
                return {"message": "An error occurred updating the publication."}, 500
        return update_publication.json()


class PublicationList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM publications"
        result = cursor.execute(query)
        publications = []
        for row in result:
            publications.append({'id': row[1], 'title': row[0], 'content': row[2]})

        connection.close()

        return {'publications': publications}
