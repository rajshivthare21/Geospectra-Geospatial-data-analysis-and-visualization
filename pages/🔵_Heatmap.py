import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: <https://streamlit.geemap.org>
    - GitHub repository: <https://github.com/rajshivthare21/streamlit>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    [GitHub](https://github.com/rajshivthare21/streamlit)
    """
)

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
        m = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner")
        m.add_heatmap(
            filepath,
            latitude="latitude",
            longitude="longitude",
            value="pop_max",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
