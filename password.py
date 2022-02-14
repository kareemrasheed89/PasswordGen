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
st.markdown(f"""<h1 style="color:white; text-align:center;font-size:28px; background-color:black;">
PASSWORD GENERATOR APP (Protect Your Credentials With A Strong Passowrd)
""",unsafe_allow_html=True)
st.markdown(f"""<h4 style="color:black ; text-align:center;font-size:14px;">The majority of
users, whether new employees or CEOs, don’t realize that even if their password meets complexity requirements, it doesn’t mean it’s secure. In fact, many common password policies are overdue for an update,
as for several years now <b>cybercriminals</b> have been taking advantage of these password policy weaknesses.
""",unsafe_allow_html=True)
image="password_img.jpg"
st.image(image,use_column_width=True)

lower="abcdefghijklmnopqrstvuyz"
upper=lower.upper()
number="0123456789"
symbols="!@#$%^&*_"

string=lower+upper+number+symbols
length= st.number_input("Input number of character you would like to have", min_value=6, max_value=16)
length=int(length)
st.write("You just tell PASSWORD GENERATOR you need", length, "password character length")
password= "".join(random.sample(string, length))
passgen=st.button("GENERATE PASSWORD")
if passgen:
    col1,col2,col3=st.columns([0.77,3,0.33])
    col2.header("You just generate your passowrd")
    time.sleep(1)
    col1,col2,col3=st.columns([2,3,0.33])
    col2.subheader(password)
    st.balloons()
line="-"*1000
st.write(line)
st.info("HELP : You can reach out to me via EMAIL below if you need a simple WEB AUTOMATION for your organization. Thank you for using my passowrd generator APP")
st.write("")
st.markdown(f"""<p style="color:grey ; text-align:center;font-size:12px;">
Copyright|RashyPy2022(c)
""",unsafe_allow_html=True)

st.markdown(f"""<p style="color:black; text-align:center;font-size:12px;">
✉️kareemrasheed89@gmail.com
""",unsafe_allow_html=True)
st.markdown(f"""<p style="color:black; text-align:center;font-size:12px;">
📞+2348178329565
""",unsafe_allow_html=True)
