from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo

from hospitality.guest import Guest
from hospitality.location import Location
from hospitality.booking import Booking

app = Flask(__name__)
api = Api(app)
mongo = PyMongo(app)

api.add_resource(Guest, '/guest')
api.add_resource(Location, '/location')
api.add_resource(Booking, '/booking')

if __name__ == '__main__':
    app.run(debug=True)
