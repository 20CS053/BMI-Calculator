# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:25:47 2021

@author: Jinal Kotadia
"""

# BMI App
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

html_code = """
        <div style="background-color: #1abc9c; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">BMI Calculator</h1>
        </div>
        """
components.html(html_code)     

# Image
img = Image.open("bmi.jpg")
st.image(img)

weight = st.number_input("Enter Your Weight:")

status = st.radio("Select height measurement", ['cms', 'meters', 'feet'])

# flag 
h_mode = 0

if(status == 'cms'):
    h_mode = 0
    height = st.number_input("Enter height in cms")

elif(status == 'meters'):
    h_mode = 1    
    height = st.number_input("Enter height in meters")
else:
    h_mode = 2
    height = st.number_input("Enter height in feet")
    
st.text("Calculate BMI")

if(st.button("Calculate BMI")):
    if(h_mode == 0):
        bmi = weight / ((height/100)**2)
    elif(h_mode == 1):
        bmi = weight / (height**2)
    else:
        bmi = weight / ((height/3.2808)**2)

    bmi = round(bmi, 2)

    st.text(bmi)

 # --------------------
    if (bmi < 16):
        st.error("You are Extremely Underweight")
    
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are underweight")
    
    elif (bmi >= 18.5 and bmi < 25):
        st.success("You are Healthy")
        st.balloons()
    
    elif (bmi >= 25 and bmi < 30):
        st.warning("You are Overweight")
    
    elif (bmi >=30):
        st.error("You are Extremely Overweight")







