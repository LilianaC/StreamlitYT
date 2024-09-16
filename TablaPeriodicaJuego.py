#https://discuss.streamlit.io/t/dynamic-buttons/7723/2

import streamlit as st
import pandas as pd
import random

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)

def jugar():
    
    num = random.randint(0, len(df))
    letra = df.iloc[num]['Elemento'][0]
    resultado = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
    lista = resultado.values.tolist()
    lista.insert(0, "🤔")
    st.write(lista)
    return [num,lista]



juego = st.button('🔄 Juego nuevo')

if "juego_state" not in st.session_state:
    st.session_state.juego_state = False

if juego or st.session_state.juego_state:
    st.session_state.juego_state = True
    puntos = 0
    num,lista = jugar()
    st.write("¿Cuál es el nombre del elemento químico con el símbolo", df.iloc[num]['Symbol'], "?")
    st.write(df.iloc[num]['Elemento'])
    elemento = st.radio("Selecciona el elemento",lista)
    st.write(elemento)

    
    if elemento ==  df.iloc[num]['Elemento']:
        st.write("¡Excelente!")
        puntos += 1
        st.write("Puntos",puntos)
    
    else:
        st.write("Respuesta incorrecta")
        puntos -= 1
        st.write("Puntos",puntos)
    
    













