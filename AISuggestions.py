import streamlit as st

def on_select_change():
    # Your conditional logic here
    if st.session_state.selected_option == "Option1":
        st.write("You selected Option1.")
    else:
        st.write("You selected a different option.")

# Initialize session state
if "selected_option" not in st.session_state:
    st.session_state.selected_option = "Option1"

# Create selectbox with session state and on_change parameter
selected_option = st.selectbox(
    "Select an option",
    ("Option1", "Option2", "Option3"),
    key="selected_option",  # Use session state key
    on_change=on_select_change
)
