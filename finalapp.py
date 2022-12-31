import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title="Prognosis", page_icon=":tada:", layout="wide")
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_tno6cg2w.json")
img_contact_form = Image.open("assets/z1.jpg")



with st.container():
    st.header("Lets see the  skills required in your favorite job 😉. ")
    option = st.selectbox('Select Any one job :',
                          ("Cloud Solutions Architect","Software Architect","Network Architect","Software Applications Architect","Data Architect","Solutions Architect","Site Reliability Engineer","Computer and Information Research Scientist","Data Scientist","Development Operations Engineer","IT Operations Manager","Data Engineer","IT Project Manager","Information Technology Manager","Hardware Engineer","Senior Web Developer","Software Engineer","Computer Hardware Engineer","Wireless RF Network Engineer","Information Systems Manager","Computer Scientist","Business Intelligence Developer","Ethical Hacker","IT Systems Engineer","Database Developer","Network Engineer","Mobile Applications Developer","Software Developer","Application Developer","Computer Systems Analyst","IT Business Analyst","Web Developer","Network Administrator","Network and Computer System Administrator","Data Manager","User Interface Designer","Computer Programmer","PHP Developer","Applications Programmer","Data Security Analyst","Video Game Designer","Systems Analyst","IT Security Administrator","Computer Security Specialist","Information Technology Auditor"
    ))
    st.write("---")
    
profession=option


df=pd.read_csv("assets/"+profession+".csv")
# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()
# Encode labels in column 'species'.
df['skills/dates']= label_encoder.fit_transform(df['skills/dates'])
df['skills/dates'].unique()
first = list(df.columns)
l=[]
for i in range (1,11):
    x = np.arange(df['skills/dates'].size)
    fit = np.polyfit(x, df[first[i]], deg=1)
    l.append(str(fit[0]))
    #Fit function : y = mx + c [linear regression ]
    fit_function = np.poly1d(fit)
    #Linear regression plot
    plt_1=plt.figure(figsize=(7,4))
    plt.plot(df['skills/dates'], fit_function(x))
    #Time series data plot
    plt.plot(df['skills/dates'], df[first[i]])
    plt.xticks(rotation=90);
    plt.xlabel('Dates')
    plt.ylabel('trends')
    plt.title(first[i])
    plt.savefig('books_read.png')
    image = Image.open('books_read.png')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image)
    with text_column:
        st.subheader( "Slope : " + str(fit[0]))  

final_list2=l
final_list=first
for i in range (0,10):
    for j in range(0,9-i):
        if(final_list2[j]>final_list2[j+1]):
            temp=final_list2[j]
            final_list2[j]=final_list2[j+1]
            final_list2[j+1]=temp
            temp=final_list[j]
            final_list[j]=final_list[j+1]
            final_list[j+1]=temp
final_list.reverse() 
st.write("---")

st.header("We recommend you to study these three skillsas they will be the most relevant in the future")
for i in range(0,3):
    p=str(i+1)
    st.subheader(p+"--" +final_list[i])
st.write("---")





with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About our website")
        st.write("##")
        st.write(
            """
            We have designed a web application that will help any one who is going through the following problems-
            - Have no idea which skills to learn . 
            - Have a bit of idea which roles they want to do in future but have zero idea which skills to learns.
            """
        )
        st.header("working of the website")
        st.write("##")
        st.write("""-We have created a database comprising of skills reqired in different jobs types """)
        st.write("""-After that with the help of machine learning our backend provides the users of this web application to know which skills he should learn to get a job in the desired feild""")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")       
        
# project         
with st.container():
    st.write("---")
    st.header("About Us")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Hi, we are Shivansh and Shivangi :wave:")
        st.subheader("We are from")
        st.subheader("Symbiosis Institute of Technology ")
        st.write("We are passionate about finding a solution to most asked question by a college student which skills shold they learn in the initial phases of their engeenering career ")    
st.write("---")  




local_css("style/style.css")
# ---- CONTACT ----
with st.container():

    st.header("Get In Touch With Us!")
    

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/shivanshnautiyal30@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()    
    