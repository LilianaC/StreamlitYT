import streamlit as st

# Define your custom CSS
custom_css = """
<style>
[data-baseweb="select"] > div {
    font-size: 20px;
    color: red;
    background-color: yellow;
}
</style>
"""

# Inject custom CSS with st.markdown()
st.markdown(custom_css, unsafe_allow_html=True)

# Render the selectbox
option = st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])
