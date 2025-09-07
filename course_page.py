import streamlit as st
from pathlib import Path
from utils import styled_text,set_background_image,set_background_color
styled_text(text="Streamlit Tutorial" ,size=65,color='White',bold=True,font_family='Times new roman')

st.subheader("Introduction")
st.image(r"image/Why-Should-You-Learn-Streamlit-in-2024.png")
st.write('''Streamlit is an open-source Python library that simplifies the creation and sharing of custom web applications, 
particularly for machine learning and data science projects. 
It allows users to transform Python scripts into interactive web apps with minimal effort, 
eliminating the need for extensive web development knowledge (HTML, CSS, JavaScript). ''')

st.write('')
st.divider()
st.write('')

advantage,disadvantage = st.columns(2)
with advantage:
    st.subheader('✅ Advantages of Streamlit')
    st.write('''
Easy to Learn & Use – Pure Python, no need for HTML/CSS/JS.

Rapid Prototyping – Build interactive apps with very few lines of code.

Seamless Data Integration – Works smoothly with pandas, NumPy, Matplotlib, Plotly, etc.

Real-time Updates – App reruns automatically on code change.

Built-in Widgets – Buttons, sliders, forms, file upload, etc., without extra libraries.

Deployment Made Simple – Free hosting on Streamlit Community Cloud + Docker support.

Beautiful by Default – Clean, responsive UI without frontend knowledge.

Customizability – Supports Markdown, HTML, CSS, LaTeX, and theming.

Open Source & Active Community – Continuous updates and wide adoption.

Supports Multi-page Apps – Easy navigation across multiple app pages.''')
with disadvantage:
    st.subheader('❌ Disadvantages of Streamlit')
    st.write('''
Limited Customization – Complex UI designs may require hacks.

Performance Issues – Slower for very large datasets or heavy ML models.

Single-threaded – Not ideal for highly concurrent or multi-user apps.

Fewer Advanced Features – Compared to Dash or Flask for enterprise apps.

Dependency on Python – Cannot directly use other languages like R or JavaScript.

State Management Limitations – Session state can be tricky in complex workflows.

Deployment Constraints – Free hosting has usage limits; scaling may need extra setup.
    ''')

st.write('')
st.divider()
st.write('')

st.subheader("Streamlit setup")
st.write('''
 1. Save your script with a .py extension, e.g., app.py
 2. Open terminal (Anaconda Prompt / Command Prompt / VS Code terminal).
 3. Navigate to the folder containing your script:
    cd path\to\your\script
 4. Run the app with:
    streamlit run app.py
    
    or 
    
    start streamlit run app.py  (to run in new window)
 5. A local server starts and your app opens in the browser automatically.
 6. Stop the app anytime by pressing CTRL + C in the terminal.

''')
st.write("Shortcut method for jupyter user")
st.code('!streamlit run app.py')

st.write('')
st.divider()
st.write('')
chapter1,chapter2,chapter3 = st.columns(3)
with chapter1:
    st.image(r"image/chapter1 thumbnail.png")
    chap1= st.button('Chapter1')
    if chap1:
        st.switch_page("pages/chapter1.py")
with chapter2:
    st.image(r"image/chapter2 thumbnail.png")
    chap2 = st.button('chapter2')
    if chap2:
        st.switch_page('pages/chapter2.py')


disclaimer = st.expander('Disclaimer')
with disclaimer:
    st.write("images used in this webapp is taken from following sites")
    st.caption("pexels.com")
    st.caption("urbanemissions.info")
    st.caption("pinterest.com")
    
    
