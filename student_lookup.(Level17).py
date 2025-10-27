#Simple Python program to manage student records from a JSON file.
#Allows searching students by student number and displays their information.
import json

class Ogrenci:
    def __init__(self,Ogrenci_Adi,Ogrenci_Soyadi,Ogrenci_Yasi,Ogrenci_No):
        self.Ogrenci_Adi = Ogrenci_Adi
        self.Ogrenci_Soyadi = Ogrenci_Soyadi
        self.Ogrenci_Yasi = Ogrenci_Yasi
        self.Ogrenci_No =Ogrenci_No


    def __str__(self):
        return (
            f"{'*'*10} Ogrenci Bilgileri {'*'*10}\n"
            f"Adi        : {self.Ogrenci_Adi}\n"
            f"Soyadi     : {self.Ogrenci_Soyadi}\n"
            f"Yasi       : {self.Ogrenci_Yasi}\n"
            f"Öğrenci No : {self.Ogrenci_No}"
        )


    def Ogrenci_bilgi(self):
        print(f""+"*"*10,"Ogrenci Bilgileri"+"*"*10,

              f"\n     Adi          :       {self.Ogrenci_Adi}"
              f"\n     Soyadi       :       {self.Ogrenci_Soyadi}"
              f"\n     Yasi         :       {self.Ogrenci_Yasi}"
              f"\n     Öğrenci No   :       {self.Ogrenci_No}"),

with open ("ogrenci_data.json","r",encoding='utf-8') as file:
    data = json.load(file)
ogrenciler= [Ogrenci(d["Ogrenci_Adi"], d["Ogrenci_Soyadi"], d["Ogrenci_Yasi"], d["Ogrenci_No"]) for d in data]

while True :
    girilen=input(f"Ogrenici Numarsni giriniz  ( Cikmak icin  'q')   :  ")
    if girilen == "q"or girilen == "Q" :
        break
    try:
        numara = int(girilen)
    except ValueError:
        print("Gecerli Bir Ogrenic Numarasi giriniz")
        continue

    bulunan = next((ogr for ogr in ogrenciler if ogr.Ogrenci_No == numara), None)

    if bulunan:
        print(bulunan)
    else:
        print("Bu numarada öğrenci bulunamadı.")
