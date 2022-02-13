mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"kareemrasheed89@outlook.com\"\n\
" > ~/.streamlit/credentials.toml

echo "
[theme]\n\
primaryColor = '#FF4B4B'\n\
backgroundColor = '#FFFFFF'
secondaryBackgroundColor = '#F0F2F6'
textColor = '#31333F'
font = 'sans serif'
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

# echo "\
# [theme]\n\
# primaryColor = '#7792E3'\n\
# backgroundColor = '#273346'
# \n\
# secondaryBackgroundColor = '#B9F1C0'
# \n\
# textColor = '#FFFFFF'
# \n\
# font = 'sans serif'\n\
# " >> ~/.streamlit/config.toml
