import streamlit as st


def footer_home():
    
    st.markdown(f"""
        <div style="margin-top:3rem; display:flex; justify-content:center; align-items:center;">
        <p style="font-family:'Outfit', sans-serif; text-transform:uppercase; letter-spacing:0.2em; font-size:0.7rem; color:#E0E3FF; opacity:0.6;">Built with ❤️ by Rakesh</p>  
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by Rakesh</p>  
        </div>
                
                """, unsafe_allow_html=True)