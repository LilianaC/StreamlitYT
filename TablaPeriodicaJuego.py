import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Custom CSS to inject
style = """
<style>
    .stSelectbox > div {font-size: 20px;}
</style>
"""
st.markdown(style, unsafe_allow_html=True)

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)

df['Año']=df['Año'].fillna(0)
df['Año'] = df['Año'].astype(int)
df = df.fillna('')

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

st.header("🧪:blue[Símbolos de elementos químicos]")


selected_element = st.selectbox(
    f'🤔 ¿Cuál es el elemento para {st.session_state.simbolo}?',
    [''] + lista) # Here we are using the 'Symbol' column of the dataframe as the options for the selectbox

st.subheader(":violet[Algunas características de este elemento son:]",divider='orange')
st.subheader(f"El :green[número atómico] es: {int(df.iloc[st.session_state.num]['AtomicNumber'])}")
st.subheader(df.iloc[st.session_state.num]['Fase'], df.iloc[st.session_state.num]['Clasifica'])
st.subheader(df.iloc[st.session_state.num]['Apariencia'])
st.subheader(f"El año de :green[descubrimiento] 🕵🏻:  {int(df.iloc[st.session_state.num]['Año'])}",divider='orange')

if selected_element:

    if selected_element == correct_element:
        st.subheader("😁 Muy bien")
        st.session_state.score += 1
        st.subheader(f"🤓 Hasta ahorita llevamos {st.session_state.score} puntos")
        st.session_state.correct = True

        st.session_state.num = random.randint(0, 118)
        st.session_state.simbolo = df.iloc[st.session_state.num]['Symbol']
        st.session_state.elemento = df.iloc[st.session_state.num]['Elemento']
        
    else:
        st.subheader("🫣 Incorrecto")
        st.subheader(f"🫢 El elemento es {st.session_state.elemento} ")
        st.session_state.score -= 1
        st.session_state.correct = False

if st.session_state.score == 3:
    st.subheader("Sí se puede 🪇", anchor=None, divider="red")

if st.session_state.score == 5:
    st.balloons()

if st.session_state.score == 5:
    st.balloons()
    
st.image("español_ptable.png",caption="Tabla periódica en Español (Ptable)",width=200)
