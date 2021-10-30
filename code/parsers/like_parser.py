from flask_restful import reqparse

like_parser = reqparse.RequestParser()
like_parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )
like_parser.add_argument('publication_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank."
                        )
