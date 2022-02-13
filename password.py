import streamlit as st
import random
import time

st.set_page_config(
page_title="RashyPy Password Generator",
page_icon="🔐",
layout="centered",
initial_sidebar_state="collapsed",
menu_items={
'Get Help': 'https://www.linkedin.com/in/rasheed-babatunde-abdulkareem-bsc-mos-mcdaa-mct-aclc-nimra-322561a4/',
'Report a bug': None,
'About': """I am professional data expert with 10years experience"""
}
)
st.markdown(f"""<h1 style="color:black ; text-align:center;font-size:32px; background-color: grey;">
PASSWORD GENERATOR APP (Protect Your Credentials With A Strong Password)
""",unsafe_allow_html=True)
image="password_img.jpg"
st.image(image,use_column_width=True)

lower="abcdefghijklmnopqrstvuyz"
upper=lower.upper()
number="0123456789"
symbols="!@#$%^&*_"

string=lower+upper+number+symbols
length= 16
password= "".join(random.sample(string, length))
passgen=st.button("GENERATE PASSWORD")
if passgen:
    col1,col2,col3=st.columns([0.77,3,0.33])
    col2.header("You just generate your password")
    time.sleep(1)
    col2.subheader(password)
    st.balloons()
    st.warning("Help: in case you dont need up to 16 character length password, just copy the length you need. This passowrd is UNIQUE and nobody sees yours")
line="_"*1000
st.write(line)
st.write("")
st.markdown(f"""<p style="color:grey ; text-align:center;font-size:12px;">
Copyright|RashyPy2022(c)
""",unsafe_allow_html=True)
st.markdown(f"""<p style="color:black; text-align:center;font-size:12px;">
✉️kareemrasheed89@gmail.com
""",unsafe_allow_html=True)
