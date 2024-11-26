def get(params):
    
    import requests

    url = "https://api.tomorrow.io/v4/timelines"

    #GET request using api
    x = requests.get(url, params)

    return x

if __name__ == '__main__':
    import processing
    print(processing.format(get({
        'location':'60, 60',
        'timestep': 'current',
        'fields':'temperature',
        'units':'metric',
        'apikey':'44rcPRlfvH9W2CJa5FoZgHD9mUWWWkVt'
        })))