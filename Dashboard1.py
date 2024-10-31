import pandas as pd
import plotly.express as px
import streamlit as st


def set_page_config():
    st.set_page_config(
        page_title="Métricas de asistencia",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)


def main():
    set_page_config()

    st.title("📊 Sales Dashboard")

    selected_product_lines, selected_countries, selected_statuses = display_sidebar(data)



if __name__ == '__main__':
    main()
