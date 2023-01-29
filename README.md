# Minimal maps

![staticmap](https://user-images.githubusercontent.com/14150766/215328357-ef55b317-4056-4bc4-b3e3-c88ec5b2a627.png)

#### Get a minimal and colorful map of a given location · Flask + Nominatim + Google Maps

After trying some geocoders and APIs, I decided wanted to experiment a bit with Google Maps' API. This Flask app takes a location as input, as well as a color palette, and returns a minimalistic map of the location to see/download. This work is inspired by [Matteo Lobello's andrioid app](https://play.google.com/store/apps/details?id=com.matteolobello.mapapers).

## Running the project

1. Clone/download repo
2. Create a venv (recommended, but there are only 3 required dependencies)
3. Run `pip install -r requirements.txt`
4. Add the file `gmaps_key.txt` with your Google Maps API key
5. Run `python app.py`
6. Open http://localhost:5000/

<img width="1033" alt="image" src="https://user-images.githubusercontent.com/14150766/215328428-cd88e5ad-348a-4851-abb6-8034b26aee8f.png">

<img width="1033" alt="image" src="https://user-images.githubusercontent.com/14150766/215328469-e19b79a3-4aa6-49c0-82f3-c7263d75b9c4.png">

<img width="1033" alt="image" src="https://user-images.githubusercontent.com/14150766/215328500-d11949d7-b4e7-4133-847f-f6f4c4295a51.png">

### Use diffent zoom levels to cover bigger areas

<img width="1033" alt="image" src="https://user-images.githubusercontent.com/14150766/215328488-2251e349-df57-4084-978f-8dcb71fae3c7.png">

### And even set your own colors for the map

<img width="1033" alt="image" src="https://user-images.githubusercontent.com/14150766/215328494-a43770b1-1815-44eb-aa64-3fda7e57f3e6.png">
