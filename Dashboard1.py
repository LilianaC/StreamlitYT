import streamlit as st
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Add a selectbox to the sidebar
option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column'])

# Add a slider to the sidebar
number = st.sidebar.slider('Pick a number', 0, 100)

# Display the selected values
st.write('You selected:', option, 'from the selectbox')
st.write('You picked:', number, 'from the slider')
