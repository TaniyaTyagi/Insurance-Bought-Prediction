import pickle
import streamlit as st
model1 = pickle.load(open("mymodel.pkl","rb"))
def model_deploy():
    st.title("Insurance Bought Prediction")
    age=st.number_input("Enter Your Age : ")
    predi = st.button("Predict")

    if predi:
        x = model1.predict([[age]])
        if x==0:
            st.error("Person will not buy insurance")
        else:
            st.success("Person will buy insurance")
model_deploy()