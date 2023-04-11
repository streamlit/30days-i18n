import glob
import os

import pandas as pd
import streamlit as st
from streamlit.locale import gettext as _
from PIL import Image

st.set_page_config(layout="wide")

query_params = st.experimental_get_query_params()

selected_language = st.session_state["language"]


def update_params():
    st.experimental_set_query_params(
        challenge=st.session_state.day.replace(f'{_("Day")} ', "Day"))


md_files = sorted(
    [int(x.strip("Day").strip(".md")) for x in glob.glob1(f"content/{selected_language}", "*.md")]
)

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("streamlit-logo-secondary-colormark-darktext.png"))
st.markdown(_("# 30 Days of Streamlit"))

days_list = [_("Day") + f" {x}" for x in md_files]

if query_params:
    try:
        selected_day = query_params["challenge"][0].replace("Day", f"{_('Day')} ")
        if selected_day in days_list:
            st.session_state.day = selected_day
    except KeyError:
        st.session_state.day = days_list[0]

selected_day = st.selectbox(
    _("Start the Challenge 👇"), days_list, key="day", on_change=update_params
)

with st.expander(_("About the #30DaysOfStreamlit")):
    st.markdown(_(
        """
    The **#30DaysOfStreamlit** is a coding challenge designed to help you get started in building Streamlit apps.
    
    Particularly, you'll be able to:
    - Set up a coding environment for building Streamlit apps
    - Build your first Streamlit app
    - Learn about all the awesome input/output widgets to use for your Streamlit app
    """
    ))

# Sidebar
st.sidebar.header(_("About"))
st.sidebar.markdown(_(
    "[Streamlit](https://streamlit.io) is a Python library that allows the creation of interactive, data-driven web applications in Python."
))

st.sidebar.header(_("Resources"))
st.sidebar.markdown(_(
    """
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
- [Book](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
"""
))

st.sidebar.header(_("Deploy"))
st.sidebar.markdown(_(
    "You can quickly deploy Streamlit apps using [Streamlit Community Cloud](https://streamlit.io/cloud) in just a few clicks."
))

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f"# 🗓️ {i}")
        j = i.replace(f'{_("Day")} ', "Day")
        with open(f"content/{selected_language}/{j}.md", "r") as f:
            st.markdown(f.read())
        if os.path.isfile(f"content/{selected_language}/figures/{j}.csv"):
            st.markdown("---")
            st.markdown(_("### Figures"))
            df = pd.read_csv(f"content/{selected_language}/figures/{j}.csv", engine="python")
            for i in range(len(df)):
                st.image(f"content/{selected_language}/images/{df.img[i]}")
                st.info(f"{df.figure[i]}: {df.caption[i]}")
