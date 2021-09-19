from flask_restful import Resource, reqparse


publications = []

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

        publication = next(filter(lambda x: x['title'] == title, publications), None)
        return {'publication': publication}, 200 if publication else 404

    def post(self, title):
        # if next(filter(lambda x: x['title'] == title, publications), None):
        #     return {'message': "An publication with title '{}' already exists".format(title)}, 400

        data = Publication.parser.parse_args()

        publication = {'title': title, 'id': data['id'], 'content': data['content'],}
        publications.append(publication)
        return publication, 201

    def delete(self, title):
        global items
        items = list(filter(lambda x: x['title'] != title, publications))
        return {'message': 'Publication deleted'}

    def put(self, title):
        data = Publication.parser.parse_args()

        publication = next(filter(lambda x: x['title'] == title, publications), None)
        if publication is None:
            publication = {'title': title, 'id': data['id'], 'content': data['content']}
            publications.append(publication)
        else:
            publication.update(data)
        return publication

class PublicationList(Resource):
    def get(self):
        return {'publications': publications}
