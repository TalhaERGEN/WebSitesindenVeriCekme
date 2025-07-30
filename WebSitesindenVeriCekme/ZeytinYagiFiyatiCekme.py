import requests
from bs4 import BeautifulSoup

url= requests.get("https://www.trendyol.com/sivi-yaglar-x-c103982?pi=2")
if url.status_code == 200:
    print("siteden veri çekilebilir")
else:
    print("siteden veri çekilemez")

soup=BeautifulSoup(url.content,"html.parser")

sayac=1
# Ürünleri bulmak için 'prdct-cntnr-wrppr' div'i içindeki her bir 'p-card-wrppr' div'ini gez
for i in soup.find("div",{"class":"prdct-cntnr-wrppr"}).find_all("div",{"class":"p-card-wrppr"}):
    baslik_al=i.find("div",{"class": "with-basket-button"}).span.text
    #ürün adı span adı altında idi.O yüzden .span yazarak sadece span kısmını aldık
    #span.text diyerek span içindeki etiketleri yok ettik
    #print(baslik_al)

    fiyat_al=i.find("div",{"class":"price-information"}).text
    #print(baslik_al,fiyat_al)

    #önceki çıktı : Hızlı TeslimatKargo Bedava şeklinde olan ürünler vardı onu replace() fonk. ile düzelttik
    kargo_al=i.find("div",{"class":"product-stamps-container"}).text.replace("Hızlı TeslimatKargo Bedava","Hızlı Teslimat-Kargo Bedava")
   # print(baslik_al , "->" ,fiyat_al,kargo_al)


    # Temel bir url(domain) tanımlamam gerekti.Çünkü sistemde domain kısmı yer almıyordu.
    base_url = "https://www.trendyol.com"

    # get("href")->burada request modülü kullanılarak "href" çekildi
    urun_link_al=base_url+ i.find("a",{"class": "p-card-chldrn-cntnr"}).get("href")
    print(f"{sayac}.Ürün Adı : {baslik_al}\nFiyat : {fiyat_al}\nKargo Durumu : {kargo_al}\nÜrün Link : {urun_link_al}\n ")
    sayac+=1