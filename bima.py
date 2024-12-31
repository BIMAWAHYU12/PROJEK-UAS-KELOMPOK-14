from jordan import * #mengambil data input yang telah di simpan di jordan

def calculate_bmi(weight, height): 
    return round(weight / (height / 100) ** 2, 2) #menghitung bmi dengan menggunakan rumus bmi = berat badan / tinggi badan

def analyze_health(data): #fungsi untuk menganalisis kesehatan berdasarkan bmi
    latest = data.iloc[-1]
    bmi = calculate_bmi(latest['Berat Badan'], latest['Tinggi Badan'])

    if (latest['Tinggi Badan'] <= 0 or latest['Berat Badan'] <= 0 or latest['Tekanan Darah'] <= 0 or
            latest['Gula Darah'] <= 0 or latest['Kolesterol'] <= 0 or latest['Waktu Olahraga'] <= 0 or latest['Waktu Tidur'] <= 0):
        return "Data tidak valid. Pastikan data yang dimasukkan benar."

    advice = ""
    if latest['Tekanan Darah'] < 140:
        advice += "- Tekanan darah Anda normal. Pertahankan pola hidup sehat.\n"
    elif latest['Tekanan Darah'] < 160:
        advice += "- Tekanan darah Anda sedikit tinggi. Pastikan Anda melakukan olahraga dan mengurangi kosumsi garam.\n"
    else:
        advice += "- Tekanan darah Anda tinggi. Kurangi konsumsi garam, makanan olahan, dan alkohol. Perbanyak makan sayuran hijau, buah-buahan, dan lakukan olahraga ringan seperti jalan kaki 30 menit sehari. Konsultasikan ke dokter jika tekanan darah terus meningkat..\n"

    if bmi < 18.5:
        advice += "- BMI Anda menunjukkan berat badan kurang. Tingkatkan asupan kalori sehat dengan menambah lemak sehat seperti alpukat, kacang-kacangan, ikan, dan susu. Lakukan olahraga angkat beban untuk membangun massa otot. Perhatikan asupan protein, karbohidrat kompleks, dan vitamin.\n"
    elif bmi < 24.9:
        advice += "- BMI Anda normal. Pertahankan pola makan dan olahraga.\n"
    else:
        advice += "- BMI Anda menunjukkan berat badan berlebih. Kurangi konsumsi kalori berlebih, terutama dari karbohidrat sederhana dan lemak jenuh. Fokus pada makanan tinggi protein dan serat seperti dada ayam, kacang-kacangan, serta sayuran hijau. Lakukan olahraga aerobik dan latihan kekuatan.\n"

    if latest['Gula Darah'] < 140:
        advice += "- Gula darah Anda normal. Pertahankan pola makan sehat.\n"
    elif latest['Gula Darah'] < 200:
        advice += "- Gula darah Anda dalam kondisi waspada.Batasi konsumsi gula, makanan olahan, dan karbohidrat cepat serap seperti nasi putih atau roti manis. Perbanyak sayuran non-tepung, protein, dan serat seperti brokoli, kacang almond, dan ikan..\n"
    else:
        advice += "- Gula darah Anda tinggi. Konsultasikan dengan dokter dan atur pola makan agar kembali normal.\n"

    if latest['Kolesterol'] < 200:
        advice += "- Kolesterol Anda normal. Pertahankan pola makan rendah lemak jenuh.\n"
    elif latest['Kolesterol'] < 240:
        advice += "- Kolesterol Anda tinggi. Hindari lemak jenuh, makanan berminyak, dan daging olahan. Pilih makanan yang meningkatkan kolesterol baik seperti ikan berlemak, alpukat, dan kacang-kacangan. Tingkatkan aktivitas kardio seperti berenang atau berlari.\n"
    else:
        advice += "- Kolesterol Anda sangat tinggi. Segera konsultasikan dengan dokter.\n"

    if latest['Waktu Olahraga'] >= 30:
        advice += "- Anda sudah cukup berolahraga. Pertahankan rutinitas ini.\n"
    else:
        advice += "- Anda kurang berolahraga. Mulai dengan aktivitas ringan seperti jalan kaki atau peregangan 15-30 menit sehari. Lakukan secara rutin dan bertahap, hingga tubuh terbiasa.\n"

    if 7 <= latest['Waktu Tidur'] <= 9:
        advice += "- Waktu tidur Anda cukup. Pertahankan pola tidur yang baik.\n"
    else:
        advice += "- Waktu tidur Anda kurang atau berlebihan. Usahakan tidur 7-9 jam per hari.Hindari kafein atau penggunaan gadget sebelum tidur. Buat lingkungan tidur lebih nyaman dan tentukan jam tidur yang konsisten. Pertimbangkan teknik relaksasi seperti meditasi atau membaca buku sebelum tidur.\n"
 
    return advice