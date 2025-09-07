import streamlit as st

def styled_text(
    text,
    color="white",
    size=16,
    bold=False,
    italic=False,
    underline=False,
    font_family="Arial"
):
    """
    Display text in Streamlit with maximum customization.
    
    Args:
        text (str): The text to display
        color (str): CSS color (e.g., "red", "#00ff00")
        size (int): Font size in px
        bold (bool): Make text bold
        italic (bool): Make text italic
        underline (bool): Add underline
        font_family (str): Font family ("Arial", "Times New Roman", etc.)
    """
    style = f"color:{color}; font-size:{size}px; font-family:{font_family};"
    if bold:
        style += " font-weight:bold;"
    if italic:
        style += " font-style:italic;"
    if underline:
        style += " text-decoration:underline;"

    st.markdown(f"<span style='{style}'>{text}</span>", unsafe_allow_html=True)


import streamlit as st

import base64
from pathlib import Path

def set_background_image(image_path, opacity: float = 0.3):
    """
    Set a background image with adjustable opacity.
    Works with local paths or URLs.
    """
    image_path = str(image_path)

    if image_path.startswith("http"):  # Case 1: URL
        bg = f'url("{image_path}")'
    else:  # Case 2: Local file → Convert to Base64
        ext = Path(image_path).suffix.replace(".", "")
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        bg = f'url("data:image/{ext};base64,{encoded}")'

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(
                rgba(255, 255, 255, {1-opacity}),
                rgba(255, 255, 255, {1-opacity})
            ),
            {bg};
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def set_background_color(color: str):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

