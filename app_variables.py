path_AnnualTicketSales = './data/hollywood/AnnualTicketSales.csv'
path_HighestGrossers = './data/hollywood/HighestGrossers.csv'
path_PopularCreativeTypes = './data/hollywood/PopularCreativeTypes.csv'
path_TopDistributors = './data/hollywood/TopDistributors.csv'
path_TopGenres = './data/hollywood/TopGenres.csv'
path_TopGrossingRatings = './data/hollywood/TopGrossingRatings.csv'
path_TopGrossingSources = './data/hollywood/TopGrossingSources.csv'
path_TopProductionMethods = './data/hollywood/TopProductionMethods.csv'
path_WideReleasesCount = './data/hollywood/WideReleasesCount.csv'

intro = '''
# Hollywood Theatrical Market Synopsis 1995 to 2021 EDA
This Streamlit app aims to provide data insight for [Hollywood Theatrical Market Synopsis 1995 to 2021](https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021) hosted on [Kaggle](https://www.kaggle.com/).
'''


intro_context = '''
## Introduction
##### [H&M Group](https://www.hmgroup.com/) is a family of brands and businesses with 53 online markets and approximately 4,850 stores. Our online store offers shoppers an extensive selection of products to browse through. But with too many choices, customers might not quickly find what interests them or what they are looking for, and ultimately, they might not make a purchase. To enhance the shopping experience, product recommendations are key. More importantly, helping customers make the right choices also has a positive implications for sustainability, as it reduces returns, and thereby minimizes emissions from transportation.  
##### In this competition, H&M Group invites you to develop product recommendations based on data from previous transactions, as well as from customer and product meta data. The available meta data spans from simple data, such as garment type and customer age, to text data from product descriptions, to image data from garment images.  
##### There are no preconceptions on what information that may be useful – that is for you to find out. If you want to investigate a categorical data type algorithm, or dive into NLP and image processing deep learning, that is up to you.

###### cited from [Kaggle](https://www.kaggle.com/c/h-and-m-personalized-fashion-recommendations)
'''

dataset_intro = '''
There are 9 datasets:
1. AnnualTicketSales  
2. HighestGrossers  
3. PopularCreativeTypes  
4. TopDistributors
5. TopGenres
6. TopGrossingRatings
7. TopGrossingSources
8. TopProductionMethods
9. WideReleasesCount.  
  
## Below presents a glance into all the datasets
'''


variables_intro = '''
## **1. Variables que puntúan las películas**
En el portal de IMDb disponemos de 3 valoraciones para cada película:
- **IMDb Rating** (asociado al número de votos para este rating)
- **Metascore**
- Popularity
#### IMDb Rating
Esta es el promedio de las valoraciones que hacen los usuarios del portal IMDb para cada película. El rango de esta puntuación se encuentra entre 1 y 10.
Asumimos que el rating es un dato que sigue variando, sigue disponible para que el usuario vote. No disponemos del rating que había cuando la película estaba exhibiéndose en las salas, pero en esa época es cuando más votaciones recibe. Es posible que cada película, tras la emisión por televisión, reciba otra ola de votaciones, pero es cierto que al ser las películas más recientes de 2019 estos impactos ya habrán afectado a los datos recogidos ahora, en julio de 2021.
#### Metascore
Metacritic es un portal web que recopila críticas de películas, series, programas de televisión, videojuegos y libros. Metacritic ha desarrollado un algoritmo que convierte cada crítica en un porcentaje y hace una media ponderada para tener en cuenta el caché de la publicación. Esto da como resultado el metascore, una puntuación del 0 al 100 para cada producto, en nuestro caso de estudio, para cada película. 
El metascore es habitualmente utilizado por los medios como referencia para medir la recepción de la crítica.
En la página de IMDb aparece este índice para cada película y en este estudio lo tomaremos en cuenta como referencia para evaluar la valoración que hace la crítica de las películas.
#### Popularity
Dato que vamos a descartar porque es muy volátil, se mantiene en cambio constante y, al no disponer de un histórico, no guarda relación temporal con la recaudación.
## **2. Variables económicas**
En IMDb tenemos 4 variables de tipo económico:
- Presupuesto
- Recaudación del primer fin de semana en EEUU y Canadá
- Recaudación en EEUU y Canadá
- Recaudación mundial
Para este estudio necesitaremos la información de presupuesto y recaudación. Esta decisión ha propiciado prescindir de muchos registros porque solo 1.553 películas tenían estas 4 variables.
Y además crearemos otras dos nuevas, que serán Beneficio y Retorno de la Inversión, con la siguiente información:
    Beneficio = Recaudación mundial - Presupuesto
    ROI = (Recaudación mundial - Presupuesto) / Presupuesto
Finalmente, las variables económicas escogidas para cada película son:
- **Presupuesto**
- **Recaudación** (mundial)
- **Beneficio**
- **ROI**
'''


variables_intro_rating = '''
Visualizando la distribución del Rating de IMDb podemos observar que los usuarios tienden a aprobar las películas. Así, la media y la mediana se situan en `6,37` y `6,4` puntos respectivamente. El valor mínimo es de `1,40` y el máximo de `8,6`, por lo que vemos que los usuarios no dejan de ser exigentes y el promedio de la puntuación máxima no se acerca a la puntuación máxima posible: `10`.
'''

variables_intro_metascore = '''
Podemos observar que las puntuaciones de la crítica son más dispersas que el Rating de usuarios, e incluso llegan a otorgar las puntuaciones míninma y máxima de `1` y `100` puntos. Seguramente esto se deba a cómo está desarrollado el algoritmo de Metacritic que otorga estas puntuaciones de una manera automatizada. Dentro de nuestro dataset la película con el máximo Metascore es 'Boyhood' de 2014 que, sorprendentemente, consigue la puntuacion perfecta: `100`.
'''

variables_intro_presupuesto = '''
Aunque en este período de tiempo tenemos unas de las películas más caras de la historia del cine, vemos que la mayoría se situan por debajo de los 13,5 millones de dólares. 'Vengadores: Endgagme' es la película con mayor presupuesto con 378 millones de dólares.
'''


variables_intro_recaudacion = '''
'''

variables_intro_beneficio = '''
Nuevamente, la película con el máximo valor o mayor beneficio es 'Vengadores: Endgame' con más de 2.400 millones de dólares. Sin embargo, vemos que un gran porcentaje de las películas dan pérdidas con valores negativos para el beneficio. El 25% de las películas tienen una pérdidas de al menos 3 millones de dólares, y la mediana se sitúa en 4,3 millones de dólares.
'''

variables_intro_roi = '''
El ROI, al tratarse de una variable independiente del presupuesto de la película, ya nos muestra un listado de películas totalmente diferente en lo alto de la tabla. En este caso hemos tenido que limitar el listado a películas con un valor máximo de 30 ya que detectamos que había datos no válidos en algunos casos. Sorprendente la cantidad de películas de terror o thriller en las primeras posiciones.
'''