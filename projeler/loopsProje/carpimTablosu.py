print("""
******************************
    Çarpım Tablosu
******************************
""")
sayi1=int(input("Çarpılacak Sayilardan İlki:"))
sayi2=int(input("Çarpılacak Sayilardan İkincisi:"))
for i in range(1,sayi1+1):
    print("****************************")
    for x in range(1,sayi2+1):
        sonuc=i*x
        print(f"{i}x{x}={sonuc}")