#Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayi1=int(input("ilk sayıyı giriniz:"))
sayi2=int(input("ikinci sayıyı giriniz:"))
sayi3=int(input("üçüncü sayıyı giriniz:"))
if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBuyuk=sayi1
elif (sayi2>sayi1) and (sayi2>sayi3):
    enBuyuk=sayi2
else:
    enBuyuk=sayi3

print("Girilen sayılar içinde en büyük olanı:",enBuyuk)
        
