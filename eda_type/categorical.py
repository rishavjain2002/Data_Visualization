

#Bar Plot
#A bar plot shows the relationship between a categorical variable and a continuous variable.

# Count Plot
# Similar to a bar plot but specifically for showing the count of observations in each category.




import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def show_cat(df):
    if df is not None and not df.empty:
        feature_columns = df.columns.tolist()
        object_type = df.select_dtypes(include=['object']).columns.tolist()
        numeric_type = df.select_dtypes(include=['int64', 'int32', 'float32','float64']).columns.tolist()

        plot_relational = ['Bar Plot', 'Count Plot']   #Line plot is mostly used for time-series data
        plot = st.selectbox("Type of relational plot" , options = plot_relational, index= None) 
            
        if plot == 'Bar Plot':
            estimator_function = ['Sum', 'Average', 'Median']
            with st.container():
                col1, col2, col3= st.columns(3)
                st.info("Bar Plot shows the aggregate relationship between a categorical variable and a continuous variable.")
                with col1:
                    x_axis = st.selectbox("Select the Categorical Variable", feature_columns ,index = None)
                with col2:
                    y_axis = st.selectbox("Select the Numeric Variable", numeric_type, index = None) 
                with col3:
                    estimator_val = st.selectbox("Select the aggregate estimator", estimator_function, index = None)
                    

            if st.button("Generate Plot"):
                plt.figure(figsize=(10, 6))  # Create a new figure
                if estimator_val == 'Sum':
                    fig = sns.barplot(x=x_axis, y=y_axis, data=df, estimator=sum)
                    
                elif estimator_val == 'Average':
                    fig = sns.barplot(x=x_axis, y=y_axis, data=df, estimator=np.median)
                    
                elif estimator_val == 'Median':
                    fig = sns.barplot(x=x_axis, y=y_axis, data=df, estimator=np.median)
                st.pyplot(plt)
                plt.close()
                

        elif plot == 'Count Plot':
            st.info("Similar to a bar plot but specifically for showing the count of observations in each category.")
            with st.container():
                col1, col2= st.columns(2)

                with col1:
                    cat_col = st.selectbox("Select the categorical variable", feature_columns ,index = None)
                with col2:
                    Hue = st.selectbox("Hue Parameter", feature_columns, index = None) 
            
            if st.button("Generate Plot"):
                fig = sns.catplot(x=cat_col, hue=Hue, data=df, kind='count')
                st.pyplot(fig.figure)  # Access the figure from the FacetGrid object
                plt.close(fig.figure) 

