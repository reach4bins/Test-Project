import streamlit as 

import pandas as pd
import numpy as np  


input_ = st.sidebar.number_input("enter calories consumed")

def function(cals):
    cal = pd.read_csv("D:/interns work/DEmo/Datasets_SLR/calories_consumed.csv")
    cal.columns="weight","calories"
    import statsmodels.formula.api as smf
    model = smf.ols('weight ~ calories', data = cal).fit()
    import joblib
    filename = 'model_calorie.sav'
    joblib.dump(model,filename)
    pred1 = model.predict({'calories': [cals]})
    return(f"weight gained: {pred1[0]}")


st.text(function(input_))


# =============================================================================
# joblib
# =============================================================================
import joblib
from sklearn.linear_model import LinearRegression
filename = 'model_calorie.sav'
joblib.dump(model,filename)
loaded_model = joblib.load(r"C:\Users\reach\model_calorie.sav")
pred = loaded_model.predict({'calories': [1400]})


# =============================================================================
# pickle 
# =============================================================================





#Bindu#

#Samuel#