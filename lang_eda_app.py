# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:07:30 2021

@author: Shashank.Shankar
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import altair as alt


def run_lang_eda_app():
    st.subheader("This is the Languages EDA Page!")
    df2 = pd.read_csv("data/lang_data.csv")
    st.dataframe(df2.head())
    
    lang_list = df2.columns.tolist()
    lang_choices = st.multiselect("Choose Language(s)",
                                  lang_list, default="Python")
    new_df2 = df2[lang_choices]
    
    # Line Chart
    st.write("Language Variation by Week")
    st.line_chart(new_df2, use_container_width=True)
    
    # Area Chart
    st.area_chart(new_df2, use_container_width=True)
    
    st.write("Sum of Programming Languages")
    lang_sum = df2.drop(columns = 'Week').sum(axis=0)
    st.write(lang_sum)
    
    # Pie Chart
    st.write("Distribution of Programming Languages")
    fig4 = px.pie(lang_sum, values=0, 
                  names=lang_sum.index)
    st.plotly_chart(fig4, use_container_width=True)
    
    # Bar Chart
    st.write("Count of Languages")
    fig5 = px.bar(lang_sum, x=lang_sum.index,
                  y=0)
    st.plotly_chart(fig5, use_container_width=True)