#Importlar
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.testlericoz.com/coz/3m012") #Linki açma
soup = BeautifulSoup(page.content, 'html.parser') #Linkteki sayfanın html kodlarını bulma

cevaplar = soup.find_all(class_="mtq_marker mtq_correct_marker") #Tüm doğru şıkları bulma

# Cevapları yazdırma
for cevap in cevaplar:
    print(str(cevaplar.index(cevap)+1)+"-"+"ABCD"[int(cevap.get('id').split("-")[2])-1])
