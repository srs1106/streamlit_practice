# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 12:46:37 2021

@author: Shashank.Shankar
"""

import streamlit as st


from iris_eda_app import run_iris_eda_app
from lang_eda_app import run_lang_eda_app

st.set_page_config(page_title='Hello', 
                   page_icon=':smiley',
                   layout='wide',
                   initial_sidebar_state='expanded')


def main():
    st.title("Main App")
    
    sidebar_menu = ['Home', 'Iris EDA', 
                    'Languages EDA', 'About']
    choices = st.sidebar.selectbox("Menu", sidebar_menu)
    
    if choices == 'Home':
        st.subheader("Welcome to the Home Page!")
    
    elif choices == 'Iris EDA':
        run_iris_eda_app()
        
    elif choices == 'Languages EDA':
        run_lang_eda_app()
    
    else:
        st.subheader("About")
    
    
    


if __name__ == '__main__':
    main()






    

