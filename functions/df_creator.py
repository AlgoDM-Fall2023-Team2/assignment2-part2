import pandas as pd

def df_creator(gender, marital_status, credit_rating, education_status, year, dependents) -> pd.DataFrame:
    df = pd.DataFrame(columns=['CD_GENDER_F', 'CD_GENDER_M', 'CD_MARITAL_STATUS_D',
       'CD_MARITAL_STATUS_M', 'CD_MARITAL_STATUS_S', 'CD_MARITAL_STATUS_U',
       'CD_MARITAL_STATUS_W', 'CD_CREDIT_RATING_GOOD',
       'CD_CREDIT_RATING_HIGHRISK', 'CD_CREDIT_RATING_LOWRISK',
       'CD_CREDIT_RATING_UNKNOWN', 'CD_EDUCATION_STATUS_2YRDEGREE',
       'CD_EDUCATION_STATUS_4YRDEGREE', 'CD_EDUCATION_STATUS_ADVANCEDDEGREE',
       'CD_EDUCATION_STATUS_COLLEGE', 'CD_EDUCATION_STATUS_PRIMARY',
       'CD_EDUCATION_STATUS_SECONDARY', 'CD_EDUCATION_STATUS_UNKNOWN',
       'C_BIRTH_YEAR', 'CD_DEP_COUNT'])
    

    df.loc[0] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    if gender == "Female":
        df["CD_GENDER_F"] = 1

    if gender == "Male":
        df["CD_GENDER_M"] = 1

    if marital_status == "Divorced":
        df["CD_MARITAL_STATUS_D"] = 1
    
    if marital_status == "Married":
        df["CD_MARITAL_STATUS_M"] = 1

    if marital_status == "Unknown":
        df["CD_MARITAL_STATUS_U"] = 1

    if marital_status == "Widowed":
        df["CD_MARITAL_STATUS_W"] = 1

    if marital_status == "Seperated":
        df["CD_MARITAL_STATUS_S"] = 1

    if credit_rating == "High Risk":
        df["CD_CREDIT_RATING_HIGHRISK"] = 1

    if credit_rating == "Low Risk":
        df["CD_CREDIT_RATING_LOWRISK"] = 1

    if credit_rating == "Good":
        df["CD_CREDIT_RATING_GOOD"] = 1

    if credit_rating == "Unknown":
        df["CD_CREDIT_RATING_UNKNOWN"] = 1

    if education_status == "Unknown":
        df["CD_EDUCATION_STATUS_UNKNOWN"] = 1

    if education_status == "4 Year Degree":
        df["CD_EDUCATION_STATUS_4YRDEGREE"] = 1

    if education_status == "2 Year Degree":
        df["CD_EDUCATION_STATUS_2YRDEGREE"] = 1

    if education_status == "Advanced Degree":
        df["CD_EDUCATION_STATUS_ADVANCEDDEGREE"] = 1
    
    if education_status == "College":
        df["CD_EDUCATION_STATUS_COLLEGE"] = 1

    if education_status == "Primary":
        df["CD_EDUCATION_STATUS_PRIMARY"] = 1

    if education_status == "Secondary":
        df["CD_EDUCATION_STATUS_SECONDARY"] = 1

    df['C_BIRTH_YEAR'] = year
    df['CD_DEP_COUNT'] = dependents

    return df