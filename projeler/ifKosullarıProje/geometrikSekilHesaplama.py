#abs(a+b) > c and abs(a+c) > b and abs(b+c) > a
print("""
***********************************
      Geometrik Şekil Hesaplama
***********************************      
""")

sekil=input("Dörtgenin Mi Yoksa Üçgenin Mi Şeklini Hesaplamak İstiyorsun:")

if sekil=="Dörtgen":
    a=float(input("Birinci Kenarı Giriniz:"))
    b=float(input("ikinci Kenarı Giriniz:"))
    c=float(input("Üçüncü Kenarı Giriniz:"))
    d=float(input("Dördüncü Kenarı Giriniz:"))

    if a==b==c==d:
        print("Bu Dörtgen Bir Karedir.")
    elif a==b and c==d or a==c and b==d or a==d or b==c:
        print("Bu Dörtgen Bir Dikdörtgendir.")
    else:
        print("Bu Dörtgen Sıradan Bir Dörtgendir.")       
elif sekil=="Üçgen":
    a=float(input("Birinci Kenarı Giriniz:"))
    b=float(input("ikinci Kenarı Giriniz:"))
    c=float(input("Üçüncü Kenarı Giriniz:"))
    if abs(a+b) > c and abs(a+c) > b and abs(b+c) > a:
        if a==b==c:
            print("Bu Üçgen Bir Eşkenar Üçgendir.")
        elif a==b or a==c or b==c:
            print("Bu Üçgen Bir İkizkenar Üçgendir.")
        else:
            print("Bu Üçgen Sıradan Bir Üçgendir.")        
    else:
        print("Verilen Kenarlar Üçgen Belirtmiyor.")
else:
    print("Hatalı Tuşlama Yaptınız!!!")    
