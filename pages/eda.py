import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import eda_type.relational as relational
import eda_type.distribution as distribution
import eda_type.categorical as categorical


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

def show_eda(df):     
    if df is not None and not df.empty:
        st.markdown(
        '<h1 class="centered-title">CSV Data Analysis and Model Evaluation</h1>',
        unsafe_allow_html=True
        )
        st.write(df.head())

        plot_type = ['Relational','Distribution- UnivariantAnalysis','Categorical']
        plot_category = st.selectbox("Select the type of plot", options = plot_type, index= None)

        if plot_category == 'Relational':
            st.info("Relational Plots are used to view relationship between numerical data")
            relational.show_rel(df)

        elif plot_category == 'Distribution- UnivariantAnalysis':
            st.info("Distribution Plots are used for univariant - Analysis")
            distribution.show_dist(df)

        elif plot_category == 'Categorical':
            st.info("Categorical plots are used to compare the distribution, frequency, or relationship of categorical data.")
            categorical.show_cat(df)
    
    else:
        st.warning("The DataFrame is empty or invalid.")

