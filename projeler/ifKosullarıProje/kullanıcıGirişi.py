print("""
******************************
      Kullanıcı Girişi
******************************
""")

kullaniciAdi=input("Kullanıcı Adı:")
parola=input("Parola:")

kAdi="Ertu"
kSifre="1234"

if kAdi==kullaniciAdi:
    if kSifre==parola:
        print("Giriş yapılıyor...")
    else:
        print("Parola Yanlış")
elif kSifre==parola:
    print("Kullanıcı Adı Yanlış")
else:
    print("Kullanıcı Adı Ve Parola Yanlış")                