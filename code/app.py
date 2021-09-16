from flask import Flask
from flask_restful import Api
from resources.publication import Publication, PublicationList

app = Flask(__name__)
api = Api(app)


api.add_resource(Publication, '/publication/<string:title>')
api.add_resource(PublicationList, '/publications')

@app.route('/healthcheck')
def healthcheck():
    return 'OK', 201


app.run(port=5000, debug=True)
