def format(request):
    import json

    data = json.loads(request.text)

    tempsX = []  
    tempsY = []

    for point in data['data']['timelines'][0]['intervals']:
        tempsX.append(point['startTime'])
        tempsY.append(point['values']['temperature'])

    return (tempsX, tempsY)

if __name__ == '__main__':
    import api
    data = api.get({
        'location':'12, 56',
        'timestep': 'current',
        'fields':'temperature',
        'units':'metric',
        'apikey':'44rcPRlfvH9W2CJa5FoZgHD9mUWWWkVt'
        })
    
    print(format(data))

