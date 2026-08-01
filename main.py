# Geliştirici: Roxie
# GitHub: https://github.com/RoxieG11/
import os
# FONKSYONLAR
def menu():
    print("")
    print (" -  -  - ROXIE Not Defteri  -  -  -")
    print("")
    print ("         1: Not Oluştur.")
    print ("         2: Not oku.")
    print ("         3: Notları Listele.")
    print ("         4: Not Sil.")
    print("          5: Not İsmi Değiştir.")
    print("          6: Çıkış.")

def not_olustur(not_ismi, not_metni):
    with open("Notlar/" + not_ismi, "w") as dosya:
        dosya.write(not_metni)

    return f"Yeni Not {not_ismi} İsmiyle Başarıyla Oluşturuldu"

def not_oku(okunacak_not):
    with open("Notlar/" + okunacak_not, "r") as dosya:
        return dosya.read()

def notlari_listele():
    for listele in os.listdir("Notlar"):
        print(listele)

def not_sil(silinecek_not):
    os.remove("Notlar/" + silinecek_not)
    return f"{silinecek_not} İsimli Not Başarıyla Silindi.\n"

def not_isimdegis(not_ismi, yeni_not_ismi):
    os.rename("Notlar/"+ not_ismi, "Notlar/" + yeni_not_ismi)
    return f"{not_ismi} İsmi Değişti. Yeni İsim: {yeni_not_ismi}"


while True:
    menu()
    try:
        islem = int(input("İşleminizi Seçin:\n "))
    except ValueError:
        print("HATALI İŞLEM SEÇTİNİZ! ")
        continue
    if islem not in (1,2,3,4,5,6):
        print("HATALI İŞLEM SEÇTİNİZ! ")
        continue

# İŞLEMLER

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
        print("Programdan Çıkılıyor...")
        break
    else:
        print("HATA!  Not İsmi Yanlış Veya Böyle Bir Not Yok!\n ")
        continue
