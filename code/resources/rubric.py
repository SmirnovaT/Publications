from flask_restful import Resource
from models.rubric import RubricModel
from parsers.rubric_parser import rubric_parser

class Rubric(Resource):

    def get(self, name):
        rubric = RubricModel.find_by_name(name)
        if rubric:
            return rubric.json()
        return {'message': 'Rubric not found'}, 404

    def post(self, name):
        if RubricModel.find_by_name(name):
            return {'message': "A rubric with name '{}' already exists".format(name)}, 400

        data = rubric_parser.parse_args()

        rubric = RubricModel(name, data['rubric_id'])

        try:
            rubric.save_to_db()
        except:
            return {"message": "An error occurred inserting the rubric."}, 500

        return rubric.json(), 201

    def delete(self, name):
        rubric = RubricModel.find_by_name(name)
        if rubric:
            rubric.delete_from_db()

        return {'message': 'Rubric deleted'}


class RubricList(Resource):
    def get(self):
        return {'rubrics': [rubric.json() for rubric in RubricModel.query.all()]}
