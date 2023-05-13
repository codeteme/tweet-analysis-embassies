import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

qatar_embassies_path = "interim/qatar_embassies_stats.xlsx"
all_qatar_embassies_path = "interim/all_qatar_embassies_df.xlsx"

# Show a warning message
st.warning(
    """This app is still under development. It currently only looks at the Qatari Embassies' tweets.
    Please use it with caution"""
)


@st.cache_data
def load_data():
    """Loads the data from the Excel file."""
    data = pd.read_excel(qatar_embassies_path, engine="openpyxl")
    all_qatar_embassies = pd.read_excel(all_qatar_embassies_path, engine="openpyxl")
    
    return data, all_qatar_embassies


with st.spinner("Loading data..."):
    data, all_qatar_embassies = load_data()
    st.success("Data loaded successfully")


# Show the raw data
st.subheader("Country specific data")
st.write("Expand to view full dataset")

st.write(data)


with st.sidebar:
    st.title("Qatar Embassies Stats")
    st.write("Select a country from the dropdown below to see its embassy stats")
    country = st.selectbox("Country", data.columns[1:])
    country_data = data.loc[:, country]


st.subheader(f"{country} Stats")
st.markdown(
    f"""
    * Total Tweets: {country_data.iloc[0]}
    * Original Tweets: {country_data.iloc[1]}
    * Retweets: {country_data.iloc[2]}
    * Unique Dates: {country_data.iloc[3]}
    * Languages: {country_data.iloc[4]}
    * Hashtags: {country_data.iloc[5]}
    """
)


# Group by the "screen_name" column
count_df = all_qatar_embassies.groupby("screen_name").size()
# Sort the data
count_df = count_df.sort_values(ascending=False)

st.bar_chart(count_df)