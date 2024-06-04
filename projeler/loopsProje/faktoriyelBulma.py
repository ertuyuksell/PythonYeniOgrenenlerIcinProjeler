print("""
**********************************
    Faktöriyel Bulma Programı
**********************************
Çıkmak İçin "q"ya Basınız.      
""")


while True:
    fSayi=input("Faktöriyelini Bulmak İstediğiniz Sayıyı Giriniz:")
    sonuc=1
    i=1
    if fSayi == "q":
        print("Çıkış Yapılıyor...")
        break
    elif not(fSayi == "q"):
        fSayi=int(fSayi)
        while i<=fSayi:
            sonuc=sonuc*i
            i += 1      
    print(sonuc)
    continue
           