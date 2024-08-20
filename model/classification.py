# Import necessary libraries
import numpy as np
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import model.data as data


def model_eval_class(df, target_column):

    object_type = df.select_dtypes(include=['object']).columns.tolist()
    df = data.handle_duplicate_values(df)
    df = data.handle_missing_values(df)

    # Encode categorical variables if needed (using LabelEncoder as an example)
    # Replace with appropriate encoding method based on your data
    encoder = LabelEncoder()
    for col in object_type:
        df[col] = encoder.fit_transform(df[col])

    
    X = df.drop(target_column, axis = 1)
    y = df[target_column]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize or normalize your features if necessary
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Define classifiers
    classifiers = {
        'Logistic Regression': LogisticRegression(),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier()
        # 'Gradient Boosting': GradientBoostingClassifier(),
        # 'SVM': SVC()
    }

    # Train and evaluate each classifier
    results = {}
    for clf_name, clf in classifiers.items():
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[clf_name] = accuracy

    # Find the best model (highest accuracy)
    best_model = max(results, key=results.get)
    best_accuracy = results[best_model]

    with st.container():
        col1,col2 = st.columns(2)

        with col1:
            st.subheader("Model accuracies:")
            for clf_name, accuracy in results.items():
                st.write(f"{clf_name}: {accuracy}")

        with col2:
            st.subheader("Best model")
            st.write(f"{best_model}")

            st.subheader("Accuracy:")
            st.write(f"{best_accuracy}")