import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:36px; margin-top:30px">
            <img src='{logo_url}' style='height:90px; margin-bottom:0.5rem;' />
            <p style='font-family:"Outfit", sans-serif; letter-spacing:0.25em; font-size:0.75rem; font-weight:600; color:#FFC857; margin:0 0 0.25rem 0; text-transform:uppercase;'>
                ● Face + Voice Attendance
            </p>
            <h1 style='text-align:center; margin:0; background:linear-gradient(90deg, #E0E3FF 0%, #FFFFFF 50%, #FFD9EE 100%); -webkit-background-clip:text; background-clip:text; color:transparent;'>AI CLASS</h1>
            <p style='font-family:"Outfit", sans-serif; color:#E0E3FF; opacity:0.85; font-size:1rem; margin-top:0.5rem;'>Stop calling names. Just show up.</p>
        </div>   
                
                """, unsafe_allow_html=True)
    

def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>AI<br/>CLASS</h2>
        </div>   
                
                """, unsafe_allow_html=True)