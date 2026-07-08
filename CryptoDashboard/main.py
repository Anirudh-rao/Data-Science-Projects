import streamlit as st

st.header('Crypto Dashboard')

home_page = st.Page("main.py", title="Home", icon="🏠", default=True)
page_1 = st.Page("page.py", title="Analytics", icon="📈")

pg = st.navigation([home_page, page_1])

pg.run()