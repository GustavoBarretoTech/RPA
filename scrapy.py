from bs4 import BeautifulSoup as soup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
site = requests.get("https://quotes.toscrape.com/" , headers=headers)

s = soup(site.text , "html.parser")
botoes = s.find_all("div" , class_="quote")

for botao in botoes:
    print(botao.find("span" , class_="text").text)
    print()