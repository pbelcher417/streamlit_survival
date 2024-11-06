# Streamlit Survival

## Purpose
A simple Streamlit Application as a POC for creating an interactive Survival Analysis Report. Note this application is specific to the "Telco Churn" dataset from Kaggle, but could be adapted for other datasets.
This application uses the lifelines library in Python. https://lifelines.readthedocs.io/en/latest/

## What is Survival Analysis
"Survival Analysis is a is a collection of statistical procedures for data analysis where the outcome variable of interest is time until an event occurs. 
Because of censoring–the nonobservation of the event of interest after a period of follow-up–a proportion of the survival times of interest will often be unknown."

In layman's terms Survival Analysis allows us to track the behaviour of an entity (a customer, a person etc) over time until whatever event we are looking for occurs.
Originally Survival Analysis was applied to medical trials, but is also applicable to subscription based customer churn, where the "event" we are interested in is a customer leaving.

Survival Analysis allows us to stastically handle "Censored" subjects. This is where a customer has not yet performed the "event" that we are looking for. 
This can be incredibly important when launching new products where a large % of our customers may not have churned yet.

Currently the application only uses the Kaplan-Meier estimator which is great for a descriptive view of survival rates.
However, long term aim is to add Cox Proportional Hazards as a predictive method.

