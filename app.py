import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import calendar

st.title("Uber Rides Data Analysis ")

# Load CSV file
uploaded_file = st.file_uploader("Upload 'My Uber Drives - 2016.csv'", type=["csv"])

if uploaded_file is not None:
    uber_df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.write(uber_df.head())

    st.subheader("Missing Values")
    st.write(uber_df.isnull().sum())

    uber_df = uber_df.dropna()

    # Convert dates to datetime format
    uber_df['START_DATE*'] = pd.to_datetime(uber_df['START_DATE*'], format='%m/%d/%Y %H:%M')
    uber_df['END_DATE*'] = pd.to_datetime(uber_df['END_DATE*'], format='%m/%d/%Y %H:%M')

    # Extract datetime features
    uber_df['Hour'] = uber_df['START_DATE*'].dt.hour
    uber_df['Day'] = uber_df['START_DATE*'].dt.day
    uber_df['Month'] = uber_df['START_DATE*'].dt.month
    uber_df['weekday'] = uber_df['START_DATE*'].dt.dayofweek
    uber_df['weekday_name'] = uber_df['START_DATE*'].dt.day_name()

    st.subheader("Processed Data Preview")
    st.write(uber_df.head())

    # Category count plot
    st.subheader("Ride Categories")
    fig1, ax1 = plt.subplots()
    sns.countplot(x='CATEGORY*', data=uber_df, ax=ax1)
    ax1.set_title('Count of Rides by Category')
    st.pyplot(fig1)

    # Hourly distribution
    st.subheader("Hourly Distribution of Rides")
    fig2, ax2 = plt.subplots()
    sns.countplot(x='Hour', data=uber_df, ax=ax2)
    ax2.set_title('Rides per Hour')
    st.pyplot(fig2)

    # Weekday distribution
    st.subheader("Weekday Distribution of Rides")
    fig3, ax3 = plt.subplots()
    sns.countplot(x='weekday_name', data=uber_df, order=calendar.day_name, ax=ax3)
    ax3.set_title('Rides per Day of the Week')
    st.pyplot(fig3)
else:
    st.info("Please upload the CSV file to proceed.")
