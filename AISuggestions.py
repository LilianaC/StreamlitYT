import streamlit as st

# Render the selectbox
option = st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])

# Call st.rerun()
st.rerun()
