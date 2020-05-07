# klas Service

# Import framework


from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class klas(Resource):
	def get(self):
	 return {
		'klassen ': ['klas1_it', 'klas_ned', 'klas_wiskunde']
		}

api.add_resource(klas, '/')

if __name__ == '__main__':
		app.run(host='0.0.0.0', port=80, debug=True)

