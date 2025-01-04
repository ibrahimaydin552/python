def topla(x,y) : return x+y
def cıkar(x,y) : return x-y
def carp (x,y) : return x*y
def bol (x,y) : return x/y
def usal (x,y) : return x**y
def modal (x,y) : return x%y
def yuzdeal(x,y) : return x*y/100

while True:
    sayi = int(input("1. Sayıyı Giriniz: "))
    sayi2 = int(input("2. Sayıyı Giriniz: "))
    islem = input("Yaptırmak İstediğiniz İşlemi Giriniz: ").lower().strip()
    if islem.count(" ") in [0,1,2,3,4,5]:
        islem.replace(" ","")
        if islem in ["toplama","t","+"]:
            print(f"{sayi}+{sayi2}={topla(sayi,sayi2)}")  
        elif islem in ["çıkarma","-","ç"]: 
            print(f"{sayi}-{sayi2}={cıkar(sayi,sayi2)}") 
        elif islem in ["çarpma","*","çar"]: 
            print(f"{sayi}*{sayi2}={carp(sayi,sayi2)}") 
        elif islem in ["bölme","/","b"]: 
            print(f"{sayi}/{sayi2}={bol(sayi,sayi2)}")
        elif islem in ["üs alma","ü","**"]: 
            print(f"{sayi}**{sayi2}={usal(sayi,sayi2)}") 
        elif islem in ["mod alma","m"]: 
            print(f"{sayi}%{sayi2}={modal(sayi,sayi2)}")
        elif islem in ["yüzde alma","%"]:
            yuzde1 = float(input("Yüzdesi alınacak sayıyı giriniz: "))
            yuzde2 = float(input("Yüzde Kaçının Alınmasını İstiyorsunuz: "))
            print(f"{yuzde1} in % {yuzde2} si = {yuzdeal(yuzde1,yuzde2)}")
        cikis = input("Sistemden Çıkmak İster Misiniz? (Evet/Hayır)").lower()
        if cikis in ["evet","e"]:
            print("Güle Güle")
            break
