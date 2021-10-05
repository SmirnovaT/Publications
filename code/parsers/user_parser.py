from flask_restful import reqparse

user_parser = reqparse.RequestParser()
user_parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
        )
user_parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
                        )