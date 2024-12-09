from bs4 import BeautifulSoup
import requests

'''with open('teste.html', encoding="utf-8") as file:
    conteudo = file.read()

ex = BeautifulSoup(conteudo, 'lxml')

# find() pega o primeiro que passar como parametro e find_all pega todos
tags = ex.find_all(class_='um')

for tag in tags:
    print(tag.text)'''


url = 'https://www.globo.com/'
page = requests.get(url)

print("A resposta do servidor foi:", page)

resposta = page.text

soup =  BeautifulSoup(resposta, 'html.parser')

noticias = soup.find_all('h2', {'class':'post__title'})

for noticia in noticias:
    print(noticia.text)