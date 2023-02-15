import helper
import streamlit as st

st.header('Services that each customer has signed up for')
features = ['PhoneService','MultipleLines','InternetService'
        ,'OnlineSecurity','OnlineBackup','DeviceProtection'
        ,'TechSupport','StreamingTV','StreamingMovies']
helper.show_plots(features)
