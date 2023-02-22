from helper import show_plots
import streamlit as st

st.header('Services that each customer has signed up for')
features = ['PhoneService','MultipleLines','InternetService'
        ,'OnlineSecurity','OnlineBackup','DeviceProtection'
        ,'TechSupport','StreamingTV','StreamingMovies']
show_plots(features)
