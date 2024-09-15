#https://discuss.streamlit.io/t/dynamic-buttons/7723/2


import streamlit as st
import pandas as pd
import random

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)


with st.form("La Tabla"):
    st.write("Inside")
    num = random.randint(0, len(df))
    letra = df.iloc[num]['Elemento'][0]
    resultado = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
    elemento = df.iloc[num]['Elemento']

    # Every form must have a submit button.
    submitted = st.form_submit_button("Presiona para jugar")
    if submitted:
        st.write("¿Cuál es el nombre del elemento químico con el símbolo", df.iloc[num]['Symbol'], "?")

buttons = []
for i in resultado.values:
    buttons.append(st.button(i,key=i))


if st.button(elemento,key=elemento):
    st.write("¡Correcto!")
    st.balloons()
            
else:
    st.write("¡Incorrecto!")
    #print("La respuesta correcta era:", df.iloc[num]['Elemento'])













