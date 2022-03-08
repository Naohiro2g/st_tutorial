import streamlit as st


def render():
    st.title("Streamlit Tutorials — readme")
    st.markdown(
    """
    ### How to install Streamlit for local development
    ### How to build a Streamlit app as a web app
    ### Basics of Streamlit Deployment
    """)

    st.text("You can try some demos of Streamlit.\n\
Please select one from the sidebar or '>' mark at the left-top.")
    st.markdown(
    """
    ### Demo 01: QR Code Generator　QRコード生成アプリ
    ### Demo 02: st.pyplot　matplotlib.pyplotのグラフを描く
    ### Demo 03: Graphing Linear Function Graph 1次関数のグラフを描く
    """)
