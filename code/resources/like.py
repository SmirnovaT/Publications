from flask_restful import Resource
from models.like import LikeModel



class Like(Resource):
    def post(self, like):
        try:
            like.save_to_db()
        except:
            return {"message": "An error occurred inserting the publication."}, 500

        return like.json(), 201
