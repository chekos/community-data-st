import streamlit as st
from utils import load_data, filter_dataframe

'''
# Data exploration
'''

data = load_data("data.dta.gz")

st.dataframe(filter_dataframe(data.drop(columns = ['rent', 'rentgrs', 'incwage'])))