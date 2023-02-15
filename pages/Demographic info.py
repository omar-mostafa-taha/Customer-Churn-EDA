import helper
import streamlit as st

st.header('Demographic info Analysis')
features=['gender','SeniorCitizen','Partner','Dependents']
helper.show_plots(features)