import webbrowser

import pandas as pd
import folium

# Load the shape of the zone (US states)
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
# You have to download this file and set the directory where you saved it
state_geo = 'ctp_rvn_WGS84.json'

# Initialize the map:
m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)

# Add the color for the chloropleth:

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Unemployment Rate (%)",
).add_to(m)

folium.LayerControl().add_to(m)

# Save to html
m.save('folium_kr.html')


