###  comienzo importando las librerias necesarias y carfgo el Dataframe para poder generar las consultas ##
from fastapi import FastAPI
from fastapi import Response
import pandas as pd
import numpy as np
import json

# import locale
# import ast
# from fastapi.responses import FileResponse


df = pd.read_csv("Datasets/Movies_ETL.csv")

app = FastAPI()

### genero los decoradores de fastAPI @app ###

# # mi ruta local es : http://127.0.0.1:8000
@app.get("/index/{nombre: str}")
def index():
    return  "Mateo Betancourt"

# PRIMERA CONSULTA
@app.get("peliculas_idioma/{idioma: str}")
def peliculas_idioma(idioma):
    consulta_idioma = df[df["spoken_languages"] == idioma]
    cantidad = consulta_idioma["spoken_languages"].shape[0]
    return {"Idioma ": idioma, "Cantidad_de_peliculas ": cantidad}

#SEGUNDA CONSULTA
@app.get("/peliculas_duracion/{pelicula: str}")
def peliculas_duracion(pelicula):
    consulta_peli = df[df["title"] == pelicula]
    duracion = consulta_peli["runtime"].values[0]
    anio = consulta_peli["release_year"].values[0]
    return {"La_Pelicula ": pelicula, "Tiene_una_duracion_en_minutos: ": str(duracion), "Año_de_estreno: ":str(anio)}

#TERCERA CONSULTA
@app.get("/franquicia/{franquicia: str}")
def franquicia(franquicia):
    cantidad = df[df["collection_name"] == franquicia]["revenue"].count()
    ganancia = df[df["collection_name"] == franquicia]["revenue"].sum()
    promedio = df[df["collection_name"] == franquicia]["revenue"].mean()
    return {"Franquicia: ": franquicia,"cantidad_de_peliculas: ":str(cantidad), "ganancia_total: ":str(ganancia), "ganancia_promedio: ":str(promedio)}

#CUARTA CONSULTA
@app.get("/peliculas_pais/{pais: str}")
def pelicula_pais(pais):
    df_filtro = df[df["production_countries"].apply(lambda x: pais in str(x))]
    cantidad_peliculas = df_filtro["production_countries"].count()
    return {"pais: ":pais, "cantidad: ":str(cantidad_peliculas)}

#QUINTA CONSULTA
@app.get("/productoras_exitosas/{productora: str}")
def productoras_exitosas(productora):
    filtro_produc = df[df["production_companies"].str.contains(productora, na=False)]
    if filtro_produc.empty:
        return "El valor que se ingreso es Nulo"
    total_ganancia = filtro_produc["revenue"].sum()
    total_peliculas = filtro_produc.shape[0]
    return {"productora": productora, "ganancia total": str(total_ganancia), "cantidad de peliculas": str(total_peliculas)} 

#SEXTA CONSULTA
@app.get("/get_director/{nombre_director: str}")
def get_director(nombre_director):
    df_director = df[df["director_name"].apply(lambda x: nombre_director in x if isinstance(x, (list, str)) else False)].head(5)
    total_ganacia = df_director["revenue"].sum()
    peliculas = []
    for index, row in df_director.iterrows():
        nombre = row["title"]
        fecha_lanzamiento = row["release_date"]
        retorno = row["return"]
        costo = row["budget"]
        ganancias = row["revenue"]
        peliculas.append({"nombre_pelicula":nombre, "fecha_lanzamiento: ": fecha_lanzamiento, "retorno: ": retorno, "costo_pelicula":costo, "ganancia_generada: ":ganancias})
    return { "nombre_director: ":nombre_director, "retorno_total: ": total_ganacia, "peliculas: " :peliculas}


################# MODELO MACHINE LEARNING ###################
 # importo las librerias que voy a utilizar para el modelo y cargo el archivo luego de realizar el EDA
from sklearn.metrics.pairwise import cosine_similarity
data = pd.read_csv('Datasets/Movies_ML.csv', low_memory=False)

#recorto el Dataframe que me arroja para que no quede muy pesado pero que funcione bien 
d = 5000
datos = data.head(d)

x = datos[["genres", "original_language", "popularity", "production_companies", "release_date", "runtime", "status", "vote_average", "return", "collection_name"]]

matris = cosine_similarity(x)

@app.get("/recomendacion/{titulo:str}")
def get_recomendacion(titulo):
    top_n=5
    indice_titulo = datos[datos["title"] == titulo].index[0]
    resultado_matris = matris[indice_titulo]
    indices = resultado_matris.argsort()[-top_n-1:-1][::-1]
    recomendacion = datos.loc[indices,"title"]
    recomendacion = recomendacion.values.tolist()
    return{"lista de peliculas recomnendada": str(recomendacion)}