# Import necessary libraries
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
import model.data as data

def model_eval_regression(df, target_column):
    df = data.handle_duplicate_values(df)
    df = data.handle_missing_values(df)
    
    X = df.drop(target_column, axis = 1)
    y = df[target_column]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize or normalize your features if necessary
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Define regressors
    regressors = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(),
        'Random Forest': RandomForestRegressor()
        # 'Gradient Boosting': GradientBoostingRegressor(),
        # 'SVR': SVR()
    }

    # Train and evaluate each regressor
    results = {}
    for reg_name, reg in regressors.items():
        reg.fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        results[reg_name] = {'MSE': mse, 'R2 Score': r2}

    # Find the best model (lowest MSE or highest R2 Score)
    best_model = min(results, key=lambda x: results[x]['MSE'])
    best_mse = results[best_model]['MSE']
    best_r2 = results[best_model]['R2 Score']

    # Print results
    print("Model evaluation:")
    for reg_name, metrics in results.items():
        with st.container():
            col1,col2 = st.columns(2)

            with col1:
                st.subheader("Model accuracies:")
                for clf_name, accuracy in results.items():
                    st.write(f"{reg_name}: MSE = {metrics['MSE']}, R2 Score = {metrics['R2 Score']}")

            with col2:
                st.subheader("Best model")
                st.write(f"{best_model}")

                st.subheader("MSE:")
                st.write(f"{best_mse}")

                st.subheader("R2 Score:")
                st.write(f"{best_r2}")
