print("HESAP MAKİNESİ programına hoşgeldiniz. \n"
      "Toplama işlemi için 1'e, \n"
      "Çıkarma işlemi için 2'ye, \n"
      "Çarpma işlemi için 3'e, \n"
      "Bölme işlemi için 4'e basınız. \n"
      "\n"
      "Virgüllü sayılarla işlem yapmak için 10'a basınız.")
Menü = int(input("Lütfen işlem yapacağınız sayıyı giriniz."))
if Menü == 1:
    İlkSayı = int(input("Lütfen 1.sayıyı giriniz."))
    İkinciSayı = int(input("Lütfen 2.sayıyı giriniz."))
    Toplam = İlkSayı + İkinciSayı
    print(f"İşlem Sonucunuz: {Toplam}'dir. İyi günler dileriz.")
    print("Lütfen Enter'a basınız.")
elif Menü == 2:
    İlkSayı = int(input("Lütfen 1.sayıyı giriniz."))
    İkinciSayı = int(input("Lütfen 2.sayıyı giriniz."))
    Toplam = İlkSayı - İkinciSayı
    print(f"İşlem Sonucunuz: {Toplam}'dir. İyi günler dileriz.")
    print("Lütfen Enter'a basınız.")
elif Menü == 3:
    İlkSayı = int(input("Lütfen 1.sayıyı giriniz."))
    İkinciSayı = int(input("Lütfen 2.sayıyı giriniz."))
    Toplam = İlkSayı * İkinciSayı
    print(f"İşlem Sonucunuz: {Toplam}'dir. İyi günler dileriz.")
    print("Lütfen Enter'a basınız.")
elif Menü == 4:
    İlkSayı = int(input("Lütfen 1.sayıyı giriniz."))
    İkinciSayı = int(input("Lütfen 2.sayıyı giriniz."))
    Toplam = İlkSayı / İkinciSayı
    print(f"İşlem Sonucunuz: {Toplam}'dir. İyi günler dileriz.")
    print("Lütfen Enter'a basınız.")
else:
    print("Yanlış sayı tuşladınız. Lütfen tekrar deneyiniz.")
    print("Lütfen Enter'a basınız.")
if Menü == 10:
    print("Virgüllü Sayılarda \n"
          "Toplama işlemi yapmak için 11'e, \n"
          "Çıkarma işlemi yapmak için 12'ye, \n"
          "Bölme işlemi yapmak için 13'e, \n"
          "Çarpma işlemi yapmak için 14'e basınız.")
    Altmenü = int(input("Hangi işlemi yapmak istiyorsunuz?"))
    if Altmenü == 11:
        BirinciSayı = float(input("İlk sayıyı giriniz."))
        İKİNCİsayı = float(input("İkinci sayıyı giriniz."))
        ToplamSonuç = BirinciSayı + İKİNCİsayı
        print(f"İşlem sonucunuz: {ToplamSonuç}'dir. İyi günler dileriz.")
        print("Lütfen Enter'a basınız.")
    elif Altmenü == 12:
        BirinciSayı = float(input("İlk sayıyı giriniz."))
        İKİNCİsayı = float(input("İkinci sayıyı giriniz."))
        ToplamSonuç = BirinciSayı - İKİNCİsayı
        print(f"İşlem sonucunuz: {ToplamSonuç}'dir. İyi günler dileriz.")
        print("Lütfen Enter'a basınız.")
    elif Altmenü == 13:
        BirinciSayı = float(input("İlk sayıyı giriniz."))
        İKİNCİsayı = float(input("İkinci sayıyı giriniz."))
        ToplamSonuç = BirinciSayı / İKİNCİsayı
        print(f"İşlem sonucunuz: {ToplamSonuç}'dir. İyi günler dileriz.")
        print("Lütfen Enter'a basınız.")
    elif Altmenü == 14:
        BirinciSayı = float(input("İlk sayıyı giriniz."))
        İKİNCİsayı = float(input("İkinci sayıyı giriniz."))
        ToplamSonuç = BirinciSayı * İKİNCİsayı
        print(f"İşlem sonucunuz: {ToplamSonuç}'dir. İyi günler dileriz.")
        print("Lütfen Enter'a basınız.")
    else:
        print("Yanlış sayı tuşladınız. Lütfen tekrar deneyiniz.")
        print("Lütfen Enter'a basınız.")