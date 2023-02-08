import folium
import streamlit as st
import geocoder

from folium.plugins import Draw

from streamlit_folium import st_folium

m = folium.Map(location=[37.8181063, -122.2851045], zoom_start=15)
Draw(export=True).add_to(m)

output = st_folium(m, width=700, height=500)

st.write(output)
coords = output["last_clicked"]
if coords:
    lat = coords.get("lat", 37.818)
    lng = coords.get("lng", -122.285)

    st.write(lat)
    st.write(lng)
    g = geocoder.google([lat, lng], method = "reverse")
    st.write(g)
