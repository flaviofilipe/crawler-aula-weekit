
## Requerimentos para começar
- [Python 3.x](https://www.python.org/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

**Obs:** Todo teste foi executado utilizando o sistema **Ubuntu 18.04**. Para outros sistemas operacionais poderá ocorrer algumas pequenas modificações. Qualquer dúvida, acesse a documentação oficial da ferramenta.

## Criar ambiente de desenvolvimento



Criação do ambiente virtual na pasta *raiz* do projeto 
```
virtualenv venv
```

Ativação do ambiente
```
source venv/bin/activate
```

Instalar pacotes [request](https://requests.readthedocs.io/pt_BR/latest/), [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) e [Flask](https://flask.palletsprojects.com/)
```
pip install request
pip install beautifulsoup4
pip install Flask
```
## Estrutura do projeto
+ **venv** - Ambiente virtual com os pacotes instalados
+ **app** - Toda a aplicação
	+ \_\_init__.py - Insere as configurações do Flask
	+ controller.py - Rotas e metodos para chamar o crawler
	+ crawlers
		+  \_\_init__.py
		+  noticias.py - Crawler responsável por pegar as noticias do site
+ **config.py** - Configurações do Flask
+ **run.py** - Comando para executar a aplicação

## Possíveis erros

 - [SSLError - certificate verify failed ](https://stackoverflow.com/questions/34503206/ssl-certificate-verify-failed-error-when-scraping-https-www-thenewboston-co)

