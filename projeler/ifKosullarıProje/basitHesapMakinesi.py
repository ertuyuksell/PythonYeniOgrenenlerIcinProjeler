#hesap makinesi başlığı yap toplama çıkarma çarpma bölme secim yaptır

print("""
********************
Basit Hesap Makinesi  
********************          

İşlemler
      
1.Toplama
2.Çıkarma      
3.Bölme
4.Çarpma
            
""")
a=input("Birinci sayıyı giriniz: ")
b=input("İkinci sayıyı giriniz:")
secim=input("Yapmak İstediğiniz işlemi Seçin:")
a=int(a)
b=int(b)
secim=int(secim)

if secim == 1:
    print("Toplama Sonucu:",a+b)

elif secim == 2:
    print("Çıkarma Sonucu:",a-b)

elif secim == 3:
    print("Çarpma Sonucu:",a*b)

elif secim == 4:
    print("Bölme Sonucu:",a/b)

else:
    print("Hatalı Tuşlama Yaptınız.")