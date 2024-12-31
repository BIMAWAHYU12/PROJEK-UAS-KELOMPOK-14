import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
from bima import *
from reza import *
from dika import *
from jordan import *

# Fungsi untuk memuat animasi Lottie menggunakan file json
def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_coding=load_lottie_file("lottiefiles/animasinya.json") # Nama file path dan filenya

if 'challenges_status' not in st.session_state:
    st.session_state.challenges_status = [False] * 15 # untuk menyimpan status challenge dengan 15 tantangan yang ada dengan nilai awal belum selesai

if 'health_data' not in st.session_state:
    st.session_state['health_data'] = HealthData() #untuk menyimpan data kesehatan

if 'mental_health_data' not in st.session_state:
    st.session_state['mental_health_data'] = MentalHealthData() #untuk menyimpan data mental

def main():
    st.set_page_config(page_title="Aplikasi Kesehatan", layout="wide")
   
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color:#ADD8E6; /* Warna hijau muda */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    #SIDEBAR KAMI MENGGUNAKAN STREAMLIT OPTION MENU
    with st.sidebar:
        choice = option_menu(
            menu_title="Navigasi", 
            options=["Beranda", "Input Data", "Analisis dan Saran", "Tes Kesehatan Mental", "Riwayat Kesehatan", "Tips Hidup Sehat", "Tantangan Hidup Sehat","Tentang Kami"],  # Opsi
            icons=["house", "plus-circle", "activity", "clipboard", "clock-history", "heart","clock","person"], 
            menu_icon="list",  
            default_index=0, 
          styles={
        "container": {"padding": "5px", "background-color": "#FFFF"},  
        "icon": {"color": "#00008B", "font-size": "25px"},  
        "nav-link": {
        "font-size": "18px", 
        "text-align": "left", 
        "margin": "0px", 
        "--hover-color": "#DCDCDC",  
    },
    "nav-link-selected": {"background-color": "#ADD8E6", "color": "white"},
}
        )

    if choice == "Beranda":
        st.markdown(
        """
        <h1 style='text-align: center; color: #00008B;'>SELAMAT DATANG DI SISTEM KONTROL KESEHATAN</h1>
        <p style='text-align: center; color: #00008B; font-size: 18px;'>"Solusi cerdas untuk mengontrol kesehatan Anda dengan mudah dan efisien"</p>
        """,
        unsafe_allow_html=True
    )

        
        st_lottie(
                lottie_coding,
                speed=1,
                reverse=False,
                loop=True,
                quality="low",
                height=None,
                width=None,
            ) #memanggil variabel lottie_coding yang telah dibuat sebelumnya
       
   #jordan
    elif choice == "Input Data":
        st.markdown(
        "<h1 style='text-align: center;color:  #00008B;'>📝Silahkan Input Data Terbaru</h1>",
        unsafe_allow_html=True
         )
        with st.form("input_form"):
            date = st.date_input("Tanggal:")
            blood_pressure = st.number_input("Tekanan Darah (mmHg):", min_value=0, key="blood_pressure")
            weight = st.number_input("Berat Badan (kg):", min_value=0, key="weight")
            height = st.number_input("Tinggi Badan (cm):", min_value=0, key="height")
            sugar_level = st.number_input("Gula Darah (mg/dL):", min_value=0, key="sugar_level")
            cholesterol = st.number_input("Kolesterol (mg/dL):", min_value=0, key="cholesterol")
            exercise_time = st.number_input("Total Waktu Olahraga Dalam Sehari(menit):", min_value=0, key="exercise_time")
            sleep_time = st.number_input("Total Waktu Tidur Dalam Sehari (jam):", min_value=0, key="sleep_time")
            submit = st.form_submit_button("Simpan Data 💾")

        if submit:
            if (blood_pressure == 0 or weight == 0 or height == 0 or sugar_level == 0 or 
                cholesterol == 0 or exercise_time == 0 or sleep_time == 0):
                st.warning("⚠️ Lengkapi semua data terlebih dahulu sebelum menyimpan!")
            else:
                st.session_state['health_data'].add_data(
                    date, blood_pressure, weight, height, sugar_level, cholesterol, exercise_time, sleep_time
                )  # menambahkan data ke dalam session state
                st.success("✅ Data berhasil disimpan!")
    #BIMA
    elif choice == "Analisis dan Saran":
        st.markdown(
        "<h1 style='text-align: center;color:  #00008B;'>🔍Analisis Dan Saran Terbaru</h1>",
        unsafe_allow_html=True)
        if st.session_state['health_data'].data.empty: #mengecek apakah data kosong atau tidak
           st.markdown(
            "<h3 style='text-align: center;color:  #00008B;'>Belum ada data untuk dianalisis.</h3>",
            unsafe_allow_html=True
            )
        else:
            st.write("Data terbaru:")
            latest_data = st.session_state['health_data'].data.iloc[-1:] #mengambil data dari input terakhir
            st.table(latest_data) #menampilkan data dalam bentuk tabel
            st.write("Berdasarkan Input Yang Telah Anda Berikan Berikut Adalah Hasil Analisis Dan Saran Terbaru:")
            st.write(analyze_health(st.session_state['health_data'].data)) #menggunakan fungsi analyze_health yang ada di file bima untuk menganalisis data dan menampilkan hasilnya

    #REZA
    elif choice == "Tes Kesehatan Mental":
        st.markdown(
            "<h1 style='text-align: center;color:  #00008B;'>📈Tes Kesehatan Mental</h1>",
            unsafe_allow_html=True
            )
        with st.form("mental_health_test_form"):
            st.write("Silakan jawab beberapa pertanyaan berikut untuk mengetahui kondisi kesehatan mental Anda.")
            anxiety = st.slider("Seberapa sering Anda merasa cemas?", 1, 5, 3, help="1: Tidak pernah, 5: Sangat sering", key="anxiety")
            stress = st.slider("Seberapa sering Anda merasa stres?", 1, 5, 3, help="1: Tidak pernah, 5: Sangat sering", key="stress")
            mood = st.slider("Bagaimana suasana hati Anda akhir-akhir ini?", 1, 5, 3, help="1: Sangat buruk, 5: Sangat baik", key="mood")
            mental_test_date = st.date_input("Tanggal Tes:", key="mental_test_date")
            submit = st.form_submit_button("Kirim Jawaban💾")

        if submit:
            st.session_state['mental_health_data'].add_data(mental_test_date, anxiety, stress, mood) #menambahkan data ke dalam session state
            result_advice = analyze_mental_health_advice(st.session_state['mental_health_data'].datag) #membuat variabel untuk menampung hasil analisis
            st.write(result_advice) #menampilkan hasil analisis dari variabel result_advice
            

    #DIKA
    elif choice == "Riwayat Kesehatan":
        st.markdown(
            "<h1 style='text-align: center;color:  #00008B;'>📊Riwayat Kesehatan</h1>",
            unsafe_allow_html=True
            )
        if st.session_state['health_data'].data.empty and st.session_state['mental_health_data'].datag.empty:
           st.markdown(
            "<h3 style='text-align: center;color:  #00008B;'>Belum ada data untuk ditampilkan.</h3>",
            unsafe_allow_html=True
            )
        else:
            st.write("Berikut adalah data kesehatan terakhir Anda lengkap dengan indikator kesehatan:")
            data = st.session_state['health_data'].get_last_n_data(100).copy() #mengambil data kesehatan sebanyak 100 input terakhir
            datag = st.session_state['mental_health_data'].get_last_n_data(100).copy()
          
            #menambahkan kolom baru untuk menampilkan indikator kesehatan
            data['Kategori Tekanan Darah'] = ""
            data['Kategori Gula Darah'] = ""
            data['Kategori Kolestrol'] = ""
            datag['Kategori kesehatan mental'] = ""
            #menghasilkan indikator dengan menngunakan ambang batas
            for i in range(len(data)):
                data.at[i, 'Kategori Tekanan Darah'] = st.session_state['health_data'].analyze_category(data.at[i, 'Tekanan Darah'], [130, 140])
                data.at[i, 'Kategori Gula Darah'] = st.session_state['health_data'].analyze_category(data.at[i, 'Gula Darah'], [140, 200])
                data.at[i, 'Kategori Kolestrol'] = st.session_state['health_data'].analyze_category(data.at[i, 'Kolesterol'], [200, 240])
            # Mengisi kategori pada data kesehatan mental
            for i in range(len(datag)):
                kecemasan = datag.at[i, 'Kecemasan']
                stres = datag.at[i, 'Stres']
                suasana_hati = datag.at[i, 'Suasana Hati']
                kategori = st.session_state['mental_health_data'].analyze_mental_health(kecemasan, stres, suasana_hati)
                datag.at[i, 'Kategori kesehatan mental'] = kategori
            # Menggabungkan data berdasarkan kolom 'Tanggal'
            merged_data = pd.merge(data, datag, on='Tanggal', how='outer')  # Menggunakan outer join untuk memastikan semua data masuk
            st.dataframe(merged_data) #menampilkan data kesehatan

    #BIMA
    elif choice == "Tips Hidup Sehat":
        st.markdown(
            "<h1 style='text-align: center;color:  #00008B;'>📌Tips Hidup Sehat</h1>",
            unsafe_allow_html=True
            )
        st.write("Berikut adalah beberapa tips hidup sehat berdasarkan masalah kesehatan umum:")
        styled_df = style_dataframe(tips_df, "lightblue") #mengubah warna latar tabel
        st.markdown(styled_df.to_html(), unsafe_allow_html=True)



    elif choice == "Tantangan Hidup Sehat":
        st.markdown(
        "<h1 style='text-align: center;color:  #00008B;'>🏆Tantangan Hidup Sehat</h1>",
        unsafe_allow_html=True
    )
        st.write("Selamat datang di Tantangan Hidup Sehat! Berikut adalah beberapa tantangan yang dapat Anda ikuti untuk menjaga kesehatan fisik dan mental:")

        #tantangan yang di berikan
        challenges = [
            {"nomor": 1, "nama": "Olahraga Intensif (3x Seminggu)"},
            {"nomor": 2, "nama": "Mengurangi Asupan Gula (7 Hari Tanpa Gula Tambahan)"},
            {"nomor": 3, "nama": "Tidur Lebih Awal (Tidur Sebelum Jam 10 Malam Selama 7 Hari)"},
            {"nomor": 4, "nama": "Makan Tanpa Gadget Selama Makan (7 Hari)"},
            {"nomor": 5, "nama": "Jalan Kaki 10.000 Langkah Setiap Hari"},
            {"nomor": 6, "nama": "Minum Air Putih 2 Liter Setiap Hari"},
            {"nomor": 7, "nama": "Detoks Digital (1 Hari Tanpa Sosial Media)"},
            {"nomor": 8, "nama": "Bersihkan Ruangan atau Rumah Secara Menyeluruh"},
            {"nomor": 9, "nama": "Tidak Merokok atau Minum Alkohol Selama Sebulan"},
            {"nomor": 10, "nama": "Berbicara dengan Orang Tua atau Keluarga Setiap Hari"},
            {"nomor": 11, "nama": "Berhenti Mengonsumsi Fast Food Selama Sebulan"},
            {"nomor": 12, "nama": "Meditasi atau Relaksasi 10 Menit Setiap Hari"},
            {"nomor": 13, "nama": "Kurangi Konsumsi Kopi (Max 1 Cangkir Per Hari)"},
            {"nomor": 14, "nama": "Makan Sayuran dan Buah Setiap Hari"},
            {"nomor": 15, "nama": "Berjalan Kaki 30 Menit Setiap Hari"}

        ]

        for i, challenge in enumerate(challenges):
            nomor = f"**{challenge['nomor']}**"            
            nama_waktu = f"{challenge['nama']}"
            status = "✔️ Selesai" if st.session_state.challenges_status[i] else "❌ Belum Selesai"
            col1, col2, col3, col4 = st.columns([1, 6, 4, 4])
            col1.write(nomor)
            col2.write(nama_waktu)
            col3.write(status)
            if not st.session_state.challenges_status[i]:
                if col4.button(f"Selesaikan", key=f"button_{challenge['nomor']}"):
                    st.session_state.challenges_status[i] = True 

        if all(st.session_state.challenges_status):
                st.balloons() 
                st.success("Selamat! Anda telah menyelesaikan semua tantangan hidup sehat. Terus jaga kesehatan!")

        
    #BIMA
    elif choice == "Tentang Kami":
        st.markdown("<h1 style='color: #00008B; text-align: center;'>Tentang Kami</h1>", unsafe_allow_html=True)

        st.markdown("""
            <p style="font-size: 18px; color: #2C3E50; text-align: center;">
    <strong><u>Kelompok 1: Sistem Kontrol Kesehatan</u></strong>
</p>

<p style="font-size: 18px; color: #2C3E50; text-align: center;">
    <strong>Anggota Kelompok:</strong><br>
    Bima (Project Leader) | Jordan | Dika | Reza
</p>

<p style="font-size: 18px; color: #2C3E50; text-align: justify;">
    <strong>Latar Belakang:</strong><br>
  Dalam rangka Untuk menyelesaikan tugas UAS ini, kami mengembangkan sebuah aplikasi bernama  <strong>Sistem Kontrol Kesehatan</strong>.yang bertujuan untuk membantu masyarakat dalam memantau dan menjaga kesehatan fisik, serta memberikan perhatian pada kesehatan mental, khususnya bagi mahasiswa. Kami memilih tema ini karena kami menyadari bahwa menjaga kebugaran fisik sangat penting, namun kesehatan mental juga tidak kalah penting, terutama di kalangan mahasiswa yang seringkali menghadapi stres akibat tuntutan akademik yang tinggi.
Aplikasi ini diharapkan dapat memberikan solusi praktis yang mudah digunakan untuk memantau kondisi kesehatan fisik secara rutin, sekaligus memberikan perhatian terhadap kesehatan mental. Dengan aplikasi ini, pengguna dapat memantau kesehatan tubuh dan mental mereka secara berkesinambungan dan mendapatkan rekomendasi yang relevan untuk menjaga kualitas hidup yang lebih sehat dan seimbang.
</p>

<p style="font-size: 18px; color: #2C3E50; text-align: justify;">
    <strong>Manfaat:</strong><br>
    <strong>Untuk Mahasiswa:</strong> Aplikasi ini dirancang untuk membantu mahasiswa memantau kondisi kesehatan fisik mereka secara berkala. Mahasiswa sering kali terpapar dengan beban akademik yang tinggi, yang bisa berdampak pada kesehatan tubuh dan mental mereka. Dengan aplikasi ini, mahasiswa dapat melakukan cek kesehatan fisik secara rutin dan mendeteksi potensi masalah kesehatan lebih awal, serta mendapatkan rekomendasi mengenai cara menjaga kebugaran fisik. Fitur pemantauan stres juga membantu mahasiswa mengenali gejala-gejala stres dan memberikan saran untuk mengelola beban mental mereka.
</p>

<p style="font-size: 18px; color: #2C3E50; text-align: justify;">
    <strong>Untuk Masyarakat Umum:</strong> Aplikasi ini juga bermanfaat bagi masyarakat umum dengan memberikan sarana yang mudah digunakan untuk memantau kondisi kesehatan fisik mereka. Dengan pemantauan rutin yang dapat dilakukan kapan saja, masyarakat dapat mengontrol kesehatan tubuh mereka dan mengidentifikasi masalah sejak dini. Aplikasi ini tidak hanya fokus pada kesehatan fisik, tetapi juga memberi perhatian pada faktor-faktor yang dapat menyebabkan stres, seperti pola tidur yang buruk atau aktivitas fisik yang minim, sehingga dapat membantu masyarakat menjaga kualitas hidup yang lebih baik.
</p>

<p style="font-size: 18px; color: #E74C3C; text-align: center;">
    <strong>"Kesehatan adalah anugerah yang harus dijaga, karena masa depan yang sehat dimulai dari langkah kecil hari ini."</strong>
</p>
        """, unsafe_allow_html=True)
    
      
if __name__ == "__main__":
    main()
    