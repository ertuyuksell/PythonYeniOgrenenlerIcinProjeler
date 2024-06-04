print("""
**************************************
      ATM Makinesine Hoşgeldiniz
**************************************
İşlemler

1.Bakiye Sorgulama

2.Para Yatırma
                 
3.Para Çekme
      
Programdan Çıkmak İçin "q" Tuşuna Basınız.
""")

bakiye=1000

while True:
    islem=input("Yapmak İstediğiniz İşlemi Seçin:")
    if islem == "1":
        print("Bakiye:",bakiye)
    elif islem == "2":
        yTutar=int(input("Yatırmak İstediğiniz Tutarı Giriniz:"))
        bakiye=bakiye+yTutar
    elif islem == "3":
        cTutar=int(input("Çekmek İstediğiniz Tutarı Giriniz:"))
        if bakiye >= cTutar:  
            bakiye=bakiye-cTutar
        else:
            print("Bakiyeniz Yetersiz.")
            continue    
    else:
        print("Geçersiz İşlem.")

    if islem == "q":
        print("Çıkış Yapılıyor...")
        break        
