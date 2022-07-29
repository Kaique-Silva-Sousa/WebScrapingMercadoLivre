import requests
from bs4 import BeautifulSoup

print('Web Scraping simples com o Mercado Livre')
url = input('Digite o link do produto: ')
try:
    response = requests.get(url)
    html = BeautifulSoup(response.text,'html.parser')
except:
    print('Utilize um link valido.')
try:
    for produto in html.select('.mr-32'):
        titulo = produto.select_one('.ui-pdp-title')
        preco_inteiro = produto.select_one('.ui-pdp-price--size-large .andes-money-amount--cents-superscript .andes-money-amount__fraction')
        preco_centavo = produto.select_one('.andes-money-amount__cents--superscript-36')
        print(f'Nome do Produto: {titulo.text}\nPreço: R${preco_inteiro.text},{preco_centavo.text}')
except Exception as e:
    print(f'Use o link de um produto do Mercado Livre!')
