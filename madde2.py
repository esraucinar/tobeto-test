#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas=float(input("maaşınızı giriniz:"))
zamOranı=float(input("zam oranını giriniz:%"))
yeniMaas=float(maas + (maas*zamOranı)/100)
print("zamlı maaşınız:", yeniMaas)
