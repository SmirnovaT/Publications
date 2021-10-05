from flask_restful import reqparse

rubric_parser = reqparse.RequestParser()
rubric_parser.add_argument('rubric_id',
                        type=int,
                        required=True,
                        help="Every publication needs a rubric id."
                        )