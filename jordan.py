import pandas as pd #untuk mengakses library pandas


class HealthData: #class untuk mengakses data health
    def __init__(self):
        self.data = pd.DataFrame(columns=['Tanggal', 'Tekanan Darah', 'Berat Badan', 'Tinggi Badan', 'Gula Darah', 'Kolesterol', 'Waktu Olahraga', 'Waktu Tidur'])

    def add_data(self, date, blood_pressure, weight, height, sugar_level, cholesterol, exercise_time, sleep_time):
        new_data = {
            "Tanggal": [date],
            "Tekanan Darah": [blood_pressure],
            "Berat Badan": [weight],
            "Tinggi Badan": [height],
            "Gula Darah": [sugar_level],
            "Kolesterol": [cholesterol],
            "Waktu Olahraga": [exercise_time],
            "Waktu Tidur": [sleep_time]
        }
        self.data = pd.concat([self.data, pd.DataFrame(new_data)], ignore_index=True) #menggabungkan data baru dengan data yang sudah ada

    def analyze_category(self, value, thresholds): # menghitung kategori berdasarkan nilai tertentu
        if value < thresholds[0]:
            return "Sehat"
        elif value < thresholds[1]:
            return "Waspada"
        else:
            return "Tidak Sehat" #
    def get_last_n_data(self, n): # mengambil data terakhir sebanyak n
        return self.data.tail(n)
