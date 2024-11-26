def plot(points):
    import plotly.express as px
    fig = px.line(x=points[0], y=points[1], markers=True)
    fig.show()
    print(points[1])

if __name__ == '__main__':
    import api
    import processing

    apikey = '44rcPRlfvH9W2CJa5FoZgHD9mUWWWkVt'

    params = {
        'location':'51.519444, 0.126944',
        'timestep': 'current',
        'fields':'temperature',
        'units':'metric'
        }

    request = api.get(params, apikey)
    points = processing.format(request)

    plot(points)