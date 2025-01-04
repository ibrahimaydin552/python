while True:
    sayi = int(input("1. Sayıyı Giriniz: "))
    sayi2 = int(input("2. Sayıyı Giriniz: "))
    islem = input("Yaptırmak İstediğiniz İşlemi Giriniz: ").lower()
    if islem.count(" ") in [0,1,2,3,4,5]:
        islem.replace(" ","")
        if islem in ["toplama","t","+"]: 
            print(f"{sayi}+{sayi2}={sayi+sayi2}") 
        elif islem in ["çıkarma","-","ç"]: 
            print(f"{sayi}-{sayi2}={sayi-sayi2}") 
        elif islem in ["çarpma","*","çar"]: 
            print(f"{sayi}*{sayi2}={sayi*sayi2}") 
        elif islem in ["bölme","/","b"]: 
            print(f"{sayi}/{sayi2}={sayi/sayi2}")
        elif islem in ["üsalma","ü","**"]: 
            print(f"{sayi}**{sayi2}={sayi**sayi2}") 
        elif islem in ["modalma","m"]: 
            print(f"{sayi}%{sayi2}={sayi%sayi2}")
        cikis = input("Sistemden Çıkmak İster Misiniz? (Evet/Hayır)").lower()
        if cikis in ["evet","e"]:
            print("Güle Güle")
            break