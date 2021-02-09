import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")

lat = list(data['LAT'])
lon = list(data["LON"])

map = folium.Map(location = [39.972937631881834, -108.300403994347], zoom_start = 3, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location = [lt, ln], popup = "Hi I am a marker", icon = folium.Icon(color = 'green')))

map.add_child(fg)
map.save("Map1.html")