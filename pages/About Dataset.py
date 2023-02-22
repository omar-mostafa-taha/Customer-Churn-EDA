import streamlit as st
from helper import Pie,load_data

st.title('About Dataset')

st.subheader('The dataset includes information about:')

st.markdown('''**1. Customers who left within the last month** – Churn column (Target).\n
**2. Services that each customer has signed up for** – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies.
\n**3. Customer account information** – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges.\n
**4. Demographic info about customers** – gender, age range, and if they have partners and dependents.''')

data = load_data() 
st.success(f'The dataset consist of {data.shape[0]} rows by {data.shape[1]} columns')
st.success('Most of the features are categorical except for 3 columns (tenure , MonthlyCharges , TotalCharges)',)
fig = Pie(data,'Churn')
st.subheader('Churn Distribution')
st.plotly_chart(fig)


# st.subheader('Churn Rates')
# features = ['gender','SeniorCitizen','Partner','Dependents','Contract','PaperlessBilling','PaymentMethod','PhoneService','MultipleLines','InternetService'
#         ,'OnlineSecurity','OnlineBackup','DeviceProtection'
#         ,'TechSupport','StreamingTV','StreamingMovies']
# plot_churn_rate(features)

if st.checkbox('Show Data'):
    st.dataframe(data)





