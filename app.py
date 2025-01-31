


import streamlit as st      
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import cv2 
from predict import predict
import base64

# Set up page configuration with title, icon, and sidebar state
st.set_page_config(page_title="Equation Solver", page_icon="📐", initial_sidebar_state="auto")

# Load logo image
LOGO_IMAGE = "logo.png"

# CSS styling
st.markdown(
    """
    <style>
    .container {
        display: flex;
        align-items: center;
    }
    .logo-text {
        font-weight: 700;
        font-size: 50px;
        color: white;
        margin-left: 15px;
        padding: 15px;
    }
    .logo-img {
        float: right;
        width: 150px;
        height: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo and title header
st.markdown(
    f"""
    <div class="container">
    <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
    <p class="logo-text">AI MATH Equation Solver using CNN</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar settings
with st.sidebar:
    st.markdown("<h3 style='color: white;'>⚙️ Settings</h3>", unsafe_allow_html=True)
    stroke_width = st.slider(label="🖌️ Adjust Stroke Width", value=5, min_value=3, max_value=10)
    bg_color = st.color_picker("🎨 Background Color", "#FFFFFF")
    stroke_color = st.color_picker("✏️ Stroke Color", "#000000")
    drawing_mode = st.selectbox("✍️ Drawing Mode", ["freedraw", "line", "rect", "circle", "transform"])
    realtime_update = st.checkbox("🔄 Realtime Update", True)
    
    # Emojis and Stickers
    st.markdown("<h4 style='color: white;'>💡 Add Emojis & Stickers</h4>", unsafe_allow_html=True)
    st.markdown("😎 🎉 🚀 💻 📚 🧠")

    # Social links
    
# Canvas for drawing equations
data = st_canvas(
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=300,
    width=700,
    drawing_mode=drawing_mode,
    key="full_app",
)

# Prediction button and result display
if st.button('🔍 Predict'):
    if data.image_data is not None:
        path = 'temp/temp.png'
        cv2.imwrite(path, data.image_data)
        eq, res = predict(path)
        
        st.write(f"#### ✒️ **Equation:** {eq}")
        
        x = str(res)
        res_length = len(x)
        width = 100
        font_size = 35
        if res_length > 3:
            width = 150
            font_size = 25

        padding_top = max(5, (40 - font_size) / 2)
        padding_bottom = max(5, (40 - font_size) / 2)
        style = f"background-color: grey; height: 70px; width: {width}px; border-radius: 5px; padding-top: {padding_top}px; padding-bottom: {padding_bottom}px; margin-left: 150px; text-align: center;"

        label_style = "font-weight: bold; color: white; font-size: {font_size}px;"

        label_style = label_style.format(font_size=font_size)

        st.subheader("📊 Result")
        st.markdown(f"<div style='{style}'><label style='{label_style}'>{res}</label></div>", unsafe_allow_html=True)
    else:
        st.error("Please draw something on the canvas to predict.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Made with ❤️ by <a href='https://github.com/Mujeeb117'>Saad Shabbir</a></p>", unsafe_allow_html=True)








