import os

from app_content import *

# Set page title and favicon.
st.set_page_config(
    page_title="Hollywood Theatrical Market Synopsis 1995 to 2021",
    layout="wide"
)

menu = st.sidebar.selectbox(
    "Select from the dropdown menu to explore",
    ["Intro",
     "Data Preview",
     "Data Profiler",
     "Data Exploration"
     ],
)

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

if menu == 'Intro':
    set_home()
elif menu == 'Data Preview':
    set_data()
elif menu == 'Data Profiler':
    set_data_profiler()
elif menu == 'Data Exploration':
    set_data_exploration()
