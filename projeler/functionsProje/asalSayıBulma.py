print("""
*****************************
       Asal Sayı Bulma
*****************************      
""")
sayi=int(input("Bulmak İstediğiniz Sayıyı Giriniz:"))
def asalSayi(sayi):
    toplam=0
    for i in range(1,sayi+1):
        if sayi % i == 0:
            toplam += i
    if toplam == sayi+1:
        print(f"{sayi},Asal Sayidir.")
    else:
        print(f"{sayi},Asal Sayı Değildir")
        
asalSayi(sayi)            