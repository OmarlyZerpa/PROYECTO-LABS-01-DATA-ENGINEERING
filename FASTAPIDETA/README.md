<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# **PROYECTO INDIVIDUAL Nº1** `</h1>`

# **`Data Engineering`**`</h1>`

# **`Omarly Zerpa`**`</h1>` `</h1>`

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

¡Bienvenidos al primer proyecto individual de la etapa de labs de HENRY! En esta ocasión, se hizo un trabajo situándose en el rol de un ***Data Engineer***.

<hr>

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

Se debe crear una  `Application Programming Interface` , la cual es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles que permiten por ejemplo, crear pipelines facilitando mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

La Api se desarrollara con **FastAPI**, esta es una web framework moderna y de alto rendimiento para construir APIs con Python.

<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

## Rol a desarrollar

Como parte del equipo de data de una empresa, el área de análisis de datos solicita al área de Data Engineering ciertos requerimientos para el óptimo desarrollo de sus actividades. Para ello se  elaboraron las *transformaciones* requeridas y se disponibilizaron los datos mediante la *elaboración y ejecución de una API*.

## **Requerimientos de aprobación (transformaciones realizadas)**

Se realizaron las siguientes transformaciones para los datos(dataset proporcionados en la carpeta Datasets los cuales tiene informacion de peliculas y series de las diferentes plataformas como, amazon, disney, hulu, netflix) para esto se trabajo con las librerias Pandas:

+ Se cambio el tipo de formato de la columna date_added de todos los csv a datetime, ademas en el csv de hulu se cambio el formato de cast a str.
+ Se genero el campo **`id`**: Cada id se compone de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`)**
+ Los valores nulos del campo rating se reemplazaron por el string “**`G`**” (corresponde al maturity rating: “general for all audiences".
+ De haber fechas, deberán tener el formato `AAAA-mm-dd.` Esto ya se modifico al cambiar el tipo de formato de las fechas usando datetime.
+ Todos los campos de texto de modificaron a **minúsculas**, sin ninguna excepcion.
+ El campo ***duration*** se convertio en dos campos: **`duration_int`** y **`duration_type`**. El primero es un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas). En el campo duration_type se remplazo la palabra seasons por season.
+ Se ordenaron las columnas de las tablas de los respectivos dataset.
+ Se unifico en un solo csv estas transformaciones, dicho documento se encuentra en la carpeta Dataset con el nombre de "canales".

Estas transformaciones se encuentran enn la carpeta Transformaciones en el documento "PL01_data_engineering.py".

<br/>

Para el **desarrollo de la API** se disponibilizaron los datos de la empresa y se realizaron la consultas usando el framework ***FastAPI***. Las consultas fueron las siguientes:

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
+ Película que más duró según año, plataforma y tipo de duración
+ Cantidad de series y películas por rating

  ** Estas consultas se detallaron en el documento main.py** se obtuvo el siguiente Puerto  http://127.0.0.1:8000 donde se encuentra la aplicacion api para realizar las consultas. las cuales son:
+ /keyword/{plataforma}/{keyword}
+ /score/{plataforma}/{puntaje}/{anio}
+ /segundapeliculaconmayorscore/{plataforma}
+ /peliculaconmayorduracion/{plataforma}/{tipo_de_duracion}/{anio}
+ /rating/{rating}

Para el **Deployment** se uso [Deta](https://www.deta.sh/?ref=fastapi) (el cual es el usado por la empresa, y este no necesita dockerizacion) para realizar el deploy de sus aplicaciones.

* De alli se obtuvo  la ruta/direccion/link de la API:

  "name": "FASTAPIDETA",

  "id": "fec4e67d-c894-4c44-891c-df2f53f20f92",

  "project": "e0bnmq7o",

  "runtime": "python3.9",

  "endpoint": "https://1aj8la.deta.dev",

  "region": "sa-east-1",

  "visor": "disabled",

  "http_auth": "disabled"

Se autorizo al publico con deta auth disable, Para realizar **consultas** a la **API ENTRAR AL SIGUIENTE LINK**: https://1aj8la.deta.dev, alli puede realizar las consultas vistas en FastAPI.

1. https://1aj8la.deta.dev/keyword/{plataforma}/{keyword} ---> Ejemplo: https://1aj8la.deta.dev/keyword/netflix/love
2. https://1aj8la.deta.dev/score/{plataforma}/{puntaje}/{anio} ---> Ejemplo: https://1aj8la.deta.dev/score/netflix/85/2010
3. https://1aj8la.deta.dev/segundapeliculaconmayorscore/{plataforma} ---> Ejemplo: https://1aj8la.deta.dev/segundapeliculaconmayorscore/amazon
4. https://1aj8la.deta.dev/peliculaconmayorduracion/{plataforma}/{tipo_de_duracion}/{anio} ---> Ejemplo: https://1aj8la.deta.dev/peliculaconmayorduracion/netflix/min/2016
5. https://1aj8la.deta.dev/rating/{rating} ---> Ejemplo: https://1aj8la.deta.dev/rating/18+

`<br/>`

<br/>

**`Video`**: El Tech Lead que le delegó esta tarea quiere darle un feedback sobre el trabajo realizado. Se realizo un video, el cual se subio a la plataforma Google Drive, link(https://drive.google.com/drive/folders/1h3gp89148ZQQSTea91TygMas0f-LMC3d?usp=sharing) En el se sintetiza lo realizado en este proyecto individual. La duracion del mismo es de ***5 minutos, mostrandose las consultas requeridas en funcionamiento desde la API.***

<br/>

## **Criterios de evaluación**

**`Código`**: Prolijidad de código, uso de clases y/o funciones, en caso de ser necesario, código comentado.

**`Repositorio`**: Nombres de archivo adecuados, uso de carpetas para ordenar los archivos, README.md presentando el proyecto y el trabajo realizado

**`Cumplimiento`** de los requerimientos de aprobación indicados en el apartado `Propuesta de trabajo`

NOTA: Recuerde entregar el link de acceso al video. Puede alojarse en YouTube, Drive o cualquier plataforma de almacenamiento. **Verificar que sea de acceso público**.

<br/>

## **Fuente de datos**

+ Podrán encontrar los archivos con datos en la carpeta Datasets, en este mismo repositorio.`<sup>`*`</sup>`
  `<br/>`
