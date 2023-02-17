import streamlit
import pandas
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Display the table on the page.

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.dataframe(my_fruit_list.loc[streamlit.multiselect("Pick some fruits:", list(my_fruit_list.set_index('Fruit').index),['Avocado','Strawberries'])])

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)