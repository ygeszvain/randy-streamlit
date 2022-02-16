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


def load_csv():
    AnnualTicketSales = pd.read_csv(os.path.join(path_AnnualTicketSales))
    HighestGrossers = pd.read_csv(os.path.join(path_HighestGrossers))
    PopularCreativeTypes = pd.read_csv(os.path.join(path_PopularCreativeTypes))
    TopDistributors = pd.read_csv(os.path.join(path_TopDistributors))
    TopGenres = pd.read_csv(os.path.join(path_TopGenres))
    TopGrossingRatings = pd.read_csv(os.path.join(path_TopGrossingRatings))
    TopGrossingSources = pd.read_csv(os.path.join(path_TopGrossingSources))
    TopProductionMethods = pd.read_csv(os.path.join(path_TopProductionMethods))
    WideReleasesCount = pd.read_csv(os.path.join(path_WideReleasesCount))
    return AnnualTicketSales, HighestGrossers, PopularCreativeTypes, TopDistributors, \
           TopGenres, TopGrossingRatings, TopGrossingSources, TopProductionMethods, WideReleasesCount


def set_home():
    st.write(intro, unsafe_allow_html=True)
    # st.write(intro_context, unsafe_allow_html=True)


def set_data():
    AnnualTicketSales, HighestGrossers, PopularCreativeTypes, TopDistributors, \
    TopGenres, TopGrossingRatings, TopGrossingSources, TopProductionMethods, WideReleasesCount = load_csv()

    st.title('Data Preview')
    st.write(dataset_intro, unsafe_allow_html=True)

    st.markdown('### 1. DataFrame `AnnualTicketSales`')
    st.markdown(
        '')
    st.markdown(f'{len(AnnualTicketSales.index)} entries  |  {len(AnnualTicketSales.columns)} columns')
    st.write(AnnualTicketSales)

    st.markdown('------')

    st.markdown('### 2. DataFrame `HighestGrossers`')
    st.markdown(
        '')
    st.markdown(f'{len(HighestGrossers.index)} entries  |  {len(HighestGrossers.columns)} columns')
    st.write(HighestGrossers)

    st.markdown('------')

    st.markdown('### 3. DataFrame `PopularCreativeTypes`')
    st.markdown(
        '')
    st.markdown(f'{len(PopularCreativeTypes.index)} entries  |  {len(PopularCreativeTypes.columns)} columns')
    st.write(PopularCreativeTypes)

    st.markdown('------')

    st.markdown('### 4. DataFrame `TopDistributors`')
    st.markdown(
        '')
    st.markdown(f'{len(TopDistributors.index)} entries  |  {len(TopDistributors.columns)} columns')
    st.write(TopDistributors)

    st.markdown('------')

    st.markdown('### 5. DataFrame `TopGenres`')
    st.markdown(
        '')
    st.markdown(f'{len(TopGenres.index)} entries  |  {len(TopGenres.columns)} columns')
    st.write(TopGenres)

    st.markdown('------')

    st.markdown('### 6. DataFrame `TopGrossingRatings`')
    st.markdown(
        '')
    st.markdown(f'{len(TopGrossingRatings.index)} entries  |  {len(TopGrossingRatings.columns)} columns')
    st.write(TopGrossingRatings)

    st.markdown('------')

    st.markdown('### 7. DataFrame `TopGrossingSources`')
    st.markdown(
        '')
    st.markdown(f'{len(TopGrossingSources.index)} entries  |  {len(TopGrossingSources.columns)} columns')
    st.write(TopGrossingSources)

    st.markdown('------')

    st.markdown('### 8. DataFrame `TopProductionMethods`')
    st.markdown(
        '')
    st.markdown(f'{len(TopProductionMethods.index)} entries  |  {len(TopProductionMethods.columns)} columns')
    st.write(TopProductionMethods)

    st.markdown('------')

    st.markdown('### 9. DataFrame `WideReleasesCount`')
    st.markdown(
        '')
    st.markdown(f'{len(WideReleasesCount.index)} entries  |  {len(WideReleasesCount.columns)} columns')
    st.write(WideReleasesCount)


def set_data_profiler():
    global data
    AnnualTicketSales, HighestGrossers, PopularCreativeTypes, TopDistributors, \
    TopGenres, TopGrossingRatings, TopGrossingSources, TopProductionMethods, WideReleasesCount = load_csv()

    st.markdown('# Data Profiling')
    st.markdown(
        'Utilize Pandas data profiling tool to gain insight to the dataset.')

    st.markdown("### **Select data set:**")
    select_data_set = [
        st.selectbox('Please select a data set to run data profiler.', ['AnnualTicketSales', 'HighestGrossers',
                                                                        'PopularCreativeTypes', 'TopDistributors',
                                                                        'TopGenres', 'TopGrossingRatings',
                                                                        'TopGrossingSources', 'TopProductionMethods',
                                                                        'WideReleasesCount'])]

    for selection in select_data_set:

        if selection == 'AnnualTicketSales':
            data = AnnualTicketSales
        elif selection == 'HighestGrossers':
            data = HighestGrossers
        elif selection == 'PopularCreativeTypes':
            data = PopularCreativeTypes
        elif selection == 'TopDistributors':
            data = TopDistributors
        elif selection == 'TopGenres':
            data = TopGenres
        elif selection == 'TopGrossingRatings':
            data = TopGrossingRatings
        elif selection == 'TopGrossingSources':
            data = TopGrossingSources
        elif selection == 'TopProductionMethods':
            data = TopProductionMethods
        elif selection == 'WideReleasesCount':
            data = WideReleasesCount

    pr = ProfileReport(data, explorative=True, orange_mode=True)
    st_profile_report(pr)


def set_data_exploration():
    st.markdown('# In progress')
