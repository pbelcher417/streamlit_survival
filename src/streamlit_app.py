import streamlit as st
import numpy as np
import pandas as pd
import lifelines
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
# from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Overall Survival",
    layout="wide"
)

st.sidebar.success("Select an option")

st.title("Customer Survival Analysis")

col = st.columns((4, 2), gap='medium')

df = pd.read_csv("C:\\Users\\pbelc\\Documents\\Streamlit_Training\\Survival_Application\\WA_Fn-UseC_-Telco-Customer-Churn.csv")
df['churn'] = [1 if x == 'Yes' else 0 for x in df['Churn']]
df['SeniorCitizen'] = ["Yes" if x == 1 else "No" for x in df['SeniorCitizen']]

gender = df['gender'].unique().tolist()
SeniorCitizen = df['SeniorCitizen'].unique().tolist()
Partner = df['Partner'].unique().tolist()
Dependents = df['Dependents'].unique().tolist()
PhoneService = df['PhoneService'].unique().tolist()
MultipleLines = df['MultipleLines'].unique().tolist()
InternetService = df['InternetService'].unique().tolist()
OnlineSecurity = df['OnlineSecurity'].unique().tolist()
OnlineBackup = df['OnlineBackup'].unique().tolist()
DeviceProtection = df['DeviceProtection'].unique().tolist()
TechSupport = df['TechSupport'].unique().tolist()
StreamingTV = df['StreamingTV'].unique().tolist()
StreamingMovies = df['StreamingMovies'].unique().tolist()
Contract = df['Contract'].unique().tolist()
PaperlessBilling = df['PaperlessBilling'].unique().tolist()
PaymentMethod = df['PaymentMethod'].unique().tolist()

# plt.title('Kaplan-Meier Curve')

with col[1]: 
    gender_flag = st.multiselect(
        'Select Gender',
        gender,
        default=gender
    )
    SeniorCitizen_flag = st.multiselect(
        'Customer is a senior citizen',
        SeniorCitizen,
        default=SeniorCitizen
    )
    Partner_flag = st.multiselect(
        'Customer has a partner',
        Partner,
        default=Partner
    )
    Dependents_flag = st.multiselect(
        'Customer has dependents',
        Dependents,
        default=Dependents
    )
    PhoneService_flag = st.multiselect(
        'Customer has phone service?',
        PhoneService,
        default=PhoneService
    )
    MultipleLines_flag = st.multiselect(
        'Customer has multiple lines?',
        MultipleLines,
        default=MultipleLines
    )

with col[0]:

    filtered = df[df["gender"].isin(gender_flag) & df['SeniorCitizen'].isin(SeniorCitizen_flag) & df["Partner"].isin(Partner_flag) 
                  & df['Dependents'].isin(Dependents_flag) & df["PhoneService"].isin(PhoneService_flag) & df['MultipleLines'].isin(MultipleLines_flag)]
 
    T = filtered['tenure'] # months
    E = filtered['churn']

    kmf = KaplanMeierFitter()
    kmf.fit(T, event_observed=E)
    fig, ax = plt.subplots() #solved by add this line 
    ax = kmf.plot()
    ax.set_ylim([0, 1])
    plt.xlabel("Tenure (months)")
    plt.ylabel("% customers remaining")
    st.pyplot(fig)


