import folium
import pandas
import json

map = folium.Map(location=(38.58,-99.6), tiles="Stamen Terrain", zoom_start=5)

df=pandas.read_csv("Volcanoes.txt")
lat=list(df["LAT"])
lon=list(df["LON"])
elev=list(df["ELEV"])

def colour_producer(elev):
    if elev<=1000:
        return 'green'
    elif 1000<=elev<3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name="Volcanoes")
for x,y,ele in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[x,y], popup=folium.Popup(str(ele)+" m"), 
    fill_color =colour_producer(ele),color='black',fill=True,fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green'if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<50000000 
else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")