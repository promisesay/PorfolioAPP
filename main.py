import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo (2).jpg")


with col2:
    st.title("Naveed Zaynali")
    content = """
    HI , My name is naveed and im a jonior programmer familiar to web development ,system  engineering, asemblie and 
    binnery coding and so on but my main interest is python and i be so happy to show you some of my apps
    
    contact with = naveedzaynali@gmail.com
    """
    st.info(content)

st.write("Below you can find some of the appps i have built in python.Feel free to contact me!")


col3, coly, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, rows in df[:10].iterrows():
        st.title(rows["title"])
        st.image(rows["image"])
        st.info(rows["description"])
        st.write(rows["url"])


with col4:
    for index, rows in df[10:].iterrows():
        st.title(rows["title"])
        st.image(rows["image"])
        st.info(rows["description"])
        st.write(rows["url"])

