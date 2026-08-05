# Geliştirici: Roxie
# GitHub: https://github.com/RoxieG11/
import os
# FONKSYONLAR
def menu():
    print("")
    print (" -  -  -   -  -  -  -  -  -ROXIE Not Defteri-  -  -  -  -  -  -  -  - ")
    print("")
    print("1: Not Oluştur.")
    print("2: Not oku.")
    print("3: Notları Listele.")
    print("4: Not Sil.")
    print("5: Not İsmi Değiştir.")
    print("6: Not Düzenle.")
    print("7: Favorilere Not Ekle.")
    print("8: Favorilerden Not Çıkart.")
    print("9: Çıkış\n")

def not_olustur(not_ismi, not_metni):
    with open("Notlar/" + not_ismi, "w") as dosya:
        dosya.write(not_metni)

    return f"Yeni Not {not_ismi} İsmiyle Başarıyla Oluşturuldu"

def not_oku(okunacak_not):
    with open("Notlar/" + okunacak_not, "r") as dosya:
        return dosya.read()

def notlari_listele():
    with open ("favoriler.txt", "r") as dosya:
        favoriler = dosya.read().splitlines()
    for not_ismi in os.listdir("Notlar"):

        if not_ismi in favoriler:
            print(f"⭐", not_ismi)
        else:
            print("  ", not_ismi)

def not_sil(silinecek_not):
    os.remove("Notlar/" + silinecek_not)
    return f"{silinecek_not} İsimli Not Başarıyla Silindi.\n"

def not_isimdegis(not_ismi, yeni_not_ismi):
    os.rename("Notlar/"+ not_ismi, "Notlar/" + yeni_not_ismi)
    return f"{not_ismi} İsmi Değişti. Yeni İsim: {yeni_not_ismi}"

def not_duzenle(eski_not):
    if eski_not in os.listdir("Notlar/"):
        os.system(f"nano Notlar/{eski_not}")
        return f"{eski_not} Başarıyla Düzenlendi."

def favorilere_ekle(eklenecek_not):
    if eklenecek_not in os.listdir("Notlar/"):
        with open("favoriler.txt", "a") as dosya:
            dosya.write(eklenecek_not + "\n")
            return f"{eklenecek_not} Başarıyla Favorilere Eklendi."

def favorilerden_cıkart(cıkarılacak_not):
        with open("favoriler.txt", "r") as dosya:
            favoriler = dosya.read().splitlines()

            if cıkarılacak_not in favoriler:
                favoriler.remove(cıkarılacak_not)

                with open("favoriler.txt", "w") as dosya:
                    dosya.write("\n".join(favoriler))

                return f"{cıkarılacak_not} Başarıyla Favorilerden Çıakrtıldı. "

        
            else:
                return "HATA!  Not İsmi Yanlış Veya Böyle Bir Not Yok!"


while True:
    menu()
    try:
        islem = int(input("İşleminizi Seçin: "))
    except ValueError:
        print("HATALI İŞLEM SEÇTİNİZ! ")
        continue
    if islem not in (1,2,3,4,5,6,7,8,9):
        print("HATALI İŞLEM SEÇTİNİZ! ")
        continue

# ISLEMLER

    elif islem == 1:
        yeni_not = input("Notun ismi ne?\n ")
        yeni_not_metni = input("Notun İçine Ne yazılacak?\n ")
        sonuc = not_olustur(yeni_not, yeni_not_metni)
        print(sonuc)

    elif islem == 2:
        okunacak_not_ismi = input("Okumak istediğin notun ismin gir:\n ")
        if okunacak_not_ismi in os.listdir("Notlar"):
            sonuc = not_oku(okunacak_not_ismi)
            print(sonuc)
        else:
            print("HATA!  Not İsmi Yanlış Veya Böyle Bir Not Yok!\n ")

    elif islem == 3:
        notlari_listele()

    elif islem == 4:
        sil_not = input("Silmek İstediğiniz Notu Seçin.\n ")
        if sil_not in os.listdir("Notlar"):
            sonuc = not_sil(sil_not)
            print(sonuc)
        else:
            print("HATA!  Not İsmi Yanlış Veya Böyle Bir Not Yok!\n ")

    elif islem == 5:
        eski_not = input("Hangi Notun İsmini Değiştirmek İstiyorsunuz?\n")
        yeni_not = input("Notun Yeni İsmi Ne olacak?\n")
        if eski_not in os.listdir("Notlar/"):
            sonuc = not_isimdegis(eski_not, yeni_not)
            print (sonuc)
        else:
            print("HATA!  Not İsmi Yanlış Veya Böyle Bir Not Yok!\n ")

    elif islem == 6:
        with open("favoriler.txt", "r") as dosya:
            favoriler = dosya.read().splitlines()

        for notlar in os.listdir("Notlar"):

            if notlar in favoriler:
                print(f"⭐ {notlar}")
            else:
                print("  ", notlar)
        duzenlenecek_not = input("Düzenlemek İstediğiniz Notu Seçin: ")
        sonuc = not_duzenle(duzenlenecek_not)
        print(sonuc)


    elif islem == 7:
        print(os.listdir("Notlar/"))
        favori_not = input("Favorilere Eklemek İstediğiniz Notu Seçin: ")
        sonuc = favorilere_ekle(favori_not)
        print(sonuc)

    elif islem == 8:
        fav_cik = input("Favorilerden Çıkartacağınız Notu Seçin: ")
        sonuc = favorilerden_cıkart(fav_cik)
        print(sonuc)

    elif islem == 9:
        print("Programdan Çıkılıyor...")
        break
    else:
        print("Bilinmeyen Bir Hata Oluştu! ")
        continue
