import mechanicalsoup
import os
import wget

procurar_por = 'Scrapy'

browser = mechanicalsoup.StatefulBrowser()
url = 'https://images.google.com/'
browser.open(url)
browser.page.title
browser.get_url()
browser.get_current_page()

browser.select_form()
browser.get_current_form().print_summary()

# Buscar um termo
browser['q'] = procurar_por

# Exibir o browser
# browser.launch_browser()

# 'Clicar' em buscar
response = browser.submit_selected()

print(browser.get_url())

url = browser.get_url()
browser.open(url)

resposta = browser.get_current_page()
imagens = resposta.find_all('img')


imagens_url = []
for imagem in imagens:
    imagem = imagem.get('src')
    imagens_url.append(imagem)

imagens_url = [image for image in imagens_url if image.startswith('https')]
path = os.getcwd()
path = os.path.join(path, procurar_por)

os.mkdir(path)

counter = 0
for imagem in imagens_url:
    save_as = os.path.join(path, procurar_por + str(counter) + '.jpg')
    wget.download(imagem, save_as)
    counter += 1
