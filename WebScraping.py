from urllib.request import urlopen
from bs4 import BeautifulSoup

res = urlopen('http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar')
# Lê o html
html = res.read()
soup = BeautifulSoup(html, "html.parser")
# Busca pela classe em que fica o link para acesso do pdf
link = soup.find_all("li", {"class": "item-2939"})[0]
link = link.find_all("a")[0]
link = link.get('href')
print('LINK para pagina do PDF: ', link)


# Acessa o link
res = urlopen('http://www.ans.gov.br'+link)
html = res.read()
soup = BeautifulSoup(html, "html.parser")
# Busca a tabela que está o pdf
pdf = soup.find_all("table", {"class": "table table-bordered"})[0]
for p in pdf.find_all("a"):
    aux = p.get('href')
    # Se for pdf salva o link
    if aux[len(aux)-3:len(aux)] == 'pdf': pdf = aux
print('LINK do pdf: ',pdf)


import requests
# Acessa a pagina do pdf
res = requests.get('http://www.ans.gov.br'+pdf)
# Salva o pdf
with open("./Padrão_TISS_Componente_Organizacional_202103.pdf", "wb") as f:
    f.write(res.content)
print('PDF baixado.')
