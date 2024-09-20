#https://discuss.streamlit.io/t/dynamic-buttons/7723/2

import streamlit as st
import pandas as pd
import random

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)

#lista=[]

juego = st.button('🔄 Juego nuevo')

def revision(respuesta):
    if respuesta ==  elemento:
        st.write("¡Excelente!")
        st.session_state.puntos += 1
        st.write("Puntos",st.session_state.puntos)
    else:
        st.write("Respuesta incorrecta")
        st.session_state.puntos -= 1
        st.write("Puntos",st.session_state.puntos)
        st.write(respuesta)

    

if "puntos" not in st.session_state:
    st.session_state.puntos = 0

if "juego_state" not in st.session_state:
    st.session_state.juego_state = False

if juego or st.session_state.juego_state:
    
    st.session_state.juego_state = True
    
    num = random.randint(0, len(df))
    elemento = df.iloc[num]['Elemento']
    
    symbol = df.iloc[num]['Symbol']
    letra = df.iloc[num]['Elemento'][0]
    pistas = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
    
    #lista.insert(0, "🤔")
    lista = pistas.values.tolist()
    
    st.write("¿Cuál es el nombre del elemento químico con el símbolo ",symbol, "?")
    respuesta = st.radio("Selecciona el elemento",lista,index=None,on_change=revision)
    st.write(respuesta)
    st.write(lista)
    st.write(elemento)
    
    
    





    
    













