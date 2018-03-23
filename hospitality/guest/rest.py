from flask_restful import Resource

class Guest(Resource):
    def get(self):
        return {'hello': 'World'}
