import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
import streamlit as st
import seaborn as sns
from app_variables import *
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def load_csv(path):
    global data
    data = pd.read_csv(os.path.join(path))
    return data


def set_home():
    st.write(intro, unsafe_allow_html=True)
    st.write(intro_context, unsafe_allow_html=True)


def set_data():
    data = load_csv(path_articles)

    st.title('Data')
    st.write(dataset_intro, unsafe_allow_html=True)

    st.markdown('### DataFrame `articles`')
    st.markdown(
        'detailed metadata for each article_id available for purchase.')
    st.markdown(f'{len(data.index)} entries  |  {len(data.columns)} columns')
    st.write(data)


def set_data_profiler():
    st.markdown('# Data Profiling')
    st.markdown(
        'Utilize Pandas data profiling tool to gain insight to the dataset.')
    data = pd.read_csv(os.path.join(path_articles))
    pr = ProfileReport(data, explorative=True, orange_mode=True)
    st_profile_report(pr)


def set_data_value_count():
    data = load_csv(path_articles)

    st.markdown('### Explore data by counts')
    st.markdown("### **Select data group:**")
    select_data_group = [
        st.selectbox('Please select a data group to review value counts.', ['product_type_name', 'colour_group_name',
                                                                            'product_group_name',
                                                                            'graphical_appearance_name',
                                                                            'colour_group_name',
                                                                            'perceived_colour_value_name',
                                                                            'perceived_colour_master_name',
                                                                            'index_name', 'section_name',
                                                                            'garment_group_name'])]
    for item in select_data_group:
        fig = plt.figure(figsize=(10, 20))
        sns.countplot(y=item, data=data)
        st.pyplot(fig)
