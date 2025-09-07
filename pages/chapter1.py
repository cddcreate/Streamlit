import streamlit as st
from utils import styled_text

st.title("Chapter1")
st.subheader("Basic functions")


title = st.expander("st.title")
with title:
    st.text('''st.title() is used to display the main heading of a Streamlit app.
It renders the text in large bold font at the top, ideal for app titles.''')
    st.code('st.title("Your title")')
    

subheader = st.expander("st.subheader")
with subheader:
    st.text('''st.subheader() shows a section heading, smaller than title but still bold and prominent.''')
    st.text('like st.subheader we also have st.header')
    st.code('st.subheader("Your sub title")')

text = st.expander("st.text")
with text:
    st.text('''st.text() adds plain text with no formatting, for simple descriptions.''')
    st.code('st.text("Your text")')

write = st.expander("st.write")
with write:
    st.text('st.write() is the most flexible function to display text, numbers, DataFrames, or Markdown.')
    st.write('''
    st.text("") or st.write("") is used to give space between line
    
    st.divider() is used as a divider line between the sections
    ''')
    st.code('st.write("Your text")')
    st.code('st.divider()')

markdown = st.expander("st.markdown")
with markdown:
    st.text("""
    For fully customization of text like size, color, style, font etc. But this requires knowledge of html/css/js
    This is also used for giving heading like what we do in jupyter notebook.
    Also used to make text bold or italic.
    """)
    st.code('st.markdown("your text")')
    st.code('st.markdown("**your text**")')

    markdown_example = st.expander('examples')
    with markdown_example:
        st.markdown("# Streamlit")
        st.markdown("### Streamlit")
        st.markdown("##### Streamlit")
        st.markdown('*Streamlit*')
    markdown_helper_fn = st.expander("markdown_customizer")
    with markdown_helper_fn:
        st.write("If you have no idea of js/html/css you can use this helper fn to customize you text")
        st.code(
    '''def styled_text(
    text,
    color="white",
    size=16,
    bold=False,
    italic=False,
    underline=False,
    font_family="Arial"
):
   
    style = f"color:{color}; font-size:{size}px; font-family:{font_family};"
    if bold:
        style += " font-weight:bold;"
    if italic:
        style += " font-style:italic;"
    if underline:
        style += " text-decoration:underline;"

    st.markdown(f"<span style='{style}'>{text}</span>", unsafe_allow_html=True))''')


success = st.expander("st.success")
with success:
    st.text('Green box showing your success msg')
    st.success("Download successful!!!!")
    st.code('st.success("Your success message")')

error = st.expander("st.error")
with error:
    st.text('Red box showing your error msg')
    st.error("Download failed!!!!")
    st.code('st.error("Your error message")')
image = st.expander('st.image')
with image:
    st.image(r"image/streamlit logo.jpg")
    st.text("Used to show an image in the web app")
    st.code('st.image("image location in computer or url of image")')
    st.write("""This should be noted that in windows path there are various hidden codes like "/t" for tab '/n' for new line. 
    Such keywords in the image file location will mess with the code so better to use raw version of the location. 
    for that use below syntex
    """)
    st.code('st.image(r"location")')
st.write("")
st.divider()
st.divider()

st.text("")

styled_text(text="goto",color='white',size=20,font_family="times new roman")
st.image(r"image/chapter2 thumbnail.png",width=150)
if st.button("chapter2"):
    st.switch_page("pages/chapter2.py")

