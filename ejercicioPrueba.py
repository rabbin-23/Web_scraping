import re
import requests

#sitio web al que queremos acceder
sitioWeb="https://listado.mercadolibre.com.mx/consolas-videojuegos/consolas/nuevo-en-distrito-federal/playstation-5-nuevo_OrderId_PRICE*DESC_NoIndex_True"
resultado= requests.get(sitioWeb)
#se guarda el contenido html de la pagina
content=resultado.text
#se encunetra el patron y se genera la expresion regular para filtrar los nombre
regex_nombre = r"ui-search-item__title\"\>[\w.\s]+[\w./w.\s]*[\w. + \w.\s]*[\w.\-\w.\s]*[^<]"  
nombres= re.findall(regex_nombre, str(content))           

#se encunetra el patron y se genera la expresion regular para filtrar los precios
regex_precio = r"<span class=\"andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript\" style=\"font-size:24px\" role=\"img\" aria-label=\"[\w.\s\w.]+[^\"]"
precios= re.findall(regex_precio, str(content))

lista_nombres_final=[]
for i in nombres:
    #se reemplaza la cadena del patron con comillas
    nombre= i.replace("ui-search-item__title\"", "")
    #los nuevos nombres se guardan en una nueva lista
    lista_nombres_final.append(nombre)


lista_precios_final=[]
for i in precios:
    #se reemplaza la cadena del patron con comillas
    precio= i.replace("<span class=\"andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript\" style=\"font-size:24px\" role=\"img\" aria-label=\"", "")
    #los nuevos precios se guardan en una nueva lista
    lista_precios_final.append(precio)
#se imprimen los primeros 5 nombres con su respectivo precio
for i in range(5):
    print(lista_nombres_final[i] +" -------- $" + lista_precios_final[i]) 




