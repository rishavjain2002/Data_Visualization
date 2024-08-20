import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to handle missing values
def handle_missing_values(df):
    object_type = df.select_dtypes(include=['object']).columns.tolist()
    numeric_type = df.select_dtypes(include=['int64', 'int32', 'float32', 'float64']).columns.tolist()

    for col in df.columns:
        if col in object_type:
            df[col] = df[col].fillna(df[col].mode().iloc[0])
        else:
            df[col] = df[col].fillna(df[col].mean())
    
    return df



# Function to handle duplicate values
def handle_duplicate_values(df):
    df = df.drop_duplicates()
    return df

