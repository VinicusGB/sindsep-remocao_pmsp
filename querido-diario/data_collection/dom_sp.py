from datetime import date, datetime, timedelta
from os import getcwd, path, listdir, chdir
from tabula import read_pdf, environment_info, convert_into_by_batch
import datetime
import os
import fitz as fz
import tabula

dt_now = date.today()
year_edition_dom = dt_now.year - 1955
head_dom ='São Paulo, ' + str(year_edition_dom) + ' ('
if dt_now.weekday() == 0:
        dt_now = dt_now + timedelta(-2)
        dt_now = dt_now.strftime("%Y-%m-%d")
else:
        dt_now = dt_now.strftime("%Y-%m-%d")

BASE_DIR = os.getcwd()
DIR_DATA = os.path.join(BASE_DIR,'data\\3550308\\'+ str(dt_now))
os.chdir(DIR_DATA)
list_files_names = os.listdir(DIR_DATA)

print('BASE_DIR: ' + BASE_DIR)
print('DIR_DATA: ' + DIR_DATA)
print('Data de referência do DOM-SP: ' + dt_now)
print('Quantidade de páginas do DOM-SP: ' + str(len(list_files_names)))


print('Obtendo edição de: ' + list_files_names[0])
with fz.open(DIR_DATA +'\\'+ list_files_names[0]) as file:
        search_edition = ''
        for page in file:
                search_edition += page.get_text()

search_edition = search_edition[search_edition.find(head_dom):]
edition_dom = search_edition[search_edition.find('(')+1:search_edition.find(')')]
head_dom ='São Paulo, ' + str(year_edition_dom) + ' (' + edition_dom + ')'
print('Cabeçalho: ' + head_dom)


contexts = ''
for file_name in list_files_names:
        print('Obtendo conteúdo de: ' + file_name)
        with fz.open(DIR_DATA +'\\'+ file_name) as file:
                context = ""
                for page in file:
                        context += '<pag>\n'+ page.get_text() + '</pag>\n'
                
                odd_page = "São Paulo, " + str(year_edition_dom) + " (" + str(edition_dom) + ") – "
                even_page = " – São Paulo, " + str(year_edition_dom) + " (" + str(edition_dom) + ")"

                if  context.find(odd_page) != -1:
                        num_page = context[context.find(odd_page)+21:context.find('\n',context.find(odd_page))]
                elif context.find(even_page) != -1:
                        num_page = context[context.find('\n',context.find(even_page)-5)+1:context.find(even_page)]
                elif context.find("D.O.C.; " + head_dom) != -1:
                        num_page = str(len(list_files_names))
                elif context.find("Ano "+ str(year_edition_dom)) != -1:
                        num_page = '1'
                else:
                        num_page = ''

        contexts += context
        os.rename(file_name, "pg_" + num_page.zfill(3) + "-" + file_name)

list_files_names = os.listdir(DIR_DATA)
list_files_names.sort()

contexts = ''
for file_name in list_files_names:
        print('Obtendo conteúdo de: ' + file_name)
        with fz.open(DIR_DATA +'\\'+ file_name) as file:
                context = ""
                for page in file:
                        context += '<pag>\n'+ page.get_text() + '</pag>'
                
                odd_page = "São Paulo, " + str(year_edition_dom) + " (" + str(edition_dom) + ") – "
                even_page = " – São Paulo, " + str(year_edition_dom) + " (" + str(edition_dom) + ")"

                if  context.find(odd_page) != -1:
                        num_page = context[context.find(odd_page)+21:context.find('\n',context.find(odd_page))]
                elif context.find(even_page) != -1:
                        num_page = context[context.find('\n',context.find(even_page)-5)+1:context.find(even_page)]
                elif context.find("D.O.C.; " + head_dom) != -1:
                        num_page = str(len(list_files_names))
                elif context.find("Ano "+ str(year_edition_dom)) != -1:
                        num_page = '1'
                else:
                        num_page = ''

        contexts += num_page + context

with open("..\\DOM_SP-"+ str(year_edition_dom) + "_" + str(edition_dom) + "_" + str(len(list_files_names)) + "_" + str(dt_now)+".txt","w",encoding='utf-8') as output_file:
    output_file.write(contexts)

area_text = [[42.849,28.172,1209.134,215.329],[42.849,216.314,1210.119,393.621],[42.849,395.591,1210.119,574.868],[42.849,576.838,1207.164,760.055]]

tabula.convert_into_by_batch(DIR_DATA,output_format="csv",area=area_text,pages="all")
