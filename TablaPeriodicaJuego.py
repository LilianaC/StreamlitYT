#https://discuss.streamlit.io/t/dynamic-buttons/7723/2


import streamlit as st
import pandas as pd
import random

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)


num = random.randint(0, len(df))
letra = df.iloc[num]['Elemento'][0]
resultado = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
lista = resultado.values.tolist()
nums = df['AtomicNumber'].loc[df['Elemento'].str.startswith(letra)]
nums = nums.values.tolist()
diccio = dict(map(lambda i,j : (i,j) , nums,lista))

st.write("¿Cuál es el nombre del elemento químico con el símbolo", df.iloc[num]['Symbol'], "?")

buttons = []
for x,y in diccio.items():
    buttons.append(st.button(y),key=x)


if st.button(df.iloc[num]['Elemento'],key=df.iloc[num]['AtomicNumber']):
    st.balloons()










