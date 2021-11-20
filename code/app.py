from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_migrate import Migrate
from db import db

from resources.publication import Publication, PublicationList
from resources.rubric import Rubric, RubricList
from resources.user import UserRegister
from security import authenticate, identity
from resources.like import Like

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@publ_db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'tanya'
api = Api(app)

migrate = Migrate(app, db)

jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Rubric, '/rubric/<id>')
api.add_resource(Publication, '/publication/<id>')
api.add_resource(PublicationList, '/publications')
api.add_resource(RubricList, '/rubrics')
api.add_resource(UserRegister, '/register')
api.add_resource(Like, '/like/<id>')




@app.route('/healthcheck')
def healthcheck():
    return 'OK', 201

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
