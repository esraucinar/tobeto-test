sayi=input("Bir sayı giriniz:")
ters_sayi= sayi[::-1]
if sayi==ters_sayi:
    print("Girilen sayı bir palindromdur.")
elif sayi!=ters_sayi:
    print("Girilen sayı bir palindrom değildir.")