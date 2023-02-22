from helper import show_plots
import streamlit as st

st.header('Demographic info Analysis')
features=['gender','SeniorCitizen','Partner','Dependents']
show_plots(features)