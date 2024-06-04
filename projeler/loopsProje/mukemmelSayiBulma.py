print("""
******************************
    Mükemmel Sayı Bulma
******************************
""")

sayi=int(input("Bulmak İstediğiniz Sayıyı Giriniz:"))
bolum=0
for i in range(1,sayi):
    if sayi % i == 0:
        bolum += i
    else:
        continue

if bolum == sayi:
    print(f"{sayi},Mükemmel Sayıdır.")
else:
    print(f"{sayi},Mükemmel Sayı Değildir.")        