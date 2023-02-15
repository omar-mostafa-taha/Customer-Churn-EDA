import streamlit as st

st.title('Telco Customer Churn EDA')
st.image('churn.png', caption='Let the Butter Churn, Not Your Customers!', use_column_width=True)

dataset = '- View The Dataset on Kaggle  [Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)'
kaggle = '- View my work on Kaggle  [Kaggle notebook](https://www.kaggle.com/code/omarmostafataha/customer-churn-eda)'
linked = '- View my LinkedIn Profile  [LinkedIn Profile](https://www.linkedin.com/in/omar-mostafa-96a840210)'
github = '- Check the GitHub Project Repository  [Github Repo](https://github.com/omar-mostafa-taha/Customer_Churn.git)'

st.write('**You Can Also:** ')
st.markdown(dataset, unsafe_allow_html=True)
st.markdown(kaggle, unsafe_allow_html=True)
st.markdown(linked, unsafe_allow_html=True)
st.markdown(github, unsafe_allow_html=True)














