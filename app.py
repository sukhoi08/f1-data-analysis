import streamlit as st
import matplotlib.pyplot as plt
import os

# List available races
races = [f.replace(".png", "") for f in os.listdir("pca_plots/2025") if f.endswith(".png")]

# Dropdown to select race
selected_race = st.selectbox("Select Race", races)

# Display image
image_path = f"pca_plots/2025/{selected_race}.png"
st.image(image_path, caption=selected_race, use_column_width=True)