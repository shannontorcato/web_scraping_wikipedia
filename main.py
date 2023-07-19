import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title='Largest Companies By Revenue (US)',
                   page_icon=':bar_chart:',
                   layout='wide')

st.title('Largest companies in the United States by revenue')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load the rows of data into the dataframe.
@st.cache_data
def load_data(nrows):
    data = pd.read_csv('output/top_companies_by_revenue_US.csv', index_col='Rank')
    return data
data = load_data(100)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)

top_10_companies_by_revenue = data[:10]
st.subheader('Top 10 Companies by Revenue')
st.write(top_10_companies_by_revenue)
st.bar_chart(top_10_companies_by_revenue['Revenue (USD millions)'])