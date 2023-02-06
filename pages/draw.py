import folium
import streamlit as st
import geocoder

from folium.plugins import Draw

from streamlit_folium import st_folium

m = folium.Map(location=[37.8181063, -122.2851045], zoom_start=15)
Draw(export=True).add_to(m)

c1, c2 = st.columns(2)
with c1:
    output = st_folium(m, width=700, height=500)

with c2:
    st.write(output)
    coords = output["last_clicked"]
    if coords:
      g = geocoder.google([coords["lat"], coords["lng"]], method = "reverse")
      st.write(g)
