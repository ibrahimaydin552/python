import random
kelimeliste = ["araba","bilgisayar","telefon","dolap","batarya","şarj"]
a = random.randint(1,len(kelimeliste))
kelime = kelimeliste[a]
uzunluk = len(kelimeliste[a])
say = 0
dogru = 0
altcizgi = []
for i in range(uzunluk):
    altcizgi.append("_")


print(" ".join(altcizgi))
while True:
    harf = input("Bir Harf Giriniz: ").lower()
    if harf in kelime:
        dogru += 1
        f = kelime.index(harf)
        altcizgi[f] = harf
        print(" ".join(altcizgi))
        if dogru == uzunluk:
            print("Tebrikler bildiniz")
            break
    else:
        say += 1
        print(" ".join(altcizgi))
        print(f"Kalan Deneme Hakkı{6-say}")
    if say == 6:
        print("İşlem Hakkınız Kalmadı")
        break
