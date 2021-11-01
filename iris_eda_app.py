# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:05:22 2021

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


def run_iris_eda_app():
    st.subheader("This is the Iris EDA Page!")
    df = pd.read_csv("data/iris.csv")
    
    st.write("Iris Dataframe Head")
    st.dataframe(df.head())
    
    # Pie Chart
    st.write("Sepal Length per Species")
    fig = px.pie(df, values='sepal_length', 
                  names='species')
    st.plotly_chart(fig, use_container_width=True)
    
    species_group = df.groupby('species').sum()
    
    # Stacked Bar Chart
    st.write('Sepal Length/Width & Petal Length/Width per Species')
    fig2 = px.bar(species_group,
                  x=['virginica', 'versicolor',
                     'setosa'], 
                  y=['sepal_length', 'sepal_width',
                     'petal_length', 'petal_width'])
    st.plotly_chart(fig2, use_container_width=True)
    
    st.write(species_group)
    
    colors = {'virginica':'red', 'versicolor':'blue', 
              'setosa':'green'}
    
    # Altair Chart
    c = alt.Chart(df).mark_circle().encode(
        x='sepal_length', y='petal_length',
        color ='species')
    
    st.altair_chart(c, use_container_width=True)
    
    # Scatter Plot
    st.write('Sepal Length v/s Petal Length')
    fig3, ax = plt.subplots()
    ax.scatter(x='sepal_length', y='petal_length', 
               data=df, c=df['species'].map(colors))
    st.pyplot(fig3, use_container_width=True)