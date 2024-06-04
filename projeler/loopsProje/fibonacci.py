a=1
b=1
fibonacci=[a,b]
fibonacciSayi=int(input("Fibonaccisini Bulmak İstediğiniz Sayıyı Giriniz:"))
if fibonacciSayi == 1 or fibonacciSayi == 2:
    print("Fibonacci Değeri:1") 
else:       
    for i in range(0,fibonacciSayi-2):
        a,b=b,a+b
        fibonacci.append(b)
        sonuc=b    
print("Fiboncaci Değeri:",sonuc)
print("Fibonacci Listesi:",fibonacci)
