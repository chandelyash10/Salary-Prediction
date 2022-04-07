import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np
data = pd.read_csv("data//Salary_Data.csv")
x = np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data["Salary"]))
st.title("salary predictor app")
nav=st.sidebar.radio("Navigation",["home","prediction","contribute"])
if nav=="home":
    st.write("home")
if st.checkbox("show table"):
    st.table(data)
graph = st.selectbox("what kind of graph ?",["Non-Interactive","Interactive"])
val= st.slider("filter data using yeards",0,20)
data= data.loc[data["YearsExperience"]>= val]
if graph == "Non-Interactive":
    plt.figure(figsize=(10,5))
    plt.scatter(data["YearsExperience"], data["Salary"])
    plt.ylim(0)
    plt.xlabel("Years of expirience")
    plt.ylabel("salary")
    plt.tight_layout()
    st.pyplot()
if graph == "Interactive":
    layout=go.Layout(
        xaxis=dict(range=[0,15]),
        yaxis=dict(range=[0,2300000])
    )

    fig = go.Figure(data=go.Scatter(x=data["YearsExperience"],y=data["Salary"],mode='markers'),layout=layout)
    st.plotly_chart(fig)
    
if nav=="prediction":
    st.header("knowing your salary")
    val= st.number_input("enter your experience",0.00,20.00,step=0.25)
    val= np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]
    if st.button("predict"):
        st.success(f"your predicted salary is{round(pred)}")
    
if nav=="contribute":
    st.write("contribute")
    st.header("primrary data contribution")
    ex= st.number_input("enter your expirience for work",0.00,20.00)
    sal=st.number_input("enter your salary for your work",0.00,80000.00,step=1000.00)

    if st.button("submit"):
        to_add= {"YearsExperience": ex, "Salary": sal}
        to_add=pd.DataFrame(to_add, index=[0])
        to_add.to_csv("Salary_Data.csv",mode='a',header=False,index=False)
        st.success("Data Submitted")