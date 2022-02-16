import os

from app_content import *

MAGE_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/259/mage_1f9d9.png"

# Set page title and favicon.
st.set_page_config(
    page_title="H&M Personalized Fashion Recommendations EDA", page_icon=MAGE_EMOJI_URL,
    layout="wide"
)

# st.sidebar.image('src/utils/streamlit/images/800px-IMDB_Logo_2016.svg.png', width=200)
# st.sidebar.header('Menu')
# st.sidebar.markdown('options')

menu = st.sidebar.selectbox(
    "Select from the dropdown menu to explore",
    ["Intro",
     "Data"
     # ,
     # "Variables",
     # 'Other variables',
     # "Relational variables",
     # "Correlations"
     ],
)

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

if menu == 'Intro':
    set_home()
elif menu == 'Data':
    set_data()
elif menu == 'Variables':
    set_variables()
elif menu == 'More variables':
    set_otras_variables()
elif menu == 'Relationships':
    set_relations()
elif menu == 'Correlation':
    set_arrays()
