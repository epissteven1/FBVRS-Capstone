# Import statements
import base64

from App_Pages import Home, AppDescription, Predict,     Record, Feedback
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration and styles
st.set_page_config(
    page_title="Filipino-to-Baybayin-Voice-Recognition-System",
    page_icon="App_Images/iconb.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
)
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return  base64.b64encode(data).decode()

img = get_img_as_base64("App_Images/irlak.png")

# Custom CSS for page styling
st.markdown(f"""
    <style>
        body {{
            text-align: center;
            background-color: white;
        }}
        
        .sidebar-content {{
            background-color: #242525;
            color: white;
        }}
      .st-emotion-cache-13k62yr {{
            position: absolute;
           
            color: rgb(193, 231, 247);
            inset: 0px;
            color-scheme: transparent;
            overflow: hidden;
         
        }}
    
       
        footer {{
            visibility: visible;
        }}
        footer:before {{
            content: 'Capstone1 @ 2023-2024: FBVRS';
            color: #FF4B4B;
            display: block;
            position: relative;
            padding: 2px;
            top: 3px;
        }}
        [data-testid="stSidebarContent"] {{
        background-image: url("data:image/png;base64,{img}");
        background-position:center;
        
        }}
        [data-testid="stVerticalBlockBorderWrapper"] {{
         background-color: transparent;
        }}
        [data-testid="stAppViewBlockContainer"] {{
        background-color: black;
        }}
        [data-testid="stAppViewContainer"] {{
        background-color: white;
        }}
        [data-testid="stHeader"] {{
        background-color: white;
        }}
       
    </style>
""", unsafe_allow_html=True)


# Function to render the app
def app():
    menu_list = ["Home", "Predict", "Description", "Translate", "Feedback"]
    with st.sidebar:
        option = option_menu("MENU",
                             menu_list,
                             icons=['house', 'record', 'sliders', 'search', 'chat'],
                             menu_icon="app-indicator",
                             default_index=1,
                             styles={
                                 "container": {"padding": "5!important"},
                                 "icon": {"color": "#b77b82", "font-size": "28px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#F6E1D3"},
                                 "nav-link-selected": {"background-color": "#00008B"}

                             })

    # Render selected page
    if option == menu_list[0]:
        Home.app()
    elif option == menu_list[1]:
        Record.app()
    elif option == menu_list[2]:
        AppDescription.app()
    elif option == menu_list[3]:
        Predict.app()
    elif option == menu_list[4]:
        Feedback.app()

if __name__ == '__main__':
    app()
