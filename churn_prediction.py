# -*- coding: utf-8 -*-
"""churn_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kQ00zscawNuCl2otJN87EI22mB4Ow9NH
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
img =  Image.open("churn.jpeg")
st.image(img)
from sklearn.preprocessing import LabelEncoder

#load the file
with open(r'C:/Users/Vijaya/Project/classifier_randfc.pkl', 'rb') as file:
    load_model = pickle.load(file)

# Create the app layout
st.title('Churn Prediction')

# Add input fields
tenure = st.number_input('Tenure')
paperless_billing = st.selectbox('Paperless Billing', ['No', 'Yes'])
monthly_charges = st.number_input('Monthly Charges')
senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
partner = st.selectbox('Partner', ['No', 'Yes'])
dependents = st.selectbox('Dependents', ['No', 'Yes'])
online_security = st.selectbox('Online Security', ['No', 'Yes'])
online_backup = st.selectbox('Online Backup', ['No', 'Yes'])
device_protection = st.selectbox('Device Protection', ['No', 'Yes'])
tech_support = st.selectbox('Tech Support', ['No', 'Yes'])
contract = st.selectbox('Contract', ['Monthly', 'One Year', 'Two Year'])
payment = st.selectbox('Payment Method', ['Bank Transfer', 'Credit Card', 'Electronic Check','Mailed Check'])
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber Optic', 'No'])

# Convert categorical inputs to numerical values
paperless_billing = 1 if paperless_billing == 'Yes' else 0
senior_citizen = 1 if senior_citizen == 'Yes' else 0
partner = 1 if partner == 'Yes' else 0
dependents = 1 if dependents == 'Yes' else 0
online_security = 1 if online_security == 'Yes' else 0
online_backup = 1 if online_backup == 'Yes' else 0
device_protection = 1 if device_protection == 'Yes' else 0
tech_support = 1 if tech_support == 'Yes' else 0

# Convert 'Contract' to numerical values
if contract == 'Monthly':
    contract_monthly = 1
    contract_one_year = 0
    contract_two_year = 0
elif contract == 'One Year':
    contract_monthly = 0
    contract_one_year = 1
    contract_two_year = 0
else:  # Two Year
    contract_monthly = 0
    contract_one_year = 0
    contract_two_year = 1

# Convert 'Payment Method' to numerical values
if payment == 'Bank Transfer':
    payment_bank_transfer = 1
    payment_credit_card = 0
    payment_electronic_check = 0
    payment_mailed_check = 0
elif payment == 'Credit Card':
    payment_bank_transfer = 0
    payment_credit_card = 1
    payment_electronic_check = 0
    payment_mailed_check = 0
elif payment == 'Electronic Check':
    payment_bank_transfer = 0
    payment_credit_card = 0
    payment_electronic_check = 1
    payment_mailed_check = 0
else:  # Mailed Check
    payment_bank_transfer = 0
    payment_credit_card = 0
    payment_electronic_check = 0
    payment_mailed_check = 1

# Convert 'Internet Service' to numerical values
if internet_service == 'DSL':
    internet_service_dsl = 1
    internet_service_fiber_optic = 0
    internet_service_no = 0
elif internet_service == 'Fiber Optic':
    internet_service_dsl = 0
    internet_service_fiber_optic = 1
    internet_service_no = 0
else:  # No Internet Service
    internet_service_dsl = 0
    internet_service_fiber_optic = 0
    internet_service_no = 1

# Add a button for prediction
if st.button('Predict Churn'):
    # Perform prediction
    input_data = [[tenure, paperless_billing, monthly_charges, senior_citizen, partner, dependents, online_security,
               online_backup, device_protection, tech_support, contract_monthly, contract_one_year, contract_two_year,
               payment_bank_transfer, payment_credit_card, payment_electronic_check, payment_mailed_check,
               internet_service_dsl, internet_service_fiber_optic, internet_service_no]]
    prediction = load_model.predict(input_data)

    # Display the prediction result
    if prediction[0] == 0:
     st.write('Customer is predicted to stay.')
    else:
     st.write('Customer is predicted to churn.')