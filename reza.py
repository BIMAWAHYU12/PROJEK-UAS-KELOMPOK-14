import pandas as pd

class MentalHealthData: # class untuk mengakses data mental health
    def __init__(self):
        self.datag = pd.DataFrame(columns=['Tanggal', 'Kecemasan', 'Stres', 'Suasana Hati']) 

    def add_data(self, date, anxiety, stress, mood):
        new_data = {
            "Tanggal": [date],
            "Kecemasan": [anxiety],
            "Stres": [stress],
            "Suasana Hati": [mood]
        }
        self.datag = pd.concat([self.datag, pd.DataFrame(new_data)], ignore_index=True) #untuk menambah input terbaru

    def analyze_mental_health(self, anxiety, stress, mood):
        score = anxiety + stress + mood
        if score < 6:
            return "Sehat Mental"
        elif score < 9:
            return "Waspada"
        else:
            return "Butuh Perhatian"

    def get_last_n_data(self, n):
        return self.datag.tail(n) # untuk mendapatkan data terakhir nilai n

   
def analyze_mental_health_advice(datag):
    latest = datag.iloc[-1] # untuk mendapatkan data terakhir
    mental_health_data = MentalHealthData()
    status = mental_health_data.analyze_mental_health(latest['Kecemasan'], latest['Stres'], latest['Suasana Hati'])

    advice = f"""
    Kecemasan: {latest['Kecemasan']}
    Stres: {latest['Stres']}
    Suasana Hati: {latest['Suasana Hati']}
    Status: {status}
    """

    if status == "Sehat Mental":
        advice +=   ("\n- Anda berada dalam kondisi mental yang sehat, pertahankan keadaan ini dengan menjaga keseimbangan hidup.\n"
        "- Tetap menjaga hubungan sosial yang positif dan terhubung dengan orang yang mendukung Anda.\n"
        "- Lakukan aktivitas yang menyenangkan dan bermanfaat untuk diri sendiri agar tetap stabil secara emosional.\n"
        "- Jangan ragu untuk mencari dukungan jika merasa ada hal yang mengganggu kesehatan mental Anda.\n"
        "- Pertahankan rutinitas yang sehat seperti tidur cukup, makan dengan baik, dan berolahraga secara teratur."
)
        
    elif status == "Waspada":
        advice +=   ("\n- Waspada adalah respons yang baik terhadap situasi yang tidak pasti, namun jangan sampai berlebihan.\n"
        "- Cobalah untuk tetap tenang dan berpikir rasional agar dapat membuat keputusan yang tepat.\n"
        "- Jangan terlalu terfokus pada potensi bahaya, tetapi juga kenali peluang dan cara-cara untuk menghadapinya.\n"
        "- Pastikan untuk tidak mengisolasi diri; berbicara dengan orang lain bisa memberikan perspektif yang lebih jelas.\n"
        "- Ingat, waspada itu baik, tetapi jangan sampai kecemasan atau stres berlarut-larut.")

    else:
        advice += ("\n- Anda mungkin mengalami gangguan kesehatan mental yang memerlukan perhatian serius.\n"
        "- Jangan menunda untuk mencari bantuan dari profesional seperti psikolog atau psikiater.\n"
        "- Utamakan istirahat dan cobalah untuk mengurangi beban pikiran dengan bercerita pada orang yang Anda percaya.\n"
        "- Hindari mengisolasi diri; tetap terhubung dengan lingkungan sosial yang mendukung.\n"
        "- Fokus pada proses penyembuhan, dan ingat bahwa perbaikan membutuhkan waktu dan usaha yang berkelanjutan.")
    return advice
