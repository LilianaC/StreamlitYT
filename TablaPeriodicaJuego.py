#https://discuss.streamlit.io/t/dynamic-buttons/7723/2


import streamlit as st
import pandas as pd
import random

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)
st.session_state.num=0

def juego():
    
    st.session_state.num = random.randint(0, len(df))
    letra = df.iloc[num]['Elemento'][0]
    resultado = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
    lista = resultado.values.tolist()
    lista.insert(0, "🤔")
    st.write(lista)
    return [num,lista]

def reset():
    st.session_state.puntos = 0

def revision():
    if elemento ==  df.iloc[num]['Elemento']:
        st.write("¡Excelente!")
        st.session_state.puntos += 1
        st.write("Puntos",st.session_state.puntos)
        juego()
    
    else:
        st.write("Respuesta incorrecta")
        st.session_state.puntos -= 1
        st.write("Puntos",st.session_state.puntos)
        juego()
    

num,lista = juego()

st.write("¿Cuál es el nombre del elemento químico con el símbolo", df.iloc[num]['Symbol'], "?")
st.write(df.iloc[num]['Elemento'])
elemento = st.radio("Selecciona el elemento",lista)
revision()
st.write(elemento)
st.session_state.puntos = 0
st.button('🔄 Resetear',on_click=reset)












