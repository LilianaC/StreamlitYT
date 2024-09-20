import streamlit as st
import pandas as pd
import random
import time

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTyeAUixFkE9fiDDCx_Zifmngrjf1_9jjr1Tb7n1twPWiw0tfqd0atb1juO9ncpD5wDrjbBgcHqmfOy/pub?gid=435584327&single=true&output=csv'
df = pd.read_csv(url)

num = random.randint(0, len(df))
elemento = df.iloc[num]['Elemento']
    
symbol = df.iloc[num]['Symbol']
letra = df.iloc[num]['Elemento'][0]
pistas = df['Elemento'].loc[df['Elemento'].str.startswith(letra)]
    
lista = pistas.values.tolist()
lista.insert(0,"😁")
    
st.write("¿Cuál es el nombre del elemento químico con el símbolo ",symbol, "?")
respuesta = st.radio("Selecciona el elemento",lista)#,index=None
#st.stop()

if respuesta ==  elemento:
  st.write("¡Excelente!")
  time.sleep(2)
  st.rerun()
else:
  st.write("Respuesta incorrecta")
  time.sleep(2)
  st.rerun()
  
