import streamlit as st
import pandas as pd
import numpy as np
import random
import time

custom_css = """
<style>
[data-baseweb="select"] > div {
    font-size: 30px;
    color: white;
    background-color: dodgerblue;
}
</style>
"""

# Inject custom CSS with st.markdown()
st.markdown(custom_css, unsafe_allow_html=True)



url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)

if 'correct' not in st.session_state:
    st.session_state.correct = True

if 'num' not in st.session_state:
    st.session_state.num = random.randint(0, 118)

if 'elemento' not in st.session_state:
    st.session_state.elemento = df.iloc[st.session_state.num]['Elemento']

if 'simbolo' not in st.session_state:
    st.session_state.simbolo = df.iloc[st.session_state.num]['Symbol']

if "score" not in st.session_state:
    st.session_state.score = 0

letra = st.session_state.elemento[0]
resultado = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
lista = resultado.values.tolist()
correct_element = st.session_state.elemento

selected_element = st.selectbox(
    f'🤔 ¿Cuál es el elemento para {st.session_state.simbolo}?',
    [''] + lista) # Here we are using the 'Symbol' column of the dataframe as the options for the selectbox

if selected_element:

    if selected_element == correct_element:
        st.write("Muy bien")
        st.session_state.score += 1
        st.write(f"Hasta ahorita llevamos {st.session_state.score} puntos")
        st.session_state.correct = True

        st.session_state.num = random.randint(0, 118)
        st.session_state.simbolo = df.iloc[st.session_state.num]['Symbol']
        st.session_state.elemento = df.iloc[st.session_state.num]['Elemento']
        
    else:
        st.write("Incorrecto")
        st.session_state.correct = False

if st.session_state.score == 5:
    st.balloons()
