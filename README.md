# Minimal maps

![staticmap](https://user-images.githubusercontent.com/14150766/179356728-dfb72b83-1a29-43cf-8f7e-905bcafd90fc.png)

#### Get a minimal and colorful map of a given location · Flask + Nominatim + Google Maps

After trying some geocoders and APIs, I decided wanted to experiment a bit with Google Maps' API. This Flask app takes a location as input, as well as a color palette, and returns a minimalistic map of the location to see/download.

Future improvements I want to do:
- More palettes/custom palettes support
- Better responsive design

## Running the project

1. Clone/download repo
2. Create a venv (recommended, but there are only 3 required dependencies)
3. Run `pip install -r requirements.txt`
4. Insert your Google Maps API key in `app.py`
5. Run `python app.py`
6. Open http://localhost:5000/

<img width="686" alt="image" src="https://user-images.githubusercontent.com/14150766/179356724-dc032c82-0a9e-4501-be3d-e35091db008f.png">

