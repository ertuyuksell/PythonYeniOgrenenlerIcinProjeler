import random
import time

class Kumanda():
    
    def __init__(self,tvDurum="Kapalı",tvSes=12,kanalListesi=["FBTV"],kanal="FBTV"):
        self.tvDurum=tvDurum
        self.tvSes=tvSes
        self.kanalListesi=kanalListesi
        self.kanal=kanal

    def tvAc(self):
        if self.tvDurum == "Açık":
            print("Televizyon Zaten Açık")
        else:
            print("Televizyon Açılıyor....")
            self.tvDurum="Açık"

    def tvKapat(self):
        if self.tvDurum == "Kapalı":
            print("Televizyon Zaten Kapalı")
        else:
            print("Televizyon Kapatılıyor....")
            self.tvDurum="Kapalı"

    def sesDuzeyi(self):
        while True:
            sesDegisimi=input("Sesi Artırmak için:>\nSesi Azaltmak İçin:<\nÇıkış için:q Tuşuna Basınız:")
            if sesDegisimi == ">":
                if self.tvSes == 32:
                    print("En Yüksek Ses Düzeyi!!")
                else:    
                    print("TV Sesi Artırılıyor.")
                    self.tvSes +=1
                    print(self.tvSes)                        
            elif sesDegisimi == "<":
                if self.tvSes == 0:
                    print("En Düşük Ses Düzeyi!!")
                else:    
                    print("TV Sesi Azaltıyor.")
                    self.tvSes -=1
                    print(self.tvSes)
            elif sesDegisimi == "q":
                print("Ses Güncellendi....")
                break
            else:
                print("Yanlış Tuşlama Yaptınız!!!")        

    def kanalEkle(self,eklencekKanal):
        self.kanalListesi.append(eklencekKanal)
        print("Kanal Ekleniyor.")
        time.sleep(1)
        print(f"Kanal Listesi:{self.kanalListesi}")

    def kanalCikar(self,cikarilcakKanal):
        kanalList=self.kanalListesi
        kanalList.remove(cikarilcakKanal)
        print("Kanal Çıkarılıyor.")
        time.sleep(1)
        print(f"Kanal Listesi:{kanalList}")

    def rastgeleKanal(self):
        rastgele=random.randint(0,len(self.kanalListesi)-1)

        self.kanal=self.kanalListesi[rastgele]
        print(self.kanal)

    def __len__(self):
        return len(self.kanalListesi)    
    
    def __str__(self):
        return f"TV Durumu:{self.tvDurum}\nTv Ses:{self.tvSes}\nKanal Listesi:{self.kanalListesi}\nKanal:{self.kanal}"


kumanda=Kumanda()
print("""
Televizyon Uygulaması
          
1.TV Aç
2.TV Kapat          
3.Ses Ayarları          
4.Kanal Ekle
5.Kanal Çıkar      
6.Kanal Sayısını Öğrenme
7.Rastgele Kanala Geçme          
8.Televizyon Bilgileri
           
Çıkmak İçin "q" Tuşuna Basınız.          
""")

while True:
    islem=input("Yapmak İstediğiniz İşlemi Seçin:")
   
    if islem == "1":
        kumanda.tvAc()

    elif islem == "2":
        kumanda.tvKapat() 

    elif islem == "3":
        kumanda.sesDuzeyi() 

    elif islem == "4":
        ekleKanal=input("Eklenecek Kanalı Yazın:")
        kumanda.kanalEkle(ekleKanal) 

    elif islem == "5":
        cikarKanal=input("Çıkarılcak Kanalı Yazın:")
        kumanda.kanalCikar(cikarKanal)

    elif islem == "6":
        print(len(kumanda))

    elif islem == "7":
        kumanda.rastgeleKanal()

    elif islem == "8":
        print(kumanda)

    elif islem == "q":
        print("Çıkış Yapılıyor...")
        break

    else:
        print("Yanlış Tuşlama Yaptınız.")    