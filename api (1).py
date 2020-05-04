# Student Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self):
        return {
            'Studenten': ['Hannes Delombaerde', 'Tamara Broutin', 'Detlef Manhaeve']
        }

# Create routes
api.add_resource(Student, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
