import streamlit as st
import readme
import demo_01
import demo_02
import demo_03

def main():
    with st.sidebar:
        st.title("Streamlit Tutorials")
        page = st.selectbox('Select', ('readme', 'demo_01', 'demo_02', 'demo_03'), index=0)

    if page == 'readme':
        readme.render()
    elif page == 'demo_01':
        demo_01.render()
    elif page == 'demo_02':
        demo_02.render()
    elif page == 'demo_03':
        demo_03.render()


if __name__ == '__main__':
    main()
