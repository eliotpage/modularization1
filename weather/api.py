def query(querystring={
    "location":"33, -84",
    "fields":["temperature", "cloudCover"],
    "units":"imperial",
    "timesteps":"1d",
    "apikey":"44rcPRlfvH9W2CJa5FoZgHD9mUWWWkVt"}):

    import requests
    import json

    url = "https://api.tomorrow.io/v4/timelines"

    x = requests.get(url, querystring)


    exec(f'results = {x.text}')

    results = results['data']
    results = results['timelines']
    results = results[0]

    return results

if __name__ == '__main__':
    print(query())