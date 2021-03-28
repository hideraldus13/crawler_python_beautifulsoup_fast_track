import requests
from bs4 import BeautifulSoup as bs

usuario = input("Usuário do GitHub: ")
url = 'https://github.com/' + usuario
r = requests.get(url)

if r.status_code == 200:
    soup = bs(r.content, 'html.parser')
    url_img_perfil = soup.find('img', {'alt': 'Avatar'})['src']
    print(url_img_perfil)
else:
    print('Usuário não encontrado')