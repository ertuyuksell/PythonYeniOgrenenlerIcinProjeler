print("""
******************************
      Harf Notu Hesaplama
******************************
""")

vize1=int(input("Birinci Vize Notunuzu Giriniz:"))
vize2=int(input("İkinci Vize Notunuzu Giriniz:"))
final=int(input("Final Notunuzu Giriniz:"))

hNotu=((vize1+vize2)*3/10)+(final*4/10)

if 100 >= hNotu >= 90:
    print("Harf notunuz AA.")
elif 90 > hNotu >= 85:
    print("Harf notunuz BA.")
elif 85 > hNotu >= 80:
    print("Harf notunuz BB.")
elif 80 > hNotu >= 75:
    print("Harf notunuz CB.")
elif 75 > hNotu >= 70:
    print("Harf notunuz CC.")
elif 70 > hNotu >= 65:
    print("Harf notunuz DC.")  
elif 65 > hNotu >= 60:
    print("Harf notunuz DD.") 
elif 60 > hNotu >= 55:
    print("Harf notunuz FD.") 
else:
    print("Harf notunuz FF.")                               