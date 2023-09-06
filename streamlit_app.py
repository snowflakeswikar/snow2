import streamlit

streamlit.title("My parents healthy diner")

streamlit.header("Breakfast")
streamlit.text("Dosa")
streamlit.text("Idli")
streamlit.text("Uttappa")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
