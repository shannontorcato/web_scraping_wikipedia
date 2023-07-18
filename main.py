import streamlit as st
import pandas as pd

st.title('Largest companies in the United States by revenue')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load the rows of data into the dataframe.
data = data = pd.read_csv('output/top_companies_by_revenue_US.csv', index_col='Rank')
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)