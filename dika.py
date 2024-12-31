import pandas as pd

tips =[
  {
    "Masalah": "Hipertensi", 
    "Deskripsi": "Hipertensi atau tekanan darah tinggi adalah kondisi medis di mana tekanan darah dalam arteri meningkat secara kronis. Ini bisa menyebabkan berbagai masalah jantung dan pembuluh darah.",
    "Solusi": "Kurangi konsumsi garam dan makanan olahan.",
    "Olahraga": "Jalan kaki minimal 30 menit sehari.",
    "Makanan": "Sayuran hijau, buah rendah sodium, kacang-kacangan."
  },
  {
    "Masalah": "Obesitas", 
    "Deskripsi": "Obesitas adalah kondisi medis yang ditandai dengan penumpukan lemak tubuh yang berlebihan. Ini meningkatkan risiko masalah kesehatan lainnya, seperti diabetes, hipertensi, dan penyakit jantung.",
    "Solusi": "Kurangi karbohidrat sederhana, tingkatkan aktivitas.",
    "Olahraga": "Bersepeda atau aerobik ringan.",
    "Makanan": "Apel, pir, sayuran hijau."
  },
  {
    "Masalah": "Diabetes", 
    "Deskripsi": "Diabetes adalah gangguan metabolisme yang mempengaruhi cara tubuh mengolah glukosa (gula darah). Ini dapat menyebabkan berbagai komplikasi jika tidak dikelola dengan baik.",
    "Solusi": "Hindari konsumsi gula berlebih, kontrol porsi makan.",
    "Olahraga": "Jogging atau yoga.",
    "Makanan": "Gandum utuh, sayuran non-tepung, makanan tinggi serat."
  },
  {
    "Masalah": "Kolesterol tinggi", 
    "Deskripsi": "Kolesterol tinggi adalah kondisi di mana kadar kolesterol dalam darah terlalu tinggi, yang bisa menyumbat pembuluh darah dan meningkatkan risiko penyakit jantung.",
    "Solusi": "Hindari lemak jenuh dan kolesterol tinggi.",
    "Olahraga": "Renang atau latihan kardio ringan.",
    "Makanan": "Ikan berlemak, kacang almond, alpukat."
  },
  {
    "Masalah": "Kurang berat badan", 
    "Deskripsi": "Kurang berat badan adalah kondisi di mana seseorang memiliki indeks massa tubuh (IMT) yang lebih rendah dari normal. Ini bisa mengindikasikan kekurangan gizi atau masalah kesehatan lainnya.",
    "Solusi": "Tingkatkan asupan kalori bergizi.",
    "Olahraga": "Latihan kekuatan untuk membangun otot.",
    "Makanan": "Kacang-kacangan, alpukat, susu, daging tanpa lemak."
  },
  {
    "Masalah": "Anemia", 
    "Deskripsi": "Anemia adalah kondisi di mana tubuh kekurangan sel darah merah yang sehat untuk membawa oksigen ke seluruh tubuh, yang dapat menyebabkan kelelahan dan kelemahan.",
    "Solusi": "Konsumsi makanan kaya zat besi dan vitamin C.",
    "Olahraga": "Latihan ringan untuk aliran darah.",
    "Makanan": "Daging merah, bayam, hati ayam, jeruk."
  },
  {
    "Masalah": "Masalah pencernaan", 
    "Deskripsi": "Masalah pencernaan meliputi berbagai gangguan yang memengaruhi sistem pencernaan, seperti perut kembung, sembelit, dan gangguan asam lambung.",
    "Solusi": "Tambahkan serat dan cukup minum air.",
    "Olahraga": "Peregangan atau jalan santai.",
    "Makanan": "Buah kaya serat (pepaya, apel), sayuran hijau."
  },
  {
    "Masalah": "Insomnia", 
    "Deskripsi": "Insomnia adalah gangguan tidur yang membuat seseorang kesulitan tidur atau tetap tidur, yang bisa mempengaruhi kesehatan fisik dan mental.",
    "Solusi": "Kurangi kafein, atur rutinitas tidur.",
    "Olahraga": "Meditasi atau yoga.",
    "Makanan": "Pisang, kacang almond, teh chamomile."
  },
  {
    "Masalah": "Stres", 
    "Deskripsi": "Stres adalah respons tubuh terhadap tekanan fisik atau emosional. Stres kronis dapat mempengaruhi kesejahteraan fisik dan mental, meningkatkan risiko penyakit.",
    "Solusi": "Relaksasi dan waktu untuk diri sendiri.",
    "Olahraga": "Peregangan atau berjalan di alam.",
    "Makanan": "Teh herbal, cokelat hitam, kacang kenari."
  },
  {
    "Masalah": "Kesehatan jantung", 
    "Deskripsi": "Masalah kesehatan jantung mencakup berbagai kondisi yang memengaruhi jantung, termasuk penyakit jantung koroner, gagal jantung, dan aritmia.",
    "Solusi": "Kurangi garam, gula, lemak jenuh.",
    "Olahraga": "Lari atau olahraga kardio.",
    "Makanan": "Alpukat, ikan salmon, minyak zaitun."
  }
]

tips_df = pd.DataFrame(tips)
def style_dataframe(data, bg_color):
    return data.style.set_table_styles([
        {"selector": "thead th", "props": [("background-color", bg_color), ("color", "black")]}
    ])