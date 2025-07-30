import requests
from bs4 import BeautifulSoup #bs4 modülünün içinden BeautifulSoup fonksiyonunu çek demektir


# requests.get() -> veri çekmek için
url=requests.get("https://tr.wikipedia.org/wiki/UEFA_%C5%9Eampiyonlar_Ligi_finalleri_listesi" )

#status_code -> çekilen veriyi kontol etmek için
#200 çıktısına verirse doğru bir şekilde çalıştığını ifade eder
a=url.status_code
print(a)


"""
a=url.content -> dediğimizde sitenin bütün html kodları gelir 

a=url.text -> sitenin bütün html kodları daha düzgün bir şekilde gelir

a=url.encoding -> hangi dile uygun olduğunu öğreniriz. Örneğin çıktı utf-8 olursa Türkçe karakterlere uygun olduğunu ifade eder 

"""

#BeautifulSoup fonksiyonu web sitesinden html kodları düzgün bir şekilde almamızı sağlar
#O yüzden url.content diyerek  html kodlarını düzgün bir şekilde alabiliriz (neden url.text'i kullanmadığımızı bilmiyorum )
#html.parser -> derleyiciye kodları nasıl parçalayacağımızı ifade ettik
soup= BeautifulSoup(url.content,"html.parser")

#print(soup.prettify()) #kodun daha güzel görünmesini sağlar

#print(soup.title) #sitenin başlığını almamızı sağlar

print(soup.title.name) # sitenin başlığının ismini almamızı sağlar. Çıktı : title (bu şekilde siteyi kodlamışlar )