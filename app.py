from typing import List
   
import requests
from flask import Flask, render_template, request
from geopy import Nominatim

app = Flask(__name__)
# open gmaps_key.txt file
with open('gmaps_key.txt', 'r') as f:  # YOUR GOOGLE MAPS API KEY TXT FILE
    app.config['GMAPS_API_KEY'] = f.read()


def get_redered_map_url(address: str, palette: List[str]) -> str:
    """ Given an address and a color palette, sends a request to the Google Maps API to get a rendered map image.  """
    road_color, water_color, land_color, city_color = palette

    query = {
        'size': '1000x1000',
        'zoom': '15',
        'center': address,
        'style': [
            f'feature:all|element:all|color:0x{land_color}',  # all on our main color
            f'feature:road|element:geometry|color:0x{road_color}',  # road color
            f'feature:road|element:geometry|visibility:simplified',  # simplified roads
            f'feature:water|element:geometry|color:0x{water_color}',  # water color
            f'feature:administrative|geometry:all|color:0x{city_color}',  # city color
            'feature:all|element:labels|visibility:off',  # all labels off
            # f'feature:landscape.man_made|element:geometry|color:0x{city_color}',  # natural land color
            # 'feature:transit|element:all|visibility:off',  # transit off
            # f'feature:poi|geometry:all|color:0x{city_color}', # parks and etc color
            # not working f'feature:all|element:all|visibility:simplified',  # simplify everything
        ],
        'key': app.config["GMAPS_API_KEY"],
        'scale': '2',
    }
    gmap = requests.get('https://maps.googleapis.com/maps/api/staticmap', params=query)

    return gmap.request.url


@app.route('/', methods=['GET'])
def home():
    if app.config['GMAPS_API_KEY'] == '':
        return 'Please set your Google Maps API key in app.py, otherwise the request will not work.'

    return render_template('index.html')


@app.route('/', methods=['POST'])
def request_and_show_map():
    # Get parameters for the API request
    address = request.form['location']
    hex_palette = request.form['palette'].split('-')
    if len(hex_palette) != 4:
        return render_template('index.html', error="Choose a color palette before continuing")
    # Normalise the input address
    try:
        geolocator = Nominatim(user_agent="laureanorp")
        normalised_address = geolocator.geocode(query=address)
    except Exception as e:
        app.logger.error(e)
        return render_template('index.html', error="We couldn't find that location, please try another")
    # Get the map image
    try:
        return render_template('index.html', rendered_map=get_redered_map_url(normalised_address, hex_palette))
    except Exception as e:
        app.logger.error(e)
        return render_template('index.html', error="Sorry, an unexpected error occurred :(")


if __name__ == '__main__':
    app.run()
