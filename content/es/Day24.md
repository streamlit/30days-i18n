# st.cache

`st.cache` le permite optimizar el rendimiento de su aplicación Streamlit.

Streamlit proporciona un mecanismo de almacenamiento en caché que permite que su aplicación siga funcionando correctamente incluso cuando carga datos de la web, manipula grandes conjuntos de datos o realiza cálculos costosos. Esto se hace con el decorador `@st.cache`.

Cuando marca una función con el decorador @st.cache, le dice a Streamlit que cada vez que se llama a la función, debe verificar algunas cosas:

1. Los parámetros con los que llamaste a la función
2. El valor de cualquier variable externa utilizada en la función
3. El cuerpo de la función
4. El cuerpo de cualquier función utilizada dentro de la función en caché

Si esta es la primera vez que Streamlit ve estos cuatro componentes con estos valores exactos y en esta combinación y orden exactos, ejecuta la función y almacena el resultado en un caché local. Luego, la próxima vez que se llame a la función almacenada en caché, si ninguno de estos componentes cambió, Streamlit simplemente omitirá la ejecución de la función por completo y, en su lugar, devolverá la salida previamente almacenada en el caché.

La forma en que Streamlit realiza un seguimiento de los cambios en estos componentes es a través del hash. Piense en la memoria caché como un almacén de clave-valor en memoria, donde la clave es un hash de todo lo anterior y el valor es el resultado real pasado por referencia.

Finalmente, `@st.cache` admite argumentos para configurar el comportamiento del caché. Puede encontrar más información sobre ellos en la referencia de nuestra API.

## Cómo utilizar?

Simplemente puede agregar el decorador `st.cache` en la línea anterior de una función que ha definido en su aplicación Streamlit. Vea el ejemplo a continuación.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## Código
Así es como se usa `st.cache`:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st`, así como otras librerías utilizadas, de la siguiente manera:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

A esto le sigue la creación de un título para la aplicación:
```python
st.title('Streamlit Cache')
```

A continuación, definiremos 2 funciones para generar un DataFrame grande donde la primera utiliza el decorador `st.cache` mientras que la segunda no:
```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

Finalmente, ejecutamos la función mientras cronometramos el tiempo de ejecución usando el comando `time()`.
```python
# Using cache
a0 = time()
st.subheader('Using st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

Observe cómo la primera ejecución puede proporcionar un tiempo de ejecución más o menos similar. Vuelva a cargar la aplicación y observe cómo cambia el tiempo de ejecución al usar el decorador `st.cache`. ¿Observó algún aumento de velocidad?

## Otras lecturas
- [Documentación de la API `st.cache`](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [Optimizar el rendimiento con `st.cache`](https://docs.streamlit.io/library/advanced-features/caching)
- [Primitivos de caché experimentales](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
