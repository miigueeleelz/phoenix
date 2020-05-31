from flask_restful import Resource


class GenericResource(Resource):
    def get(self):
        return 'Welcome to Phoenix'
