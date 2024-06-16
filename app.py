import streamlit as st

st.title('Hello Guys, How u doing?')
st.header('this is a header')
st.subheader('this is a subheader')
st.text('this is a textual format')


st.markdown('# Hi')
st.markdown('## hiii')
st.success('data is submitted')         # success
st.info('Information')                  #info
st.warning('warning')                   #warning
st.error("Error")                        #error
st.exception( ZeroDivisionError('Division is not possible with zero'))     #exception
st.write("range(1,10)")
st.write(range(1,10))
st.write(1+2+3)

st.code('x = 10 \n' 
        'for i in range(x):\n'
        '    print(i)')


st.checkbox('male')                      #checkbox 
if(st.checkbox('Adult')):
    st.write('you are an adult')

radioButton = st.radio('Select: ' , ('male ', 'female'))            #radiobutton

if(radioButton == 'Male'):
    st.write("you are a male")
elif(radioButton == 'feMale'):
    st.write("you are a female") 

st.subheader('Select Box')                        # Select Box
selectBox = st.selectbox("Data Science : ",  [   'Data analysis ', 'Web Scrapping',
                                                 'Machine Learning','Deep Learning' ,
                                                 'NLP'])

st.write("You have selected :  " , selectBox)

st.subheader('MultiSelect Box')                # MultiselectBox

multiselectBox = st.multiselect("Data Science : ",  [   'Data analysis ', 'Web Scrapping',
                                                        'Machine Learning','Deep Learning' ,
                                                        'NLP'])

st.write("You have selected" , len(multiselectBox) ,"courses")

st.subheader("Button")                       # Button
if(st.button('Click Me')):
    st.write("Someone clicked me") 
       
st.subheader('slider')                       # slider       
val = st.slider('Selec the level', 1,10,step=1)
 
st.write('val is : ' ,val)

st.subheader("Text Input")                    # Text Input
username = st.text_input('Username : ')
password = st.text_input("password : " ,type = 'password')

st.subheader("Text Area")                      # Text area
textArea = st.text_area("Wrute something good about you in 20 words: " )
st.write(textArea)

st.subheader("Input number")             # number number
st.number_input("Select your age", 18,110 )

st.subheader("Input date")             # number date
st.date_input("Select the date")

st.subheader("Input time")             # number time
st.time_input("select the time")

