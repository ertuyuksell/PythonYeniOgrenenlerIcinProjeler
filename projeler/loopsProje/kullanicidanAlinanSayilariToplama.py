print("""
**********************************************
    Kullanıcıdan Alınan Sayıları Toplama
**********************************************
Çıkmak için "q" Tuşuna Basınız.      
""")
toplam=0
while True:
    sayi=input("Toplanmasını İstediğiniz Sayıyı Giriniz:")
    if sayi == "q":
        print(toplam)
        print("Çıkış Yapılıyor...")
    else:
        sayi=int(sayi)
        print(f"{toplam}+{sayi}:{toplam+sayi}")
        toplam += sayi
    