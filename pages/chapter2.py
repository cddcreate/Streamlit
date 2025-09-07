import streamlit as st
from utils import styled_text
import datetime

st.title("Chapter2")
st.subheader("Widgets and User inputs")


styled_text(text="All widgets are used to take user input/s so can be stored in a variable",color='pink',size=15)

expand1 = st.expander("Level 1 - Yes/No input")
with expand1:
    button,checkbox,toggle = st.columns(3)
    with button :
        st.subheader('button')
        st.write('st.button is used to take yes or know choise from the user')
        st.write('This buttons are stateless and can be used only once. Once used system forget what was user choise')
        st.code('User_choise = st.button("Name of button")')
        st.write('example--')
        user_choise = st.button("Are you enjoying this course")
    
    with checkbox :
        st.subheader("checkbox")
        st.write('st.checkbox is used to take yes or know choise from the user')
        st.write('This buttons are note stateless and can be used only again and again. System remembers it until checked ')
        st.code('User_choise = st.checkbox("Name of button")')
        st.write('example--')
        user_choise = st.checkbox("Do you agree to terms and conditions")
    
    with toggle :
        st.subheader('toggle')
        st.write('st.toggle is used to take yes or know choise from the user')
        st.write('This buttons are note stateless and can be used only again and again. TSystem remembers it until toggled ')
        st.code('User_choise = st.toggle("Name of button")')
        st.write('example--')
        user_choise = st.toggle("Do you agree to terms and conditions")

    st.write("")
    st.divider()
    st.write("")
expand2 = st.expander('Level 2 - Multiple choice input')
with expand2:
    radio,selectbox, multiselect,slider = st.tabs(['radio','selectbox','multiselect','slider'])
    with radio:
        st.subheader('st.radio')
        st.write('Used to select one from multiple choice')
        st.code('st.radio("title",[list of options])')
        st.write('example--')
        radio_input = st.radio("Select your gender",["Male","Female","Other"])
        st.write(f"You have selected {radio_input}")
    with selectbox:
        st.subheader('st.selectbox')
        st.write('Used to select one from multiple choice')
        st.write("this is similar to dropdown options in google forms")
        st.code('st.selectbox("title",[list of options])')
        st.write('example--')
        selectbox_input = st.selectbox("How are you feeling",["--select--","Happy","Ok","Sad","Depressed"])
        if selectbox_input != '--select--':
            st.success(f'You have selected {selectbox_input}')
        else:
            st.error("Plz make a choice")
        st.write("By default one option will be selected, so you can add a empty placeholder also to represent none selected situation like --select--")
    
    
    with multiselect:
        st.subheader('st.multiselect')
        st.write('Used to select more than one options from multiple choice')
        st.code('st.multiselect("title",[list of options],max_selections=3,default="abc")')
        st.write('example--')
        st.multiselect("What you would like to learn",["python","numpy","pandas","sklearn","tensorflow",'pytorch'],max_selections=3,default='python')

    with slider:
        st.subheader('st.slider')
        st.write('Used to select a numerical value from a range')
        st.code('st.slider("title",min_value=0,max_value=10,step=1)')
        st.write('example--')
        slider_input = st.slider("How much you are willing to spent on Learning MLAI",min_value=1000,max_value=100000,step=1000)
        st.write(f"So you can spent {slider_input} on learning, thats enough i guess !!")
        

    st.write("")
    st.divider()
    st.write("")
    
expand3 = st.expander("Level 3 - Non directive inputs")
with expand3:
    num,text,area,date,time = st.tabs(['number_input','text_input',"text_area",'date_input','time_input'])
    with num:
        st.subheader("number_input")
        st.write('st.number_input is used to take a number from user . Speciality of this is just that you can give a min max condition on this number')
        st.code('User_choise = st.number_input("How many members are in your family",min_value=1,max_value=20,step=1)')
        st.write('example--')
        user_choise = st.number_input("Enter your age",min_value=18,max_value=100,step=1)
        st.write("For most of the case this is similar to st.slider")

    with text:
        st.subheader("text_input")
        st.write('st.text_input is used to take a text from user . This used used to take small one liner inputs like name')
        st.code('User_choise = st.text_input("What is your fathers name")')
        st.write('example--')
        user_choice = st.text_input("Enter your name")
        if user_choice:
            st.write(f"Hello {user_choice} ! How are you doing ?")

    with area:
        st.subheader("text_area")
        st.write('st.text_area is used to take a text from user . This can take multiple lines of code from user')
        st.code('User_choise = st.text_area("Tell me about yourself")')
        st.write('example--')
        user_choice = st.text_area("Give your valuable feedback about this course")
    with date:
        st.subheader("date_input")
        st.write('st.date_input is used to take a date as input from user')
        st.write('By default we can only access upto last 10 years but by using datetime library we can expand it very easily')
        st.code('''
        import datetime
        start_date = datetime.date(1900,1,1)
        end_date = datetime.date.today()
        User_choise = st.date_input("Tell me about DoB",min_value=start_date,max_value=end_date)''')
        st.write('example--')
        user_choice = st.date_input("When did you started learning MLAI",min_value=datetime.date(1900,1,1),max_value=datetime.date.today())
        if user_choice:
            st.success(f"You are doing this for {(datetime.date.today()-user_choice).days} days")
        else:
            st.error("Plz select a date")
    with time:
        st.subheader("time_input")
        st.write('st.time_input is used to take a time as input from user')
        st.code('st.time_input("Please give your arrival time")')
        st.write('example--')
        user_choice = st.time_input("Input your birth time")
    

                
expand4 = st.expander("Level 4 - Data upload")
with expand4:
    st.subheader("Data Upload")
    st.write("User can give input as a doc,pdf,excel,csv etc")
    st.write('Multiple file formats are supported by streamlit')
    st.code('st.file_uploader("Upload data")')
    st.write("Example--")
    uploaded_file = st.file_uploader("Please upload your file")
    if uploaded_file:
        if st.toggle("Is uploaded file a image/gif"):
            st.image(uploaded_file)
    st.write("")
    st.write("")

    st.write("To download uploaded file we can use st.download_button")
    st.code('st.download_button("Download file from here",data=uploaded_file,file_name="map.gif")')
    if uploaded_file:
        st.write("Example--")
        st.download_button("Download file from here",data=uploaded_file,file_name="map.gif")

expand5 = st.expander("Advance Option")
with expand5:
    styled_text(text="Kindly wait this part is being prepared",font_family="times new roman",size=40,color='Yellow')
    st.image(r"image\please wait3.gif")
    


# st.switch_page('pages/chapter3.py')
