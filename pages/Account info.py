from helper import show_plots , load_data , hist
import streamlit as st

df = load_data()
df_churn = df[ df['Churn']== 1 ]
df_retained = df[ df['Churn']== 0 ]
#==================Categorical Features==========================
st.header('Account info Analysis')
st.subheader('Categorical Features')
cat_features=['Contract','PaperlessBilling','PaymentMethod']
show_plots(cat_features)
#==================Numerical Features==========================
st.subheader('Numerical Features')
feature = st.selectbox('**Choose Feature**',['tenure','MonthlyCharges','TotalCharges'])
churn_hist = st.radio('**Show Plot for**: ',('All ','Churn ','Retained '))
if churn_hist == 'Churn ':
    fig = hist(df_churn,feature)
        
elif churn_hist == 'Retained ':
    fig = hist(df_retained,feature)
else:
    fig = hist(df,feature)
    #end of radio button
    
    #plot kind radio button
st.plotly_chart(fig)


