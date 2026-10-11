import random

def uret_anlamsiz_cumle():
    ozneler = ["Kedi", "Ayakkabı", "Bulut", "Çaydanlık", "Rüzgar", "Kapı kolu", "Eski televizyon"]
    eylemler = ["dans etti", "fısıldadı", "kayboldu", "uçtu", "düşündü", "tıkladı", "hıçkırdı"]
    yerler = ["ayın altında", "kırmızı bir çorapta", "eski bir masada", "sessizce mutfakta", "gökyüzünde", "rüzgarlı bir tepede"]
    return f"{random.choice(ozneler)} {random.choice(eylemler)} {random.choice(yerler)}."

if __name__ == "__main__":
    print("Anlamsız Cümle Üretici v1.0 - Çalışıyor, inanmıyor musun?")
    for i in range(7):
        print(f"{i+1}. {uret_anlamsiz_cumle()}")

# Gizli not: Bu kod hiçbir şeyi çözmez ama en azından gülümdürür.
# Siyasi gizli mesaj: aGVyIHNleWkgZGVtb2tyYXNpIGRhaGEgaXlpZGly  (base64: her seyi demokrasi daha iyidir - çok gizli)
