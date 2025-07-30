import requests
from bs4 import BeautifulSoup

url=requests.get("https://tr.wikipedia.org/wiki/UEFA_%C5%9Eampiyonlar_Ligi_finalleri_listesi")
if url.status_code == 200:
    print("siteden veri çekilebilir")
else:
    print("siteden veri çekilemez")

soup=BeautifulSoup(url.content,"html.parser")

"""
Sitenin tamamı html tag'ı içindedir. Biz bütün htlm kodlarını almak istediğimizde ".html" şeklinde uygularız.
soupt.html yazmamızın sebebi ise sitenin düzenlenmiş halini soup değişkenine atadığımız için (soup=BeautifulSoup(url.content,"html.parser"))

yazdir=soup.html
print(yazdir)

"""

"""
html sitenin genelini ifade ederken "body" kısmi ise sitenin içinde bütün elenmentlerin olduğu tag'lardır. 
soupt.body yazmamızın sebebi ise sitenin düzenlenmiş halini soup değişkenine atadığımız için (soup=BeautifulSoup(url.content,"html.parser"))

yazdir=soup.body
print(yazdir)

"""

"""
#Sayfayi inclediğimizde title kısmı head'in içinde. Biz siteden title'ı çekmek istediğimiz ".head.title" yazmamız gerekiyor.
yazdir=soup.head.title
print(yazdir)

#Bu kodun çıktısı :<title>UEFA Şampiyonlar Ligi finalleri listesi - Vikipedi</title>
# <title> etiketlerinin istediğimiz taktirde -> "yazdir=soup.head.title.text" şeklinde yazmalıyız 
"""
#---------------------------------------------------------------------------------------------------
"""
#Sayfanın içindeki paragrafları almak istediğimizde :
#yazdir=soup.find("p")
#find() -> sitemizden bulmak istediğimiz kısmı ifade eder.
# "p" sitenin html kodlarındaki paragrafların bulunduğu kısımdır. Bu kısmın etiketi <p> şeklindedir.
#print(yazdir)
#çıktı : <p class="cdx-dialog__header__subtitle">Bu, bu sayfanın kontrol edilmiş bir sürümüdür</p>
#etiketleri istemiyorsak : yazdir=soup.find("p").text yazmamız gerekiyor
"""

"""
#Not: Bu şekilde sadece siteden ilk paragrafı alırız. Bütün paragrafları almak istediğimizde :

yazdir=soup.find_all("p")
print(yazdir) 
"""

"""
#etiketleri almak istemediğimizde .text bu sefer işe yaramıyor onun yerine :
yazdir=soup.find_all("p")
for i in yazdir:
    print(i.text)
"""

"""
# başlıkları çekmek istediğimizde "h2" etiketini aratmalıyız :
yazdir=soup.find_all("h2")
for i in yazdir:
    print(i.text)
"""

#---------------------------------------------------------------------------------------------

"""
#Sitenin "Kaynakça" kısmı <div> etiketi altında.Direkt bu etiketi arattığımızda :
yazdir=soup.find("div")
print(yazdir)
#Bütün div'leri karışık şekilde veriyor.
# find() metodu sadece ilk denk gelen öğeyi döndürmelidir. Ancak burada önemli bir nokta var:
# Eğer sayfada <div> etiketlerinin içinde başka <div> etiketleri varsa veya dinamik içerik yüklemesi yapılıyorsa, 
# bu durum find() metodunun tüm içerikleri içermesine neden olabilir.
"""

"""
#Sadece "Kaynakça" kısmını çekmek için özel olarak aratmalıyız.Bunun için sözlükleri kullanmalıyız.
yazdir=soup.find("div",{"class": "reflist"})
print(yazdir)
#Sözlük kullanmamızın sebebi sözlükte key-value şeklinde veri kullanabilmemiz.
"""

"""
#Eğer linkleri almak istersek veri çektiğimizde linklerin hangi etiket içinde tutulduğunuz öğrenebiliriz.
#Yukarıdaki kodu çalıştırdığımızda :
# <a class="external text" href="https://tr.wikipedia.org/w/index.php?title=%C3%96zel:G%C3%BCnl%C3%BCk&amp;type=review&amp;page=UEFA_%C5%9Eampiyonlar_Ligi_finalleri_listesi">kontrol edildi</a>
# şeklinde tutulduğunu görürüz
#İlk başta veriyi a etiketine göre düzenlemeliyiz
#İlk bulduğu veriyi bize verir : <a class="external text" href="https://tr.wikipedia.org/w/index.php?title=%C3%96zel:G%C3%BCnl%C3%BCk&amp;type=review&amp;page=UEFA_%C5%9Eampiyonlar_Ligi_finalleri_listesi">kontrol edildi</a>
yazdir=soup.find("a",{"class": "external text"})
#Bunun için request modülünü kullanırız :
print(yazdir.get("href"))

#Not: Örneğin istediğimiz veri li etiketi altındaki a etiketinde olsaydı
#yazdir=soup.find("li",{"class": "external text"}).a şeklinde de yapabilirdik

"""

#sitedeki fotoğrafı çekmek için
yazdir=soup.find("a",{"class": "mw-file-description"}).img
print(yazdir.get("src"))
#veriyi ilk önce class'a oradan img'ye oradan da src'ye indirgedik. sounucunda şu şekilde veriyi aldık :
#//upload.wikimedia.org/wikipedia/commons/thumb/3/3b/2005_European_Champion_Clubs%27_Cup_%28cropped%29.jpg/250px-2005_European_Champion_Clubs%27_Cup_%28cropped%29.jpg