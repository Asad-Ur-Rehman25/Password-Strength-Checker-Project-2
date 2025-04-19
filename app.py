import streamlit as st 
import re



st.set_page_config(page_title="passward strength Checker", page_icon="🔒")
st.title("  🔒 password strength Checker")
st.markdown('''''## Welcome To The PassWord Strength Checker! 👋  we will give you tip to create a **STRONG PASSWORD** ''''') 
Password = st.text_input('enter Password', type='password')
feedback =[]
score =0
if Password:
    if len(Password) >= 8:
        score = score + 1
    else:
        feedback.append("password should be atleast 8 Character")
    if re.search(r'[A-Z]',Password) and re.search(r'[a-z]',Password):
        score = score + 1
    else:
        feedback.append("password should be used upper and lower case alpha") 
    if re.search(r'\d',Password):
        score = score + 1
    else:
        feedback.append("password should be used Number") 
    if re.search(r'[@#$%&*]',Password):
        score = score + 1
    else:
        feedback.append("password should be used Special symbol ") 
    if score ==4:
        feedback.append("YOUR PASSWORD IS STRONG👍")
    elif score == 3:  
        feedback.append("YOUR PASSWORD IS MEDIUM STRENGTH 👍")
    else:
        feedback.append("YOUR PASSWORD IS WEAK STRENGTH 👍")
    if feedback:
        for tip in feedback:
            st.write(tip)
else:
    ("please Enter Your password")