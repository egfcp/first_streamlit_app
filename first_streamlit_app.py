import streamlit
import pandas
import requests


my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

