import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

def render():
    st.header("Demo 03  pyplot(2)")
    st.write("Display a matplotlib.pyplot figure.　matplotlib.pyplotのグラフを描く。")
    st.info("keywords: pyplot columns radio slider numpy random matplotlib histgram")

    st.subheader(f"y = ax + b の1次関数グラフ")
    col1, col2 = st.columns([1, 2])

    with col1:
        param_a = st.select_slider("a", options=[-4,-3, -2, -1, 0, 0.2, 0.25, 0.333, 0.5, 0.666, 1, 2, 3, 4], value=1)
        param_b = st.slider("b", -4, 4, value=-1)
        st.subheader(f"y = {param_a}x + {param_b}")

    x = np.arange(-9, 9, 0.1)
    y = param_a * x + param_b
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set_aspect('equal')
    ax.grid(which='major', color='gray', linewidth=0.25)
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)

    #  軸ラベルを整数値、1ごとに、文字サイズを小さくする。
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.tick_params(labelsize=6)

    # x軸y軸を0のところに描き、目盛りを下、左に配置
    ax.spines.left.set_position('zero')
    ax.spines.right.set_color('none')
    ax.spines.bottom.set_position('zero')
    ax.spines.top.set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    with col2:
        st.pyplot(fig)


if __name__ == '__main__':
    render()
