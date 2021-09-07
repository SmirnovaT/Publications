from flask import Flask
#from flask_restful import Resource, Api


app = Flask(__name__)
#api = Api(app)


@app.route('/healthcheck')
def healthcheck():
    return 'OK', 201


app.run(port=5000)
