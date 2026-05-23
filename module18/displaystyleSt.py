import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit import bokeh_chart

# df = pd.DataFrame({
#     'Name':['Miloti', 'Dreni', 'Uvejsi'],
#     'Age':[17, 18, 23],
#     'City':['Lipjan','Klin','Prishtin']
# })
#
# df

books_df = pd.read_csv('eda-amazon-top-50-bestselling-books.ipynb')

st.title("Bestselling books in Amazon")
st.write("This app analyzes the Amazon Top Selling books")


st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_title = books_df['name']
avg_rating = books_df['User Rating']
avg_price = books_df['Price']

col1, col2, col3, col4 =  st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Title", unique_title)
col3.metric("Average Rating", avg_rating)
col4.metric("Average Price", avg_price)


st.subheader("Dataset Preview")
st.write(books_df.head())