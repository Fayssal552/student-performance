import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
L = data["model"]




def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### We need some information to predict the salary""")
    
    """
    reason = (
        "course",
        "home",
        "reputation",
        "other",
    )
    """
    schoolsup = (
        "yes",
        "No",
    )
    famsup = (
        "yes",
        "No",
    )
    paid = (
        "yes",
        "No",
    )
    activities = (
        "yes",
        "No",
    )
    higher = (
        "yes",
        "No",
    )
    internet = (
        "yes",
        "No",
    )
    romantic = (
        "yes",
        "No",
    )
    
    #reason = st.selectbox("reason u chose this shool", reason)
    schoolsup = st.selectbox("schoolsup", schoolsup)
    famsup = st.selectbox("famsup", famsup)
    paid = st.selectbox("paid", paid)
    activities = st.selectbox("activities", activities)
    higher = st.selectbox("higher", higher)
    internet = st.selectbox("internet", internet)
    romantic = st.selectbox("romantic", romantic)

    Studytime = st.slider("weekly study time", 1, 4, 1)
    traveltime = st.slider("nbr of hour trvl", 1, 4, 1)
    famrel = st.slider("quality of family relationships", 1, 5, 1)
    freetime = st.slider("free time after school", 1, 5, 1)
    goout = st.slider("going out with friends", 1, 5, 1)
    health = st.slider("current health status", 1, 5, 1)

    ok = st.button("Calculate final note")
    if ok:
        X = np.array([ schoolsup, famsup,paid,
        activities,higher,internet,romantic ,Studytime,traveltime, famrel,freetime,goout,health])
        

        for i in range(7):
            
            if X[i] == "yes":
                X[i]=1
            else:
                X[i]=0
        X=[int(X[j]) for j in range(13)]
        X = np.array(X)
        X=X.reshape(1,-1)

        salary = L.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")