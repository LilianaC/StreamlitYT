import streamlit as st

buttons = []

for i in range(5):
    buttons.append(st.button(str(i)))

for i, button in enumerate(buttons):
    if button:
        st.write(f"{i} button was clicked")
