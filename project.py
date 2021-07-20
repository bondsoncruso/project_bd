import streamlit as st
from streamlit import beta_util
from datetime import datetime
from streamlit import beta_util

st.set_page_config(page_title='Softy',page_icon=':icecream:')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.balloons()

# st.title('ti/tle')
relation_date = datetime(2019, 9,10)
today_date = datetime.today()
days_since_together = (today_date - relation_date).days
months_since_together = round((today_date - relation_date).days/30)
years_since_together = round((today_date - relation_date).days/365)
birth_date = datetime(1994,7,29)
def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    
    return ((delta1 if delta1 > now else delta2) - now).days

days_to_next_bd = calculate_dates(birth_date, datetime.now())
st.title(f':heart:{days_since_together} Days/ {months_since_together} Months/ {years_since_together} Years')
st.header(' since together')

# col1.title(f':heart:{days_since_together} Days')
# col1.header(' since together')

st.title(f':birthday:{days_to_next_bd} Days')
st.header('left until next birthday')
if st.button('Click here if feeling sad'):
    video_file = open('myv', 'rb')
    video_bytes = video_file.read()
    st.write("""
    'Don't be sad because opposite of sad is das and das not good.' - Aditya Chauhan
    """)
    st.video(video_bytes)
