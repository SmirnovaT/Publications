from flask_restful import reqparse

publication_parser = reqparse.RequestParser()
publication_parser.add_argument('id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
publication_parser.add_argument('content',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )