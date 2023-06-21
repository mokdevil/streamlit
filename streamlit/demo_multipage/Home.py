import streamlit as st

st.set_page_config(
    page_title="Fliq streamlit demo",
    page_icon="👋",
)

st.write("# Welcome to the Streamlit demo! 👋")

st.info("**Select a demo from the sidebar on the left** to see some examples of what Streamlit can do!")
st.markdown(
    """
    **What is Streamlit?**

    Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps.
    It is a Python-based library specifically designed for machine learning engineers.
    """    
)