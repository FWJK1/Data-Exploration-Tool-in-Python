"""
Ian Sargent
ORCA
Streamlit Data Visualization App

Run this in the terminal to launch the app:
-------------------------------------------
streamlit run Home.py
-------------------------------------------
"""

# Necessary imports
from PIL import Image
import streamlit as st
from app_utils.streamlit_config import streamlit_config


def main():
    # Set page configurations
    st.set_page_config(page_title="Vermont Data App", layout="wide", page_icon="🍁")

    # Set the page title
    st.header("Vermont Data Exploration App")

    with open("main_page.html") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    # Display a background photo for the page
    with open("main_page.css") as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)


    logos = [
        "Images/center_rural_studies.png",
        "Images/leahy_logo.png",
        "Images/Picture1.png"
    ]

    cols = st.columns(len(logos))
    for col, path in zip(cols, logos):
        img = Image.open(path)
        col.image(img, use_container_width=True)


if __name__ == "__main__":
    streamlit_config()
    main()
