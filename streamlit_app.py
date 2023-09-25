import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# ここに選択リストを置き、含めたい果物を選択できるようにしましょう。アボカド、いちごは例として表示
streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) 
# ページにテーブルを表示します。
streamlit.dataframe(my_fruit_list)
