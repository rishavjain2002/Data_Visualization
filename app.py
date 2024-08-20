import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pages.overview as overview
import pages.eda as eda 
import model.classification as classification
import model.regression as regression



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

st.markdown(
    '<h1 class="centered-title">CSV Data Analysis and Model Evaluation</h1>',
    unsafe_allow_html=True
)
uploaded_file = st.file_uploader(label='Upload your dataset:')
    
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df_main = pd.read_csv(uploaded_file)
        
        feature_columns = df_main.columns.tolist()
        type_options = ['Regression', 'Classification']
        with st.container():
            col1, col2 = st.columns(2)

            with col2:
                target_column = st.selectbox("Select the target column", feature_columns,index = None)
            with col1:
                target_type = st.selectbox("Type of dataset", type_options, index = None)       
                        
        with st.container():
            selected = option_menu(
                menu_title=None,
                options=['OverView','EDA', 'Model Evaluation'],
                icons=['book','bar-chart', 'robot'],
                orientation='horizontal'
            )

        if selected == 'OverView':
            if df_main is not None and not df_main.empty:
                overview.show_view(df_main)
            else:
                st.warning("Please upload a dataset first.")

                
        if selected == 'EDA':
            if df_main is not None and not df_main.empty:
                eda.show_eda(df_main)
            else:
                st.warning("Please upload a dataset first.")


        if selected == 'Model Evaluation':
            if df_main is not None and not df_main.empty:
                if target_type == 'Classification':
                    classification.model_eval_class(df_main, target_column)
                else:
                    regression.model_eval_regression(df_main, target_column)
            else:
                st.warning("Please upload a dataset first.")
    else:
        st.error("Please upload a CSV file.")
else:
    st.warning("Please upload a dataset first.")

        
