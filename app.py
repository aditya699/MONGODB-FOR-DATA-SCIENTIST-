import streamlit as st
import pymongo
# Add a title
st.title('Subscribe to Newsletters')
# Add a header
st.header('Please fill out your information:')
# Add text
st.subheader('Personal Information')
# Get user inputs
name = st.text_input('Name')
age = st.number_input('Age', 1, 100, step=1, key='age')
gender = st.selectbox('Gender', ['Male', 'Female'])
email=st.text_input('Email')
# Add a button
if st.button('Submit'):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient['mynewdb']
    mycol=mydb['Newsletter_Sub']
    data={"Name":name,"Email":email,"Gender":gender,"Age":age}
    z=mycol.insert_one(data)
    st.success('Your Are Registered for the newsletters !!!!!!!')

