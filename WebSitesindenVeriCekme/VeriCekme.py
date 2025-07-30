import requests
from bs4 import BeautifulSoup

headers = {
     "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
     "Accept" :"application/json, text/plain, */*"

 }
url = "https://apigw.trendyol.com/discovery-web-websfxproductgroups-santral/api/v2/product-groups?productGroupIds=693671575&productGroupIds=633574004&productGroupIds=696880061&productGroupIds=618424367&productGroupIds=684242505&productGroupIds=653836255&productGroupIds=684241879&productGroupIds=637943102&productGroupIds=684242505&productGroupIds=653836255&productGroupIds=684241879&productGroupIds=664152601&productGroupIds=175331247&productGroupIds=671572645&productGroupIds=611774890&productGroupIds=129449205&productGroupIds=684008320&productGroupIds=681620329&productGroupIds=323005559&productGroupIds=664152601&productGroupIds=173487692&productGroupIds=671572645&productGroupIds=577259553&productGroupIds=659053895&channelId=1"
response= requests.get(url,headers=headers)

if response.status_code==200:
    veri = response.json()
#equests.get(...) fonksiyonuyla gelen yanıt (response) genellikle JSON formatındadır.
#.json() metodu, bu JSON verisini Python veri yapılarına (örneğin: dict, list) otomatik olarak dönüştürür.
    
    # result sözlüğündeki her grup id'si için döngü
    for grup_id, urun_listesi in veri["result"].items(): #grup_id: "129449205" gibi string anahtar
        for urun in urun_listesi:
            name = urun.get("name", "Yok")
            url = urun.get("url", "Yok")
            imageUrl = urun.get("imageUrl", "Yok")
            price = urun.get("price", {}).get("sellingPrice", "Yok")
            currency = urun.get("price", {}).get("currency", "TL")
            print(f"{name} → {price} {currency}")


else:
    print("Veri çekilemedi:", response.status_code)