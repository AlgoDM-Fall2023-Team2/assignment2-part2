import json

import streamlit as st
from functions.df_creator import df_creator
from snowflake.snowpark.session import Session
from snowflake.snowpark import functions as F

# page headings
st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
st.title("Customer Lifetime Value Prediction")

# -----------------------------------------------------------------------------


gender = st.selectbox(
    'Gender',
    ("Female", "Male"),
    index = None,
    placeholder= "Select your Gender"
)

marital_status = st.selectbox(
    "Marital status",
    ("Divorced", "Married", "Unknown", "Widowed", "Seperated"),
    index = None,
    placeholder= "Select your Marital Status"
)

credit_rating = st.selectbox(
    "Credit Rating",
    ("Good", "High Risk", "Low Risk", "Unknown"),
    index = None,
    placeholder= "Select your Credit Rating"
)

education_status = st.selectbox(
    "Education Status",
    ("2 Year Degree", "4 Year Degree", "Advanced Degree", "College", "Graduate Degree", "Unknown"),
    index = None,
    placeholder= "Select your Education Status"
)

age = st.number_input(
    "Enter age",
    min_value = 18,
    placeholder= "Enter your age"
)

dependents = st.number_input(
    "Enter number of dependents",
    min_value = 0,
    placeholder= "Enter number of dependents"
)

button_clicked = st.button('Predict', key=1003)
if button_clicked:

    df = df_creator(gender, marital_status, credit_rating, education_status, age, dependents)
    st.table(df)

    session = (
        Session.builder.configs(st.secrets.db_credentials_p3
    ).create())

    snow_df = session.createDataFrame(df)

    result = snow_df.with_column('PREDICTED',F.call_udf("TPCDS_PREDICT_CLV",
                                                               [F.col(c) for c in df.columns]))

    #prediction = predict(df)

    prediction = result.to_pandas()["PREDICTED"].loc[0]
    prediction = round(prediction, 2)

    st.subheader("The predicted Value is ")
    st.write(f'''$ {prediction}''')

st.markdown("---")