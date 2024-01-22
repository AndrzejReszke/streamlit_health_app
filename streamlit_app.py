# ---------------------------------------------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # comment out for now as it triggers error
import os
import numpy as np

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


# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [10, 15, 7, 12]


plt.bar(categories, values)


plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Plot')


plt.show()

