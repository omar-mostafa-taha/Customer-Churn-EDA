import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st
sns.set()

@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv('Telco-Customer-Churn.csv')
    return df

def count(df,col,set_hue=None):
    val = df[col].value_counts(normalize = True)
    fig = px.bar(val,y=val,color=val.index,height = 500, width = 500)
    fig.update_layout(xaxis_title = col, yaxis_title = 'Percentage')
    return fig

def Pie(df,col):
    val = df[col].value_counts(normalize = True)
    fig = px.pie(values=val.values,names=val.index,height = 450, width = 450)
    #fig.update_layout(xaxis_title = col, yaxis_title = 'Percentage')
    return fig

def hist(df,col,set_hue=None):
    fig = px.histogram(df,x=col)
    return fig

def churn_rate(df,col):
    df2 = df
    df2['Churn'].replace(to_replace = 'Yes', value = 1 , inplace = True)
    df2['Churn'].replace(to_replace = 'No',  value = 0,  inplace =True)
    val = df2.groupby([col])['Churn'].mean()
    fig = px.bar(val,color=val.index,width = 500,height=500)
    fig.update_layout(xaxis_title = col, yaxis_title = 'Churn Rate')
    return fig
    

def show_plots(features):
    df = load_data()
    df_churn = df[ df['Churn']=='Yes' ]
    df_retained = df[ df['Churn']=='No' ]
    feature = st.selectbox('**Choose Feature**',tuple(features))
    #==============================================================
    #Churn radio button
    churn = st.radio('**Show Plot for**: ',('All','Churn','Retained'))
    if churn == 'Churn':
        bar = count(df_churn,feature)
        pie = Pie(df_churn,feature)
        
    elif churn == 'Retained':
        bar = count(df_retained,feature)
        pie = Pie(df_retained,feature)
    else:
        bar = count(df,feature)
        pie = Pie(df,feature)
    #end of radio button
    
    #plot kind radio button
    kind = st.radio('**Show Plot as**: ',('Pie','Bar'))
    if kind == 'Bar':
        st.plotly_chart(bar)
    else:
        st.plotly_chart(pie)
    #end of radio button
    #===============================================================


def plot_churn_rate(features):
    df = load_data()
    feature = st.selectbox('**Choose Feature**',tuple(features))
    fig = churn_rate(df,feature)
    st.plotly_chart(fig)






