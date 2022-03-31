# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:21:51 2022

@author: haind
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/Haindhavi/model/trained_model.sav','rb'))

# creating a function for prediction

def Machine_failure_prediction(input_data):

    #changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
       print('The machine is not likely to fail')
    else:
       print('The machine is likely to fail')

def Main():   
    
    #giving a title
    st.title("Machine failure prediction Web App")
    
    #getting the input data from the user
    
    Airtemperature = st.text_input("Air Temperature value")
    Processtemperature = st.text_input("Process Temperature value")
    Rotationalspeed = st.text_input("Rotational Speed value")
    Torque = st.text_input("Torque value")
    Toolwear = st.text_input("Tool Wear value")
    Toolwearfailure = st.text_input("Tool Wear Failure value")
    Heatdissipationfailure = st.text_input("Heat dissipation failure value")
    Powerfailure = st.text_input("Power failure value")
    Overstrainfailure = st.text_input("Overstrain failure value")
    Randomfailures = st.text_input("Random failures value")    
    
    
    # code for prediction
    Machine_failure = ''
    
    # creating a button for prediction
    
    if st.button("Machine failure Test result"):
        Machine_failure = Machine_failure_prediction([Airtemperature,Processtemperature,Rotationalspeed,Torque,Toolwear,Toolwearfailure,Heatdissipationfailure,Powerfailure,Overstrainfailure,Randomfailures])
    
    st.success(Machine_failure)
    
if __name__=='__main__':
    Main()