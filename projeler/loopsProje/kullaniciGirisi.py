print("""
******************************
      Kullanıcı Girişi
******************************
""")
kAdi="Ertu"
kSifre="1234"
girisHakki=3
while True:
    kullaniciAdi=input("Kullanıcı Adı:")
    parola=input("Parola:")
    if kAdi==kullaniciAdi:
        if kSifre==parola:
            print("Giriş yapılıyor...")
            break
        else:
            print("Parola Yanlış")
            girisHakki -=1
    elif kSifre==parola:
        print("Kullanıcı Adı Yanlış")
        girisHakki -=1
    else:
        print("Kullanıcı Adı Ve Parola Yanlış")
        girisHakki -=1
    if girisHakki == 0:
        print("Giriş Hakkınız Bitti.")
        break                    