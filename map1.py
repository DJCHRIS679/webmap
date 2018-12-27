import folium
import pandas
import numpy

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
vol_name = list(data['NAME'])

map = folium.Map(location=[38.58, -99.09], zoom_start= 6, tiles = "Mapbox Bright")

fg = folium.FeatureGroup(name = "My Map")

for lt,ln,name in zip(lat,lon,vol_name):
    fg.add_child(folium.Marker(location = [lt,ln],popup = name,icon = folium.Icon(color = 'green')))


map.add_child(fg)
map.save("map1.html")
