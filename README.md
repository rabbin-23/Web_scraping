Creado por Elias Abiram Torres Vazquez
# Web_scraping
En este ejercicio se realiza la extraccion del nombre y el precio del producto Playstation 5 en la plataforma  https://www.mercadolibre.com
con las siguientes condiciones:
- Seleccionar México como país
- Buscar el termino PlaySation 5
- Filtrar por la ciudad de México
- Ordenar de mayor a menor precio

El resultado se muestra en consola.

Requisitos:
-Tener instalado Python
-Asegurarse de tener instalada la libreria re
-Asegurarse de tener instalada la libreria requests
-Tener conexión a internet para acceder a los datos del sitio

Proceso para ejecutar:
Una vez copiado el codigo a la IDE que se prefiera,se guarda y se ejecuta de la siguiente forma en la consola(primero ingresar a la carpeta donde se guardó el archivo):
python ejercicioPrueba.py

nota:
El codigo funciona a partir de expresiones regulares, la libreria request nos permite acceder al codigo HTML de la pagina, en ese codigo podemos encontrar el nombre y precio de los productos, la tarea es encontrar un patrón que nos permita identificar exactamente el nombre y precio entre todo el codigo, una vez encontrado debemos pensar en la expresión regular que valide la estructura que tiene el nombre y el precio, esto se realiza mediante la libreria re. Despues de haber encontrado tanto los nombres como los precios procedemos a eliminar la impresion del patron remplazando con comillas(""), se realiza mediante una iteracion en la lista de nombres y precios. Al final concatenamos ambas listas y listo.
