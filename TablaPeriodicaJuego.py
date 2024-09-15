import streamlit as st
import pandas as pd
import random

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)
num = random.randint(0, len(df))
letra = df.iloc[num]['Elemento'][0]
resultado = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
lista = resultado.values.tolist()


buttons = []

for i in range(len(lista)):
    buttons.append(st.button(lista[i]))

for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")
