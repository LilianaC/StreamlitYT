import streamlit as st
import pandas as pd
import numpy as np

# Create a pandas DataFrame with chemical elements and their symbols
df = pd.DataFrame({
    'Element': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron'],
    'Symbol': ['H', 'He', 'Li', 'Be', 'B']
})

# Initialize session state
if 'correct' not in st.session_state:
    st.session_state.correct = True
if 'element' not in st.session_state:
    st.session_state.element = np.random.choice(df['Element'])

# If the previous answer was correct, randomly select a new element
if st.session_state.correct:
    st.session_state.element = np.random.choice(df['Element'])

# Ask the user to select the symbol for the randomly selected element
selected_symbol = st.selectbox(
    f'What is the symbol for {st.session_state.element}?',
    [''] + list(df['Symbol'])) # Here we are using the 'Symbol' column of the dataframe as the options for the selectbox

# If a symbol is selected, check if it is correct and display a message
if selected_symbol:
    # Get the correct symbol for the selected element
    correct_symbol = df[df['Element'] == st.session_state.element]['Symbol'].values[0]

    # Check if the selected symbol is correct
    if selected_symbol == correct_symbol:
        st.write('Correct! The symbol for', st.session_state.element, 'is', correct_symbol)
        st.session_state.correct = True
        st.experimental_rerun() # Rerun the script to ask for another element
    else:
        st.write('Incorrect. The symbol for', st.session_state.element, 'is', correct_symbol)
        st.session_state.correct = False
