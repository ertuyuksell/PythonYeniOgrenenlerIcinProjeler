print("""
************************************
      En Büyük Sayıyı Bulma
************************************
""")

a=int(input("Birinci Sayıyı Giriniz:"))
b=int(input("İkinci Sayıyı Giriniz:"))
c=int(input("Üçüncü Sayıyı Giriniz:"))

if a>=b and a>=c :
    print("En Büyük Sayı:",a)
elif b>=a and b>=c :
    print("En Büyük Sayı:",b)
elif c>=b and c>=a :
    print("En Büyük Sayı:",c)     