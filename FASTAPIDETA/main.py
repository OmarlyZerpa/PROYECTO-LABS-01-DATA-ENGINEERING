#Importamos las librerias necesarias
import pandas as pd
import numpy as np

#Importamos la bases de datos a usar
canales= pd.read_csv(r"Datasets/canales.csv")

##Creeamos la aplicacion api usando FastAPI
from fastapi import FastAPI
app = FastAPI() # nombre de la aplicacion

#http://127.0.0.1:8000 Pueto donde se encuentra la aplicacion api

@app.get('/') #Primera ruta
def get_bienvenida():
    return 'Bienvenidos, en esta aplicacion encontras las diferentes peliculas/series de las plataformas de amazon, disney, hulu y netflix. realiza tus consuta'

##Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get('/keyword/{plataforma}/{keyword}') #Segunda ruta
def get_word_count(plataforma, keyword):
    canal= canales[canales['id'].str.contains(plataforma[0], case= False)]
    cantidad= canal[canal['title'].str.contains(keyword, case= False)]
    return {'plataforma':plataforma, 'cantidad':len(cantidad)}

##Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get('/score/{plataforma}/{puntaje}/{anio}') # tercera ruta
def get_score_count(plataforma, puntaje: int, anio: int):
    canal= canales[canales['id'].str.contains(plataforma[0], case= False)]
    cantidad= canal[(canal.score > puntaje) & (canal.release_year == anio)& (canal.type== 'movie')]
    return {'plataforma':plataforma, 'cantidad':len(cantidad)}

##La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
@app.get('/segundapeliculaconmayorscore/{plataforma}') # cuarta ruta
def get_second_score(plataforma):
    canal= canales[canales['id'].str.contains(plataforma[0], case= False)]
    canal=canal.sort_values('title', ascending=True)
    filtro= canal[(canal.type== 'movie') & (canal['score']==canal['score'].max())]
    segundo_title= filtro.iloc[1]['title']
    segundo_score= filtro.iloc[1]['score']
    respuesta= pd.DataFrame({'title':[segundo_title], 'score':[segundo_score]}).T.to_dict()
    return respuesta

##Película que más duró según año, plataforma y tipo de duración
@app.get('/peliculaconmayorduracion/{plataforma}/{tipo_de_duracion}/{anio}') # quinta ruta
def get_longest(plataforma, tipo_de_duracion, anio: int):
    canal= canales[canales['id'].str.contains(plataforma[0], case= False)]
    filtro= canal[(canal.release_year == anio) & (canal.type== 'movie') & (canal.duration_type == tipo_de_duracion)]
    duracion= filtro[['title','duration_int', 'duration_type']].loc[filtro.duration_int.idxmax()] 
    pelicula= duracion.T.to_dict()
    return pelicula

##Cantidad de series y películas por rating
@app.get('/rating/{rating}') #sexta ruta
def get_rating_count(rating):
    cantidad= canales[canales["rating"]== rating]
    return {'rating':rating, 'cantidad':len(cantidad)}

##Se obtuvo la ruta/direccion/link de la API con DETA 
##        "name": "FASTAPIDETA",
        ##"id": "fec4e67d-c894-4c44-891c-df2f53f20f92",
        ##"project": "e0bnmq7o",
        ##"runtime": "python3.9",
        ##"endpoint": "https://1aj8la.deta.dev",
        ##"region": "sa-east-1",
        ##"visor": "disabled",
        ##"http_auth": "disabled"
## Se autorizo al publico con deta auth disable
## Para realizar consultas a la API ENTRAR AL SIGUIENTE LINK: https://1aj8la.deta.dev
