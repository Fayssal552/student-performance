import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


@st.cache
def load_data():
    df_train = pd.read_csv('student-mat.csv')

    df_train['schoolsup'] = df_train['schoolsup'].replace({'yes':1, 'no':0})
    df_train['famsup'] = df_train['famsup'].replace({'yes':1, 'no':0})
    df_train['paid'] = df_train['paid'].replace({'yes':1, 'no':0})
    df_train['activities'] = df_train['activities'].replace({'yes':1, 'no':0})
    df_train['higher'] = df_train['higher'].replace({'yes':1, 'no':0})
    df_train['internet'] = df_train['internet'].replace({'yes':1, 'no':0})
    df_train['romantic'] = df_train['romantic'].replace({'yes':1, 'no':0})

    return df_train

df_train = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2020
    """
    )
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )

    
    data = df_train.groupby(["studytime"])["G3"].mean().sort_values(ascending=True)
    st.line_chart(data)