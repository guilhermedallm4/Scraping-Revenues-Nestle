from gettext import textdomain
from pydoc import pager
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')


job = Service(ChromeDriverManager().install()) 
navegador = webdriver.Chrome(options=options, service=job)

def main():
    with open('receitas_two.csv', 'a', encoding="UTF-8") as columns:
        columns.write(('"calda_longa"') + ',')
        columns.write(('"titulo"') + ',')
        columns.write(('"ingrediente"') + ',')
        columns.write(('"modo_de_preparo"') + '\n')
    counter = 0
    response = requests.get('https://www.receitasnestle.com.br/nossas-receitas')
    site = BeautifulSoup(response.text, 'html.parser')
    menu_receitas = site.findAll('h2', attrs={'class': 'title'})
    for menu in menu_receitas:
        link_menu = menu.text
        print(link_menu)
        aux_link = str(link_menu)
        aux_link = aux_link.replace(' ','-')
        print(aux_link)
        if(aux_link != "Com-um-cadastro-em-Receitas-Nestlé,-tenha-acesso-a:" and aux_link != "Fique-por-dentro-das-novidades-e-tenha-acesso-à-benefícios-exclusivos." and  aux_link != "Crie-sua-conta:" and aux_link != "Quer-ficar-por-dentro-das-novidades-de-Receitas-Nestlé,-criar-foodlists-e-receber-dicas?"):
            link = "https://www.receitasnestle.com.br/categorias/" + aux_link
            print(link)
            get_url = link
            execute = requests.get(get_url)
            if(execute.status_code != 404):
                counter += 1
                action(get_url, counter)
                
    
    
def action(get_url, counter):
    #Selenium
        navegador.get(get_url)
        sleep(5)
        if(counter == 1):
            navegador.find_element('xpath', '//*[@id="js-modal-cadu-light-close"]').click()
            sleep(4)
        for i in range(40):
            try:    
                navegador.find_element('xpath', '//*[@id="load_more"]').click()
                print("Click:", i)
                if(i == 39):
                    lista = navegador.page_source
            except:
                print("Error")
                lista = navegador.page_source
                break
            sleep(3)
        page = BeautifulSoup(lista, 'html.parser')
        pagina = page.findAll('div', attrs={'class': 'recipes-list'})
        for captura_titulo in pagina:
            teste = captura_titulo.findAll('h2', attrs={'class': 'title'})
            for link_title in teste:
                title = str(link_title.text)
                aux_link = title.replace(' ','-')
                link_two = "https://www.receitasnestle.com.br/receitas/" + aux_link
                get_url = link_two
                if(get_url == 'https://www.receitasnestle.com.br/receitas/'):
                    break
                second_execute = requests.get(get_url)
                if(second_execute.status_code != 404):
                    second_execute = requests.get(get_url)
                    introduction = BeautifulSoup(second_execute.text, 'html.parser')
                    aux_ingrediente = introduction.findAll('div', attrs={'class': 'view-content'})
                    aux_metodo = introduction.findAll('div', attrs={'class': 'view-contents'})
                    for ingrediente in aux_ingrediente:
                        texto = ingrediente.find('ul')
                        ingred = texto.text
                        break
                    for metodo in aux_metodo:
                        metd = metodo.text
                    auxMetodo = (metd.replace(',',''))
                    print('\n')
                    print(auxMetodo)
                    with open('receitas_two.csv', 'a', encoding="UTF-8") as title_archive:
                            auxCaldaLonga = 'Como fazer '+ title 
                            title_archive.write('<h1>' + (auxCaldaLonga) +'</h1>'+ ',')
                    with open('receitas_two.csv', 'a', encoding="UTF-8") as title_archive:
                            auxTitle = title
                            title_archive.write('<h2>'+(auxTitle) +'</h2>' ',')
                    with open('receitas_two.csv', 'a', encoding="UTF-8") as ingre_archive:
                            ingre_archive.write('<p>' + (ingred.replace('\n','<br>')) +'</p>' + ',')
                    with open('receitas_two.csv', 'a', encoding="UTF-8") as preparo_archive:
                            preparo_archive.write('<p>' + (auxMetodo.replace('\n', '<br>')) +'</p>' + '\n') 

main()
