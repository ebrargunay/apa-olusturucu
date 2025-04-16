import json
from datetime import datetime


#1. Adım: Json Dosyasını oku

def json_oku() -> list:
    with open("apa.json", encoding="utf-8") as apa:
       return json.loads(apa.read())

#2. Adım: Başlıklarda ilk kelimenin ilk harfi büyük ve diğer harfleri küçük olacak şekilde düzenle.

def format_baslik(yayin_baslik: str) -> str:
    return yayin_baslik.capitalize()

#3. Adım: Yazar adlarını her bir kelimesinin ilk harfi büyük olacak şekilde düzenle.

def format_yazar_adi(yazar_adi: str) -> str:
    yazar_adi = yazar_adi.title()
    ad_parcalari = yazar_adi.split()
    soyad = ad_parcalari[-1]
    adlar = ad_parcalari[:-1]
    formatlanmis_ad = f"{soyad}, "
    for ad in adlar:
        formatlanmis_ad += f"{ad[0]}. "
    return formatlanmis_ad.strip()

def join_yazar_adlari(yazar_adlari: list):
    yazar_adlari_sayisi = len(yazar_adlari)
    if yazar_adlari_sayisi == 1:
        return yazar_adlari[0]
    elif yazar_adlari_sayisi == 2:
        return yazar_adlari[0] + " ve " + yazar_adlari[1]
    elif 3 <= yazar_adlari_sayisi < 6:
        son_yazar = yazar_adlari[-1]
        diger_yazarlar = yazar_adlari[:-1]
        diger_yazarlar = ", ".join(diger_yazarlar)
        return f"{diger_yazarlar} ve {son_yazar}"
    else:
        ilk_alti_yazar = yazar_adlari[:6]
        ilk_alti_yazar = ", ".join(ilk_alti_yazar)
        return f"{ilk_alti_yazar} ve diğerleri"

#4. Adım: Id kısmını '-bugünün tarihi- tarihinde 'https://search.trdizin.gov.tr/en/yayin/detay/'-id- adresinden erişildi.' şeklinde düzenle ve tarihi DD.MM.YYYY formatında yaz.

def format_id(id_numarasi):
    bugun = datetime.now().strftime("%d/%m/%Y")
    return f"{bugun} tarihinde https://search.trdizin.gov.tr/en/yayin/detay/{id_numarasi} adresinden erişildi."

#5. Adım: Dergi adlarını her bir kelimesinin ilk harfi büyük olacak şekilde düzenle.

def format_dergi_adi(dergi_adi: str) -> str:
    return dergi_adi.title()

#6. Adım: Sayı ve cilt bilgisi ekle.

def format_dergi_sayi_cilt(dergi_sayi: str, dergi_cilt: str) -> str:
     if dergi_cilt:
         return f"{dergi_sayi}({dergi_cilt})."
     else:
         return f"{dergi_sayi}."


if __name__ == '__main__':
    yayinlar = json_oku()
    for yayin in yayinlar:
        if yayin["baslik"]:
            baslik = format_baslik(yayin["baslik"])
        if yayin["yazarlar"]:
            yazarlar = yayin["yazarlar"].split("<|>")
            yazar_adlari = []
            for yazar in yazarlar:
                formatlanmis_yazar_adlari =  format_yazar_adi(yazar)
                yazar_adlari.append(formatlanmis_yazar_adlari)
            yazarlar = join_yazar_adlari(yazar_adlari)

#7. Adım: Kaynakları yayın türüne göre düzenleyerek APA formatında yazdır.

        if yayin["yayin_turu"] == 'PAPER':
            yil = yayin["dergi_yili"]
            dergi_adi = format_dergi_adi(yayin["dergi_adi"])
            dergi_sayi_cilt = format_dergi_sayi_cilt(dergi_sayi=yayin["sayi"], dergi_cilt=yayin["cilt"])
            erisim = format_id(yayin["id"])
            print(f"{yazarlar}. ({yil}). {baslik}. {dergi_adi}, {dergi_sayi_cilt} {erisim}")
        elif yayin["yayin_turu"] == 'PROJECT':
            yil = yayin["proje_yili"]
            erisim = format_id(yayin["id"])
            print(f"{yazarlar}. ({yil}). {baslik}. {erisim}")
