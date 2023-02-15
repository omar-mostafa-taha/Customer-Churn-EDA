import helper
import streamlit as st

df = helper.load_data()
df_churn = df[ df['Churn']=='Yes' ]
df_retained = df[ df['Churn']=='No' ]
#==================Categorical Features==========================
st.header('Account info Analysis')
st.subheader('Categorical Features')
cat_features=['Contract','PaperlessBilling','PaymentMethod']
helper.show_plots(cat_features)
#==================Numerical Features==========================
st.subheader('Numerical Features')
feature = st.selectbox('**Choose Feature**',['tenure','MonthlyCharges','TotalCharges'])
churn_hist = st.radio('**Show Plot for**: ',('All ','Churn ','Retained '))
if churn_hist == 'Churn ':
    fig = helper.hist(df_churn,feature)
        
elif churn_hist == 'Retained ':
    fig = helper.hist(df_retained,feature)
else:
    fig = helper.hist(df,feature)
    #end of radio button
    
    #plot kind radio button
st.plotly_chart(fig)


