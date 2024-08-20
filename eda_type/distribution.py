#Distribution plots are used for univariant analysis- focus on one column at a time
#Range of DataSpread
#Distribution Plot: Used for continuous data to show the distribution of a variable

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_dist(df):
    if df is not None and not df.empty:
        feature_columns = df.columns.tolist()
        object_type = df.select_dtypes(include=['object']).columns.tolist()
        numeric_type = df.select_dtypes(include=['int64', 'int32', 'float32','float64']).columns.tolist()

        plot_relational = ['Histogram Plot', 'KDE Plot', 'Box Plot']   #Line plot is mostly used for time-series data
        plot = st.selectbox("Type of relational plot" , options = plot_relational, index= None) 
            
        if plot == 'Histogram Plot':
            x_axis = st.selectbox("Select the X_axis", numeric_type ,index = None)
            if st.button("Generate Plot"):
                fig = sns.displot(x=x_axis, data=df, kind='hist')
                st.pyplot(fig)

        elif plot == 'KDE Plot':# Continuous plot which gives hint of probablity
            x_axis = st.selectbox("Select the X_axis", numeric_type ,index = None)
            if st.button("Generate Plot"):
                fig = sns.displot(x=x_axis,data=df, kind='kde')
                st.pyplot(fig)
                
        elif plot == 'Box Plot':
            st.info("Shows the distribution of quantitative data variable.")
            numerical_var = st.selectbox("Select the Numerical Variable", numeric_type ,index = None) 
            if st.button("Generate Plot"):
                fig = sns.catplot(x=numerical_var,data=df, kind='box')
                st.pyplot(fig)