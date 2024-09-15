#https://discuss.streamlit.io/t/dynamic-buttons/7723/2


import streamlit as st
import pandas as pd
import random

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)

def juego():
    num = random.randint(0, len(df))
    letra = df.iloc[num]['Elemento'][0]
    resultado = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
    lista = resultado.values.tolist()
    st.write("¿Cuál es el nombre del elemento químico con el símbolo", df.iloc[num]['Symbol'], "?")
    return [num,lista]
num,lista = juego()

elemento = st.radio("Selecciona el elemento",juego())

if elemento ==  df.iloc[num]['Elemento']:
    st.balloons()
else:
    juego()










