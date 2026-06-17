import streamlit as st

def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background:
                        radial-gradient(circle at 1px 1px, rgba(255,255,255,0.08) 1.5px, transparent 0) 0 0/28px 28px,
                        linear-gradient(155deg, #6873F5 0%, #4750C9 45%, #1B1F4D 100%) !important;
                    background-attachment: fixed !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #FAFAFE !important;
                    padding: 2.25rem 2rem !important;
                    border-radius: 28px !important;
                    border: none !important;
                    border-left: 6px solid #5865F2 !important;
                    box-shadow: 0 24px 48px -28px rgba(15, 18, 50, 0.55) !important;
                    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
                    }

                .stApp div[data-testid="stColumn"]:hover{
                    transform: translateY(-6px) !important;
                    box-shadow: 0 32px 60px -24px rgba(15, 18, 50, 0.6) !important;
                }

                .stApp div[data-testid="stColumn"]:nth-of-type(2){
                    border-left-color: #EB459E !important;
                }

                @media (prefers-reduced-motion: reduce) {
                    .stApp div[data-testid="stColumn"] { transition: none !important; }
                }
        </style>       
        """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>
                .stApp{
                    background: #E0E3FF !important;
                }
        </style>         
        """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');    

                 
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
                }

            button:hover{
                transform: scale(1.05) !important;
                box-shadow: 0 12px 24px -8px rgba(88,101,242,0.45) !important;
            }
        </style>         
        """, unsafe_allow_html=True)