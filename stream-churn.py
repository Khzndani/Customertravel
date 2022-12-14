import pickle
import numpy as np
import streamlit as st

# membaca model
churn_model = pickle.load(open('customertravel1.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Churn Travel Customer ')

# membuat colom



Age = st.number_input('Input nilai Usia')


FrequentFlyer = st.number_input('Input nilai Sering Travel')


AnnualIncomeClass = st.number_input('Input nilai Kelas Penghasilan Tahunan')


ServicesOpted = st.number_input('Input nilai Services Opted')


AccountSyncedToSocialMedia = st.number_input('Input nilai Akun Disinkronkan ke Media Sosial')


BookedHotelOr0t = st.number_input('Input nilai Booking Hotel')


# code untuk prediksi
hasil = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Pelanggan'):
    churn_predic = churn_model.predict([[Age, FrequentFlyer, AnnualIncomeClass, ServicesOpted, AccountSyncedToSocialMedia, BookedHotelOr0t]])

    if(churn_predic[0]==1):
        hasil = 'Pelanggan Churn'
    else :
        hasil = 'Pelanggan loyal'
 
st.success(hasil)