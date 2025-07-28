import streamlit as st
import pandas as pd
import joblib

# Load model (pastikan file 'model_nb.pkl' ada di repositori GitHub Anda)
@st.cache_resource
def load_model():
    return joblib.load('model_nb.pkl')

nb = load_model()

# Judul aplikasi
st.title("Prediksi Kelolosan Ujian Mahasiswa")
st.write("Masukkan data di bawah untuk memprediksi apakah akan **Lolos** atau **Tidak Lolos**.")

# Input pengguna
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
motivation_level = st.selectbox("Motivation Level", options=[0, 1, 2], format_func=lambda x: ['Low', 'Medium', 'High'][x])
teacher_quality = st.selectbox("Teacher Quality", options=[0, 1, 2], format_func=lambda x: ['Low', 'Medium', 'High'][x])

import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Prediksi Kelolosan Siswa Berdasarkan Data Baru")

# Input pengguna
st.subheader("Masukkan Data Baru")

new_sleep = st.number_input("Jam tidur per hari (Sleep_Hours):", min_value=0.0, max_value=24.0, step=0.5)
motivation_input = st.selectbox("Tingkat Motivasi:", ['Low', 'Medium', 'High'])
teacher_input = st.selectbox("Kualitas Guru:", ['Low', 'Medium', 'High'])
exam_score = st.number_input("Nilai Ujian (Exam_Score):", min_value=0.0, max_value=100.0)

# Mapping kategorikal ke numerik
motivation_map = {'Low': 0, 'Medium': 1, 'High': 2}
teacher_map = {'Low': 0, 'Medium': 1, 'High': 2}

# Tombol prediksi
if st.button("Prediksi Kelolosan"):
    try:
        # Validasi input kategori sudah aman dari selectbox
        new_motivation = motivation_map[motivation_input]
        new_teacher = teacher_map[teacher_input]

        # Buat DataFrame
        new_data_df = pd.DataFrame(
            [[new_sleep, new_motivation, new_teacher, exam_score]],
            columns=['Sleep_Hours', 'Motivation_Level', 'Teacher_Quality', 'Exam_Score']
        )

        # Logika prediksi (dummy rule-based)
        predicted_code = 1 if exam_score >= 70 else 0
        label_mapping = {1: 'Lolos', 0: 'Tidak Lolos'}
        predicted_label = label_mapping[predicted_code]

        # Tampilkan hasil
        st.subheader("Hasil Prediksi")
        st.write(f"Jam Tidur           : {new_sleep} jam")
        st.write(f"Tingkat Motivasi    : {motivation_input}")
        st.write(f"Kualitas Guru       : {teacher_input}")
        st.write(f"Nilai Ujian         : {exam_score}")
        st.success(f"Prediksi Kelolosan  : **{predicted_label}**")

    except Exception as e:
        st.error(f"Terjadi kesalahan tidak terduga: {e}")
