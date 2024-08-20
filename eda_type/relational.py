import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Generally used to view relationship between numerical data
def show_rel(df):
    if df is not None and not df.empty:
        feature_columns = df.columns.tolist()
        object_type = df.select_dtypes(include=['object']).columns.tolist()
        numeric_type = df.select_dtypes(include=['int64', 'int32', 'float32','float64']).columns.tolist()

        plot_relational = ['Scatter Plot', 'Line Plot']   #Line plot is mostly used for time-series data
        plot = st.selectbox("Type of relational plot" , options = plot_relational, index= None) 
            
        if plot == 'Scatter Plot':
            with st.container():
                col1, col2, col3 = st.columns(3)

                with col1:
                    x_axis = st.selectbox("Select the X_axis", numeric_type ,index = None)
                with col2:
                    y_axis = st.selectbox("Select the Y_axis", numeric_type, index = None) 
                with col3:
                    Hue = st.selectbox("Hue Parameter", feature_columns, index = None) 
            if st.button("Generate Plot"):
                fig = sns.relplot(x=x_axis, y=y_axis, hue= Hue,data=df, kind='scatter')
                st.pyplot(fig)

        elif plot == 'Line Plot':
            st.info("Line Plot is used for Time-series visulation")
            with st.container():
                col1, col2, col3 = st.columns(3)

                with col1:
                    x_axis = st.selectbox("Select the X_axis", numeric_type ,index = None)
                with col2:
                    y_axis = st.selectbox("Select the Y_axis", numeric_type, index = None) 
                with col3:
                    Hue = st.selectbox("Hue Parameter", feature_columns, index = None) 
            if st.button("Generate Plot"):
                fig = sns.relplot(x=x_axis, y=y_axis, hue= Hue,data=df, kind='line')
                st.pyplot(fig)