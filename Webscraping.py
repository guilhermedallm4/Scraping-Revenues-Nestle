
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.receitasnestle.com.br/nossas-receitas')
site = BeautifulSoup(response.text, 'html.parser')
menu_receitas = site.findAll('h2', attrs={'class': 'title'})
global counter_archive
counter_archive = 0
for categorias_receitas in menu_receitas:
    titulo = categorias_receitas.text
    aux_link = str(titulo)
    aux_link = aux_link.replace(' ','-')
    if(aux_link != "Com-um-cadastro-em-Receitas-Nestlé,-tenha-acesso-a:" and aux_link != "Fique-por-dentro-das-novidades-e-tenha-acesso-à-benefícios-exclusivos." and  aux_link != "Crie-sua-conta:" and aux_link != "Quer-ficar-por-dentro-das-novidades-de-Receitas-Nestlé,-criar-foodlists-e-receber-dicas?"):
        link = "https://www.receitasnestle.com.br/categorias/" + aux_link
        print(link)
        get_url = link
        second_execute = requests.get(get_url)
        introduction = BeautifulSoup(second_execute.text, 'html.parser')
        receitas = introduction.findAll('div', attrs={'class': 'text'})
        for receita in receitas:
            titulo = receita.find('h2', attrs={'class': 'title'})
            aux_link = str(titulo.text)
            aux_link = aux_link.replace(' ','-')
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
                if(link != 'https://www.receitasnestle.com.br/receitas/' and link != 'https://www.receitasnestle.com.br/receitas/Origem,-história-e-curiosidades'):
                    #print('titulo:', titulo.text)
                    #print('\nLink:', link_two)
                    #print('\nIngredientes:', ingred)
                    #print('\nModo de Preparo:', metd)
                    print('\n\n')
                    name_archive = str(counter_archive) + '.txt'
                    print(name_archive)
                    counter_archive += 1
                    with open(name_archive, 'a') as title_archive:
                            auxTitle = titulo.text
                            title_archive.write((auxTitle) + ',')
                    with open(name_archive, 'a') as ingre_archive:
                            ingre_archive.write((ingred) + ',')
                    with open(name_archive, 'a') as preparo_archive:
                            preparo_archive.write((metd))     