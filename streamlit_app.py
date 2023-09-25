import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭自分でフルーツスムージーを作ろう🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
# ここに選択リストを置き、含めたい果物を選択できるようにしましょう。
streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index)) 
# ページにテーブルを表示します。
