# Minimal maps

![staticmap](https://user-images.githubusercontent.com/14150766/215328357-ef55b317-4056-4bc4-b3e3-c88ec5b2a627.png)

### Get a minimal and colorful map of a given location

After trying some geocoders and APIs, I decided wanted to experiment a bit with Google Maps' API. This app lets you write a location and choose a color palette, and returns a minimalistic map of the desired location. In the begging, this was a Flask (Python) app that also used Nominatim as a geocoder. But in the end I transitioned to a full frontend solution, so I could improve the UX and practice my JS. The app it's currently deployed on GitHub Pages: https://laureanorp.github.io/minimal_maps/. This work is inspired by [Matteo Lobello's andrioid app](https://play.google.com/store/apps/details?id=com.matteolobello.mapapers).

## Running the app

1. Clone/download repo
2. Add your Google Maps Static API key to the corresponding line in `index.html`
3. Just open `index.html` in your favorite browser

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/14150766/215763900-fb5d96ee-308c-4875-8d41-8773b10f2c85.png">

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/14150766/215763920-2af66310-d485-4fe4-946f-457c2dc7fb6e.png">

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/14150766/215763912-59615815-9013-458c-9eb4-06c37a9f55c1.png">

### Use diffent zoom levels to cover bigger areas

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/14150766/215763939-48360ccb-6d3e-44bd-b9c1-1db4be9a0d19.png">

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/14150766/215763949-3e64c0bd-bc23-437a-8b18-3cab58a4993e.png">

### And even set your own colors for the map

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/14150766/215763977-ea44c188-652b-47c2-a820-b224a4e03488.png">
