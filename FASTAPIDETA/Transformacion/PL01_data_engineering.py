#Importamos las librerias necesarias
import pandas as pd
import numpy as np

#Importamos la bases de datos a usar
amazon= pd.read_csv(r"Datasets/amazon_prime_titles-score.csv")
disney= pd.read_csv(r"Datasets/disney_plus_titles-score.csv")
hulu= pd.read_csv(r"Datasets/hulu_titles-score (2).csv")
netflix= pd.read_csv(r"Datasets/netflix_titles-score.csv")

#Cambiamos el tipo de formato de la columna date_added
amazon['date_added'] = pd.to_datetime(amazon['date_added'], infer_datetime_format=True, errors='coerce')
disney['date_added'] = pd.to_datetime(disney['date_added'], infer_datetime_format=True, errors='coerce')
hulu['date_added'] = pd.to_datetime(hulu['date_added'], infer_datetime_format=True, errors='coerce')
hulu['cast'] = hulu['cast'].astype('str') #Cambiamos el formato de cast en el csv de hulu
netflix['date_added'] = pd.to_datetime(netflix['date_added'], infer_datetime_format=True, errors='coerce')

#Aplicamos las transformaciones respectivas

##Se genera el campo id, se compondra de la primera letra de la plataforma seguido del show_id presente en los dataset
amazon["id"]= 'a'+ amazon["show_id"]
amazon['id'] = amazon['id'].astype('str')
disney["id"]= 'd'+ disney["show_id"]
disney['id'] = disney['id'].astype('str')
hulu["id"]= 'h'+ hulu["show_id"]
hulu['id'] = hulu['id'].astype('str')
netflix["id"]= 'n'+ netflix["show_id"]
netflix['id'] = netflix['id'].astype('str')

##Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” 
##(corresponde al maturity rating: “general for all audiences”)

amazon.fillna({'rating':'G'}, inplace= True)
disney.fillna({'rating':'G'}, inplace= True)
hulu.fillna({'rating':'G'}, inplace= True)
netflix.fillna({'rating':'G'}, inplace= True)

##De haber fechas, deberán tener el formato **`AAAA-mm-dd`**
##Esto ya se modifico al cambiar el tipo de formato de las fechas usando datetime.

##Los campos de texto deberán estar en **minúsculas**, sin excepciones
amazon['id'] = amazon['id'].str.lower()
amazon['type'] = amazon['type'].str.lower()
amazon['title'] = amazon['title'].str.lower()
amazon['director'] = amazon['director'].str.lower()
amazon['cast'] = amazon['cast'].str.lower()
amazon['country'] = amazon['country'].str.lower()
amazon['rating'] = amazon['rating'].str.lower()
amazon['listed_in'] = amazon['listed_in'].str.lower()
amazon['description'] = amazon['description'].str.lower()

disney['id'] = disney['id'].str.lower()
disney['type'] = disney['type'].str.lower()
disney['title'] = disney['title'].str.lower()
disney['director'] = disney['director'].str.lower()
disney['cast'] = disney['cast'].str.lower()
disney['country'] = disney['country'].str.lower()
disney['rating'] = disney['rating'].str.lower()
disney['listed_in'] = disney['listed_in'].str.lower()
disney['description'] = disney['description'].str.lower()

hulu['id'] = hulu['id'].str.lower()
hulu['type'] = hulu['type'].str.lower()
hulu['title'] = hulu['title'].str.lower()
hulu['director'] = hulu['director'].str.lower()
hulu['cast'] = hulu['cast'].str.lower()
hulu['country'] = hulu['country'].str.lower()
hulu['rating'] = hulu['rating'].str.lower()
hulu['listed_in'] = hulu['listed_in'].str.lower()
hulu['description'] = hulu['description'].str.lower()

netflix['id'] = netflix['id'].str.lower()
netflix['type'] = netflix['type'].str.lower()
netflix['title'] = netflix['title'].str.lower()
netflix['director'] = netflix['director'].str.lower()
netflix['cast'] = netflix['cast'].str.lower()
netflix['country'] = netflix['country'].str.lower()
netflix['rating'] = netflix['rating'].str.lower()
netflix['listed_in'] = netflix['listed_in'].str.lower()
netflix['description'] = netflix['description'].str.lower()

##* El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. 
##El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

amazon[['duration_int', 'duration_type']] = amazon['duration'].str.split(' ', expand=True)
amazon['duration_type'] = amazon['duration_type'].str.lower()
amazon['duration_int'] = amazon['duration_int'].astype('int64')
amazon['duration_type'] =  amazon['duration_type'].replace('seasons', 'season', regex=True)

disney[['duration_int', 'duration_type']] = disney['duration'].str.split(' ', expand=True)
disney['duration_type'] = disney['duration_type'].str.lower()
disney['duration_int'] = disney['duration_int'].astype('int64')
disney['duration_type'] =  disney['duration_type'].replace('seasons', 'season', regex=True)

hulu[['duration_int', 'duration_type']] = hulu['duration'].str.split(' ', expand=True)
hulu['duration_type'] = hulu['duration_type'].str.lower()
hulu['duration_int'] = hulu['duration_int'].astype(float).astype('Int64')
hulu['duration_type'] =  hulu['duration_type'].replace('seasons', 'season', regex=True)

netflix[['duration_int', 'duration_type']] = netflix['duration'].str.split(' ', expand=True)
netflix['duration_type'] = netflix['duration_type'].str.lower()
netflix['duration_int'] = netflix['duration_int'].astype(float).astype('Int64')
netflix['duration_type'] =  netflix['duration_type'].replace('seasons', 'season', regex=True)

##Ordenando las columnas de las tablas (dataset)
amazon= amazon[['id','show_id','type','title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'duration_int', 'duration_type', 'listed_in', 'description', 'score']]
disney= disney[['id','show_id','type','title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'duration_int', 'duration_type', 'listed_in', 'description', 'score']]
hulu= hulu[['id','show_id','type','title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'duration_int', 'duration_type', 'listed_in', 'description', 'score']]
netflix= netflix[['id','show_id','type','title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'duration_int', 'duration_type', 'listed_in', 'description', 'score']]

##Agrupando las tablas o dataset en uno solo
canales_streaming= pd.concat([amazon, disney, hulu, netflix], axis=0)

##Creo un dataset con estos datos agrupados
canales_streaming.to_csv('canales.csv', index= False)