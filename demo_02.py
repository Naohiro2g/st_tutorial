import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def render():
    st.header("Demo 02  pyplot")
    st.write("Display a matplotlib.pyplot figure.　matplotlib.pyplotのグラフを描く。")
    st.info("keywords: pyplot columns radio slider numpy random matplotlib histgram")
    col1, col2 = st.columns([1, 2])

    with col1:
        num_of_r = st.radio("乱数の生成数", [10, 20, 50, 100, 200, 500, 1000, 10000, 100000, 1000000], index=8)
    interval = st.slider("階級", 1, 200, value=100)
    st.subheader(f"{num_of_r:,}個の乱数を{interval}階級に分類したヒストグラム")

    arr = np.random.normal(0, 1, size=num_of_r)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=interval, range=(-4, 4))

    with col2:
        st.pyplot(fig)


if __name__ == '__main__':
    render()
