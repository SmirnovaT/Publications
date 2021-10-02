from flask_restful import Resource
from models.user import UserModel
from parsers.user_parser import user_parser


class UserRegister(Resource):
    def post(self):
       data = user_parser.parse_args()

       if UserModel.find_by_username(data['username']):
           return {"message": "A user with that username already exists"}, 400

       user = UserModel(data['username'], data['password'])
       user.save_to_db()

       return {"message": "User created successfully."}, 201
