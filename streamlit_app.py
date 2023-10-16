# ---------------------------------------------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# ---------------------------------------------------------------------------------------------------------------------------------------------
# data
# ---------------------------------------------------------------------------------------------------------------------------------------------

# Create a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values'  : [10, 20, 15, 30]
}
df = pd.DataFrame(data)


# ---------------------------------------------------------------------------------------------------------------------------------------------
# streamlit
# ---------------------------------------------------------------------------------------------------------------------------------------------


# Streamlit app title
st.title("Simple Bar Chart in Streamlit")

# Display a message
st.write("Hello, Streamlit!")

# Display the DataFrame
st.write("Sample DataFrame:")
st.write(df)

# ---------------------------------------------------------------------------------------------------------------------------------------------
# graph
# ---------------------------------------------------------------------------------------------------------------------------------------------
# Create a bar chart using Seaborn
plt.figure(figsize=(6, 4))  # Set the figure size
sns.barplot(x='Category', y='Values', data=df)
plt.xlabel('Category')
plt.ylabel('Values')

# Display the chart in Streamlit
st.pyplot(plt)

