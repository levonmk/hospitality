from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from hospitality.guest.rest import Guest
#from hospitality.location.rest import Location
#from hospitality.booking.rest import Booking

app = Flask(__name__)
app.config.from_envvar('HOSPITALITY_SETTINGS')
db = SQLAlchemy(app)
api = Api(app)

api.add_resource(Guest, '/guest/')
#api.add_resource(Location, '/location')
#api.add_resource(Booking, '/booking')

if __name__ == '__main__':
    app.run(host=app.config['HOST'])
