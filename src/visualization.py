import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

qatar_embassies_path = "interim/qatar_embassies_stats.xlsx"
global_embassies_path = "interim/global_embassies_stats.xlsx"
all_qatar_embassies_path = "interim/all_qatar_embassies_df.xlsx"
all_global_embassies_path = "interim/all_global_embassies.xlsx"

# # Show a warning message
# st.warning(
#     """This app is still under development. It currently only looks at the Qatari Embassies' tweets.
#     Please use it with caution"""
# )


@st.cache_data
def load_data():
    """Loads the data from the Excel file."""
    data = pd.read_excel(qatar_embassies_path, engine="openpyxl")
    data_globaL_embassies = pd.read_excel(global_embassies_path, engine="openpyxl")
    all_qatar_embassies = pd.read_excel(all_qatar_embassies_path, engine="openpyxl")
    all_global_embassies = pd.read_excel(all_global_embassies_path, engine="openpyxl")

    return data, data_globaL_embassies, all_qatar_embassies, all_global_embassies


with st.spinner("Loading data..."):
    data, data_globaL_embassies, all_qatar_embassies, all_global_embassies = load_data()
    st.success("Data loaded successfully")


st.subheader("Qatari Embassies")
count_df_qatar_embassies = (
    all_qatar_embassies.groupby("screen_name").size().sort_values(ascending=False)
)

st.write("Language distribution")
# Plot the language distribution
st.bar_chart(all_qatar_embassies['languages'].value_counts())
st.write("Refer to this page to get the list of ISO 639-1 codes:https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")

st.write("Hashtag distribution")
st.write(f"**{all_qatar_embassies['hashtags'].isnull().sum()}** tweets do not contains hashtags")

st.write("Tweet count distribution")
st.bar_chart(count_df_qatar_embassies)

st.subheader("Embassies in Qatar")
count_df_global_embassies = (
    all_global_embassies.groupby("screen_name").size().sort_values(ascending=False)
)

st.write("Language distribution")
# Plot the language distribution
st.bar_chart(all_global_embassies['languages'].value_counts())
st.write("Refer to this page to get the list of ISO 639-1 codes:https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")

st.write("Hashtag distribution")
st.write(f"**{all_global_embassies['hashtags'].isnull().sum()}** tweets do not contains hashtags")

st.write("Tweet count distribution")
st.bar_chart(count_df_global_embassies)

st.markdown("""---""")

with st.sidebar:
    st.title("Qatar Embassies Stats")
    st.write("Select a country from the dropdown below to see its embassy stats")
    country = st.selectbox("Country", data.columns[1:])
    country_data = data.loc[:, country]

with st.sidebar:
    st.title("World Cup embassies in Qatar")
    st.write("Select a country from the dropdown below")
    world_cup_country = st.selectbox("Country", data_globaL_embassies.columns[1:])
    world_cup_country_data = data_globaL_embassies.loc[:, world_cup_country]
    

st.subheader(f"Stats of Qatar Embassy in {country}")
st.markdown(
    f"""
    * Total Tweets: {country_data.iloc[0]}
    * Original Tweets: {country_data.iloc[1]}
    * Retweets: {country_data.iloc[2]}
    * Unique Dates: {country_data.iloc[3]}
    * Languages: {country_data.iloc[4]}
    * Hashtags: {country_data.iloc[5]}
    * Tweets with Images: {country_data.iloc[6]}
    * Tweets with Videos: {country_data.iloc[7]}
    """
)

st.subheader(f"Stats of {world_cup_country} Embassy in Qatar")
st.markdown(
    f"""
    * Total Tweets: {world_cup_country_data.iloc[0]}
    * Original Tweets: {world_cup_country_data.iloc[1]}
    * Retweets: {world_cup_country_data.iloc[2]}
    * Unique Dates: {world_cup_country_data.iloc[3]}
    * Languages: {world_cup_country_data.iloc[4]}
    * Hashtags: {world_cup_country_data.iloc[5]}
    * Tweets with Images: {world_cup_country_data.iloc[6]}
    * Tweets with Videos: {world_cup_country_data.iloc[7]}
    """
)