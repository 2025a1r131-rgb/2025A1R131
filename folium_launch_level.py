"""Create an interactive launch-level historical SpaceX Folium map."""
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from geopy.distance import geodesic

df = pd.read_csv("dataset_part_2.csv")
assert len(df)==90 and set(df.Class.unique())=={0,1}
m=folium.Map(location=(36,-100),zoom_start=4,tiles="OpenStreetMap",control_scale=True)
sites=folium.FeatureGroup(name="Launch site summaries",show=True).add_to(m)
flights=folium.FeatureGroup(name="Individual flights (90 markers)",show=True).add_to(m)
cluster=MarkerCluster(options={"spiderfyOnMaxZoom":True}).add_to(flights)
for site,g in df.groupby("LaunchSite"):
    lat,lon=g.Latitude.iloc[0],g.Longitude.iloc[0]
    count=len(g);good=int(g.Class.sum())
    folium.Marker((lat,lon),tooltip=site,popup=f"{site}: {good}/{count} positive ({good/count:.1%})",
        icon=folium.Icon(color="blue")).add_to(sites)
for _,r in df.iterrows():
    positive=int(r.Class)
    popup=(f"Flight {int(r.FlightNumber)} | {r.Date}<br>Site: {r.LaunchSite}"
           f"<br>Orbit: {r.Orbit}<br>Payload: {r.PayloadMass} kg"
           f"<br>Class: {positive}")
    folium.Marker((r.Latitude,r.Longitude),popup=popup,
                  tooltip=f"Flight {int(r.FlightNumber)} (Class={positive})",
                  icon=folium.Icon(color="green" if positive else "red")).add_to(cluster)
vafb=(34.632093,-120.610829)
refs=[
 ("OSM coast way 41412049",(34.6346981,-120.6252741),"blue"),
 ("OSM rail way 641766417",(34.63556075374395,-120.62408359556251),"green"),
 ("Ocean Avenue OSM way 16264464",(34.6826743,-120.6038031),"orange"),
 ("Lompoc center (GeoNames)",(34.63915,-120.45794),"purple")
]
measure=folium.FeatureGroup(name="VAFB straight-line proximity",show=True).add_to(m)
for name,coordinates,color in refs:
    km=geodesic(vafb,coordinates).km
    folium.Marker(coordinates,tooltip=f"{name}: {km:.2f} km",
                  popup=f"{name}: {km:.3f} km geodesic",
                  icon=folium.Icon(color=color)).add_to(measure)
    folium.PolyLine((vafb,coordinates),tooltip=f"{km:.3f} km (straight line)",
                    color=color).add_to(measure)
    print(name,round(km,3),"km")
folium.LayerControl(collapsed=False).add_to(m)
m.save("SpaceX_90_Launches_Folium.html")
print("saved SpaceX_90_Launches_Folium.html")
