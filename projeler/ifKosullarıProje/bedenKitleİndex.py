print("""
*****************************
      Beden Kitle İndex
*****************************      
""")
kilo=int(input("Kilonuzu Giriniz:"))
boy=int(input("Boyunuzu Giriniz:"))
boy=boy/100
index=kilo/boy**2

if index<18.5:
    print("Beden Kilo İndexine Göre Zayıfsınız.")
elif 18.5<=index<25:
    print("Beden Kilo İndexine Göre Normalsiniz.")
elif 25<=index<30:
    print("Beden Kilo İndexine Göre Fazla Kilolusunuz.")
elif 30<index:
    print("Beden Kilo İndexine Göre Obezsiniz.")       