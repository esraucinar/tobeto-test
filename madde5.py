#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

sayi=input("Bir sayı giriniz:")
ters_sayi= sayi[::-1]
if sayi==ters_sayi:
    print("Girilen sayı bir palindromdur.")
else:
    print("Girilen sayı bir palindrom değildir.")