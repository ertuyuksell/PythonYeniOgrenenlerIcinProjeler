print("""
******************************
    Armstrong Sayı Bulma
******************************
""")

sayi=input("Bulmak İstediğiniz Sayıyı Giriniz:")
basamakSayisi=len(sayi)
sayi=int(sayi)
basamak=0
toplam=0
geciciSayi=sayi
while geciciSayi>0:
    basamak = geciciSayi % 10
    toplam += basamak ** basamakSayisi
    geciciSayi //=10

if sayi==toplam:
    print(f"{sayi},Armstrong Sayıdır.")
else:
    print(f"{sayi},Armstrong Sayı Değildir.")    