while True:
    sayi = int(input("1. Sayıyı Giriniz: "))
    sayi2 = int(input("2. Sayıyı Giriniz: "))
    islem = input("Yaptırmak İstediğiniz İşlemi Giriniz: ")

    if islem == "Toplama" or islem == "+" or islem == "toplama" or islem == "t": 
        print(f"{sayi}+{sayi2}={sayi+sayi2}") 
    elif islem == "Çıkarma" or islem ==  "-" or islem ==  "ç" or islem ==  "çıkarma": 
        print(f"{sayi}-{sayi2}={sayi-sayi2}") 
    elif islem == "Çarpma" or islem ==  "*" or islem ==  "çar" or islem ==  "çarpma": 
        print(f"{sayi}*{sayi2}={sayi*sayi2}") 
    elif islem == "Bölme" or islem ==  "/" or islem ==  "bölme" or islem ==  "b": 
        print(f"{sayi}/{sayi2}={sayi/sayi2}")
    elif islem == "üs alma" or islem ==  "**" or islem ==  "üs alma" or islem ==  "ü": 
        print(f"{sayi}**{sayi2}={sayi**sayi2}") 
    elif islem == "mod alma" or islem ==  "m" or islem ==  "Mod Alma" or islem ==  "Mod alma": 
        print(f"{sayi}%{sayi2}={sayi%sayi2}")
    cikis = input("Sistemden Çıkmak İster Misiniz? (Evet/Hayır)")
    if cikis == "Evet" or cikis ==  "E" or cikis ==  "e" or cikis ==  "evet":
        print("Güle Güle")
        break