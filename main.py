from weather.api import get
from weather.processing import format
from weather.vizualization import plot

apikey = '44rcPRlfvH9W2CJa5FoZgHD9mUWWWkVt'

params = {
    'location':'39, -12',
    'timestep': 'current',
    'fields':'temperature',
    'units':'metric',
    'apikey':apikey
    }

request = get(params)
points = format(request)
plot(points)
