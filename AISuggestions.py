import streamlit as st
import pandas as pd
import numpy as np

# Create a pandas DataFrame with chemical elements and their symbols
df = pd.DataFrame({
    'Element': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron'],
    'Symbol': ['H', 'He', 'Li', 'Be', 'B']
})

random_index = np.random.randint(len(df))
element, correct_symbol = df.iloc[random_index]["Element"], df.iloc[random_index]["Symbol"]

user_symbol = st.selectbox("Select the correct symbol for this element:", df["Symbol"].values)

if user_symbol == correct_symbol:
    st.success("Correct!")
else:
    st.error("Incorrect!")

if "score" not in st.session_state:
    st.session_state.score = 0

if user_symbol == correct_symbol:
    st.session_state.score += 1
    st.experimental_rerun()

else:
    st.write(f"Game over! Your final score is {st.session_state.score}.")

if st.button("Start a new game"):
    st.session_state.score = 0
    st.experimental_rerun()
