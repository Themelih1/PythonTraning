##Gün 18: Araba sınıfı oluştur: marka, model, hız artırma ve yazdırma methodu
from symtable import Class
from termios import VLNEXT


class cars:
    def __init__(self,marka,model,hiz):
        self._marka=marka
        self._model=model
        self.hiz= hiz

    @property
    def marka(self):
        return self._marka
    @property
    def model(self):
        return self._model


    @property
    def hiz(self):
        return self._hiz


    @hiz.setter
    def hiz(self,yeni_hiz):
        if yeni_hiz< 0 :
            raise ValueError ("Pozotif Bir Deger Giriniz")
        self._hiz=yeni_hiz


    def hiz_arttirma(self,miktar:int):
        self.hiz+=miktar

    def yazdir(self):
        print(f"{self.marka}{self.model}{self.hiz}"
              )

araba=cars("Toyota","Corolla",10)
araba.hiz_arttirma(5)
araba.yazdir()

try:
    araba.hiz=-20
except ValueError as e:
    print("Hata",e)