# Import Required Libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Function to generate synthetic data
def generate_data(n_samples, mean, std):
    np.random.seed(42)
    data = np.random.normal(mean, std, n_samples)
    return data

# Generate synthetic data
n_samples = 1000
mean = 50
std = 10
data = generate_data(n_samples, mean, std)

# Function to calculate confidence interval
def compute_confidence_interval(data, confidence=0.95):
    n = len(data)
    m, se = np.mean(data), stats.sem(data)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

mean, lower, upper = compute_confidence_interval(data)

# Creating Streamlit app
st.title("Confidence Interval Demonstration")

st.sidebar.header("User Input Parameters")
n_samples = st.sidebar.slider('Number of samples', min_value=100, max_value=2000, value=1000, step=100)
mean = st.sidebar.slider('Mean', min_value=0, max_value=100, value=50, step=1)
std = st.sidebar.slider('Standard Deviation', min_value=1, max_value=30, value=10, step=1)

data = generate_data(n_samples, mean, std)
mean, lower, upper = compute_confidence_interval(data)

st.write(f"Mean: {mean:.2f}")
st.write(f"95% Confidence Interval: [{lower:.2f}, {upper:.2f}]")

fig, ax = plt.subplots()
sns.histplot(data, kde=True, color='skyblue', ax=ax)
ax.axvline(mean, color='green', linestyle='--')
ax.axvline(lower, color='red', linestyle='--')
ax.axvline(upper, color='red', linestyle='--')
ax.set(title='Histogram with Confidence Interval', xlabel='Value', ylabel='Frequency')
st.pyplot(fig)

st.sidebar.header("Plot Customization")
color = st.sidebar.color_picker('Pick A Color', '#00f900')
bins = st.sidebar.slider('Number of bins', min_value=10, max_value=100, value=30, step=1)

fig, ax = plt.subplots()
sns.histplot(data, bins=bins, kde=True, color=color, ax=ax)
ax.axvline(mean, color='green', linestyle='--', label=f'Mean: {mean:.2f}')
ax.axvline(lower, color='red', linestyle='--', label=f'Lower CI: {lower:.2f}')
ax.axvline(upper, color='red', linestyle='--', label=f'Upper CI: {upper:.2f}')
ax.set(title='Histogram with Confidence Interval', xlabel='Value', ylabel='Frequency')
ax.legend()
st.pyplot(fig)

st.write("This app demonstrates the concept of confidence intervals using synthetic data. Adjust the parameters on the left sidebar to see how the data and confidence interval change.")
