import requests
from bs4 import BeautifulSoup

# Tefas'ın sitesinden belirtilen fonun 1 yıllık verisini getirir

fonkod = input("Fon kodu?: ")
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0;"
            "Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"}
with requests.get("https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod=" + fonkod,
                    headers=headers) as url:
    data = url.content
soup = BeautifulSoup(data, features="html.parser")
# Tarih ve rakam bilgisi javascript'in içindeki chartMainContent_FonFiyatGrafik fonksiyonunda 
js_text = soup.find_all('script', type="text/javascript")
for fiyat in range(len(js_text)):
        if len(js_text[fiyat].contents) == 0:
                continue
        if js_text[fiyat].contents[0].find("chartMainContent_FonFiyatGrafik") > 0:
                kacinci = fiyat
                break
# fonksiyondan gelen veriyi düzeltmek için
tarih_rakam = js_text[kacinci].contents[0].split("categories")
tarih = tarih_rakam[1].split("]")[0].split("[")[1]
rakam = tarih_rakam[1].split("[")[4].split("]")[0]


print("tarih, ", tarih, ", rakam, ", rakam)
