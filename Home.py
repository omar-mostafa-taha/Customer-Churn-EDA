import streamlit as st

st.title('Telco Customer Churn EDA')
st.image('churn.png', caption='Let the Butter Churn, Not Your Customers!', use_column_width=True)

dataset = '- View The Dataset on Kaggle  [Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)'
kaggle = '- View my work on Kaggle  [Kaggle notebook](https://www.kaggle.com/omarmostafataha/customer-churn-eda-seaborn-and-plotly-streamlit)'
linked = '- View my LinkedIn Profile  [LinkedIn Profile](https://www.linkedin.com/in/omar-mostafa-96a840210)'
github = '- Check the GitHub Project Repository  [Github Repo](https://github.com/omar-mostafa-taha/Customer_Churn.git)'

st.write('**You Can Also:** ')
st.markdown(dataset, unsafe_allow_html=True)
st.markdown(kaggle, unsafe_allow_html=True)
st.markdown(linked, unsafe_allow_html=True)
st.markdown(github, unsafe_allow_html=True)
#=====================Conclusion=======================
st.markdown("## Conclusion")

# Create a bullet list
st.write("##### Based on Demographic info:")
st.write("- Gender has no effect on Churn Rate .")
st.write("- Seniors are more probable to churn with a churn rate of 0.42 while 0.23 for non seniors.")
st.write("- Customers that don't have partners are more likely to churn with a rate of 0.33.")
st.write("- Customers that don't have dependents are more likely to churn with a rate of 0.32.")


st.write("##### Based on Customr Account info:")
st.write("- Customers With Month to Month contract are more likely to churn with a churn rate of 0.42.")
st.write("- Customers that prefer Paperless Billing are more likely to churn 0.33.")
st.write("- Customers that pay with Electronic Check have a high churn rate 0.44")
st.write("- The longer the customer stay with the corporation the less the churn rate (low: 0.41).")
st.write("- The higher the charges the higher the churn rate (high: 0.34).")


st.write("##### In term of Services:")
st.write("- Customers using Fiber Optic Have a high churn rate (0.42).")
st.write("- Customers Using the rest of the services have low churn rates compared to customers who don't.")
