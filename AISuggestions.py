import streamlit as st

# Initialize session state values if not already set
if 'selected_option' not in st.session_state:
    st.session_state['selected_option'] = 'Option 1'

# Render the selectbox
st.session_state['selected_option'] = st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'], key='selected_option')

# Evaluate the selected option
if st.session_state['selected_option'] == 'Option 1':
    st.write('You selected Option 1.')
elif st.session_state['selected_option'] == 'Option 2':
    st.write('You selected Option 2.')
else:
    st.write('You selected Option 3.')
