import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    header_home()
    style_background_home()
    style_base_layout()
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("<p style='text-transform:uppercase; letter-spacing:0.15em; font-size:0.75rem; font-weight:700; color:#5865F2; margin-bottom:0.25rem;'>Student</p>", unsafe_allow_html=True)
        st.header("I'm Student")
        st.caption("Scan in with your face or voice — no roll call needed.")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.markdown("<p style='text-transform:uppercase; letter-spacing:0.15em; font-size:0.75rem; font-weight:700; color:#EB459E; margin-bottom:0.25rem;'>Teacher</p>", unsafe_allow_html=True)
        st.header("I'm Teacher")
        st.caption("Create classes and run attendance in one tap.")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()