import streamlit as st 
import pandas as pd

qatar_embassies_path = "interim/qatar_embassies_stats.xlsx"

@st.cache_data
def load_data():
    data = pd.read_excel(qatar_embassies_path, engine="openpyxl")
    return data

with st.spinner("Loading data..."):
    data = load_data()
    st.success("Data loaded successfully")

with st.sidebar:
    st.title("Qatar Embassies Stats")
    st.write("Select a country from the dropdown below to see its embassy stats")
    country = st.selectbox("Country", data.columns[1:])
    country_data = data.loc[:, country]

st.write(f'Total Tweets: {country_data.iloc[0]}')
st.write(f'Original Tweets: {country_data.iloc[1]}')
st.write(f'Retweets: {country_data.iloc[2]}')
# st.write(f'Unique Dates: {country_data.iloc[3]}')
st.write(f'Languages: {country_data.iloc[4]}')
st.write(f'Hashtags: {country_data.iloc[5]}')

