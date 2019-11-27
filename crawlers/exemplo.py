
import requests
from bs4 import BeautifulSoup


host = 'http://127.0.0.1:5000'
def getContent():
    page = requests.get(host)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def getLinks():
    page = requests.get(host)

    # Criar o objeto BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser').find_all('a')
    all_links = []
    for links in soup:
        if(links['href']== '/'):
            all_links.append(host)
        else:
            all_links.append(host+'/'+links['href'])

        print(links)
    return all_links


def getInfor():
    page = requests.get(host)
    
    # Criar o objeto BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser').find_all('section')
    dados = []
    for artigos in soup:
        artigo = {
            'img':artigos.img['src'],
            'text':artigos.p.getText(),
            'author': artigos.find(id='author').getText()
        }

        dados.append(artigo)
    return dados

print(getInfor())