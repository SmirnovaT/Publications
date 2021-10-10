from flask_restful import Resource
from models.publication import PublicationModel
from flask_jwt import jwt_required
from parsers.publication_parser import publication_parser


class Publication(Resource):
    @jwt_required()
    def get(self, id):
        pulication = PublicationModel.find_by_id(id)
        if pulication:
            return pulication.json()
        return {'message': 'Publication not found'}, 404

    @jwt_required()
    def post(self, id):
        if PublicationModel.find_by_id(id):
            return {'message': "An publication with id '{}' already exists".format(id)}, 400

        data = publication_parser.parse_args()

        publication = PublicationModel(data['title'], data['content'], data['rubric_id'])

        try:
            publication.save_to_db()
        except:
            return {"message": "An error occurred inserting the publication."}, 500

        return publication.json(), 201

    @jwt_required()
    def delete(self, id):
        publication = PublicationModel.find_by_id(id)
        if publication:
            publication.delete_from_db()

        return {'message': 'Publication deleted'}

    @jwt_required()
    def put(self, id):
        data = publication_parser.parse_args()

        publication = PublicationModel.find_by_id(id)

        if publication is None:
            publication = PublicationModel(data['title'], data['content'], data['rubric_id'])
        else:
            publication.title = data['title']
            publication.content = data['content']

        publication.save_to_db

        return publication.json()


class PublicationList(Resource):
    @jwt_required()
    def get(self):
        return {'publication': [publication.json() for publication in PublicationModel.query.all()]}

