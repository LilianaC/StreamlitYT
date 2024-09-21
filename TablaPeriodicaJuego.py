import streamlit as st
import pandas as pd
import numpy as np
import random

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)

# Initialize session state
if 'correct' not in st.session_state:
    st.session_state.correct = True

if 'num' not in st.session_state:
    st.session_state.num = random.randint(0, 118)

if 'elemento' not in st.session_state:
    st.session_state.elemento = df.iloc[st.session_state.num]['Elemento']

if 'simbolo' not in st.session_state:
    st.session_state.simbolo = df.iloc[st.session_state.num]['Symbol']



# If the previous answer was correct, randomly select a new element
if st.session_state.correct:
    st.session_state.num = random.randint(0, 118)
    #st.session_state.Symbol = df.iloc[st.session_state.num]['Symbol']

letra = st.session_state.elemento[0]
resultado = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
lista = resultado.values.tolist()
# Ask the user to select the symbol for the randomly selected element
selected_element = st.selectbox(
    f'🤔 ¿Cuál es el elemento para {st.session_state.simbolo}?',
    [''] + lista) # Here we are using the 'Symbol' column of the dataframe as the options for the selectbox

if selected_element:
    # Get the correct symbol for the selected element
    correct_element = st.session_state.elemento
    st.write(correct_element)

    # Check if the selected symbol is correct
    if selected_element == correct_element:
        st.write('Correct! The symbol for', st.session_state.elemento, 'is', correct_element)
        st.session_state.correct = True
        st.rerun() # Rerun the script to ask for another element
    else:
        st.write('Incorrect. The symbol for', st.session_state.elemento, 'is', correct_element)
        st.session_state.correct = False

if st.button("🫡 Comenzar de nuevo"):
    st.session_state.correct = True
    #st.rerun()
