from flask_restful import Resource
from models.publication import PublicationModel
from parsers.publication_parser import publication_parser
from parsers.rubric_parser import rubric_parser

class Publication(Resource):

    def get(self, title):
        pulication = PublicationModel.find_by_title(title)
        if pulication:
            return pulication.json()
        return {'message': 'Publication not found'}, 404

    def post(self, title):
        if PublicationModel.find_by_title(title):
            return {'message': "An publication with title '{}' already exists".format(title)}, 400

        data = publication_parser.parse_args()
        dat = rubric_parser.parse_args()

        publication = PublicationModel(data['id'], title, data['content'], dat['rubric_id'])

        try:
            publication.save_to_db()
        except:
            return {"message": "An error occurred inserting the publication."}, 500

        return publication.json(), 201

    def delete(self, title):
        publication = PublicationModel.find_by_title(title)
        if publication:
            publication.delete_from_db()

        return {'message': 'Publication deleted'}

    def put(self, title):
        data = publication_parser.parse_args()
        dat = rubric_parser.parse_args()

        publication = PublicationModel.find_by_title(title)

        if publication is None:
            publication = PublicationModel(data['id'], title, data['content'], dat['rubric_id'])
        else:
            publication.id = data['id']
            publication.content = data['content']

        publication.save_to_db

        return publication.json()


class PublicationList(Resource):
    def get(self):
        return {'publication': [publication.json() for publication in PublicationModel.query.all()]}

