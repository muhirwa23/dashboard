# starting stream lit  
import streamlit as st # APP making  framework
import pandas as pd # data handling
import numpy as np  # Numerical computation
import matplotlib.pyplot as plt # visualization
import  seaborn as sns # visualization
st.title('My first app')
st.write("Here's our first attem")
# text  handling  
st.text("Hello streamlit")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("### This is a markdown , `code`")
st.success("Successful")
# input
st.text_input("Enter Your Name", "Type Here ...")
st.number_input("Enter a Number", 0, 50)
st.text_area("Area for Text")
st.date_input("Input Date")
# display data  
st.write("Displaying Data")
st.write(range(10))
# read  data  
df = pd.read_csv(r"\data\customer_churn_dataset.csv")
st.dataframe(df.head(5))
st.table(df.head(5))
# display  graph
st.write("Displaying Graph")
st.bar_chart(df.head(5))
# describing  data  
st.write("Describing Data")
st.write(df.describe())    
# sidebar 
st.sidebar.title("Sidebar")
st.sidebar.text("This is a sidebar")
st.sidebar.number_input("Enter a Number", 0, 50)
st.sidebar.text_area("Area for Text")
st.sidebar.radio("Choose a Gender", ["Male", "Female"])
st.sidebar.checkbox("Check me out")
st.sidebar.selectbox("Choose a Gender", ["Male", "Female"])
st.sidebar.multiselect("Choose a Gender", ["Male", "Female"])  
# adding a button
st.button("Click me")
st.button("Click me", key="1")
st.button("Click me", key="2")
# ADDING  METRIC 
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F", border=True)
col2.metric("Temperature", "70 °F", "1.2 °F",border=True)
col3.metric("Temperature", "70 °F", "1.2 °F",border=True) 
st.write(df['churn'] .value_counts())
st.sidebar.multiselect("Choose a any column", ['gender', 'SeniorCitizen', 'Partner', 'Dependents'])  


