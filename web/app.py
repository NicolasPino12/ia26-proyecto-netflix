import pandas as pd
import streamlit as st


st.title("Mi primera web")

st.subheader ("Resumen - Datos")

df = pd.read_csv("data/clean/popular_movies.csv")

st.dataframe(df.head(3))

st.write(df["title"].count())