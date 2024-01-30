# ---------------------------------------------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------------------------------------------

# standard libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # comment out for now as it triggers error
import os
import numpy as np

# custom modules
from create_graph import CreateGraph, Matlab

# ---------------------------------------------------------------------------------------------------------------------------------------------
# data
# ---------------------------------------------------------------------------------------------------------------------------------------------
folder_path = os.getcwd()
file_name = "df_final.csv"
full_path = os.path.join(folder_path, file_name)

data = pd.read_csv(full_path)
df = pd.DataFrame(data)

# ---------------------------------------------------------------------------------------------------------------------------------------------
# streamlit
# ---------------------------------------------------------------------------------------------------------------------------------------------

# Streamlit app title
st.title("Streamlit Health App")

# Display a message
st.write("Hello, Streamlit!")

# Display head of the DataFrame
st.write("Healthcare Project DataFrame:")
st.write(df)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# graph
# ---------------------------------------------------------------------------------------------------------------------------------------------
# streamlit method - vertical graph
st.bar_chart(df, y="OBS_VALUE", x="geo", color="top_no")

# streamlit method - horizontal graph
st.bar_chart(df, x="OBS_VALUE", y="geo", color="top_no")


# ----------------------------------------------------------------------------------------------------------------------------------------------
# matplotlib graph
# ----------------------------------------------------------------------------------------------------------------------------------------------

# call the function here
Matlab(df)
CreateGraph(df)


