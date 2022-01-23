# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 00:18:18 2022

@author: Adarsh
"""


import numpy as np
import pickle
import pandas as pd
import time
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

import streamlit as st

import webbrowser

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(variance,skewness,curtosis,entropy):
   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
  
    print(prediction)
    return prediction



def main():
    st.title("Bank Note Authenticator")
    html_temp = """
    <div style="background-color:SlateBlue;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance"," ")
    skewness = st.text_input("skewness"," ")
    curtosis = st.text_input("curtosis"," ")
    entropy = st.text_input("entropy"," ")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    if result == 1:
        with st.spinner('Wait for it...'):
            time.sleep(1)
        st.success('You have the Genuine Note'.format(result))
        st.balloons()
        
    if result == 0:
        with st.spinner('Wait for it...'):
            time.sleep(1)
        st.error('You Have the Fake Note'.format(result))
    
    if st.button("About"):
        html_temp_footer = """
           <p class='footer-description'>Made with &#10084;&#65039; by Adarsh Malviya</p>
        """

        st.markdown(html_temp_footer,unsafe_allow_html = True)
        
url = 'www.github.com/adarshmalviy'
url2 = 'www.linkedin.com/in/adarshmalviy'       
left, right = st.columns(2)
with left:
    if st.button('GitHub'):
        webbrowser.open_new_tab(url1)
with right:
    if st.button('Linkedin'):
        webbrowser.open_new_tab(url2)
        
        
        
if __name__=='__main__':
    main()
    
        