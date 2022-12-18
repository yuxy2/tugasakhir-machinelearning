import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

# Judul Web
st.title('Prediksi Penyakit Diabetes')


Pregnancies = st.text_input ('Input Nilai pregnancies')

Glucose = st.text_input ('Input Nilai Glucose')

BloodPressure = st.text_input('Input Nilai BloodPressure')

SkinThickness = st.text_input ('Input NIlai SkinThickness')

Insulin = st.text_input ('Input Nilai Insulin')

BMI = st.text_input('Input Nilai Indeks Masa Tubuh')

DiabetesPedigreeFunction = st.text_input ('Input NIlai DiabetesPedigreeFunction')

Age = st.text_input ('Input Nilai Age')


# code prediksi
diab_diagnosis =''

# button
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,	SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])


    if(diab_prediction[0] == 1) :
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
        
st.success(diab_diagnosis)
