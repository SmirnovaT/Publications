from flask_restful import Resource
from models.like import LikeModel
from parsers.like_parser import like_parser


class Like(Resource):
 def post(self, id):
        if LikeModel.find_by_id(id):
            return {'message': "An like with id '{}' already exists".format(id)}, 400

        data = like_parser.parse_args()

        like = LikeModel(data['user_id'], data['publication_id'])

        try:
            like.save_to_db()
        except:
            return {"message": "An error occurred inserting the publication."}, 500

        return like.json(), 201