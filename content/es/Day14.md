# Componentes de Streamlit

Los componentes son módulos Python de terceros que amplían lo que es posible con Streamlit [[1](https://docs.streamlit.io/library/components)].

## Que componentes están disponibles?

Hay varias docenas de componentes de Streamlit que aparecen en el sitio web de Streamlit [[2](https://streamlit.io/components)].

Fanilo (un creador de Streamlit) seleccionó una increíble lista de componentes de Streamlit en una publicación wiki [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)] que enumera alrededor de 85 componentes a partir de abril de 2022.

## Cómo utilizar?

Los componentes Streamlit están a solo un pip de distancia.

En este tutorial, comencemos a usar el componente `streamlit_pandas_profiling` [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

#### Instalar el componente 

```bash
pip install streamlit_pandas_profiling
```

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## Código
Aquí se explica cómo crear una aplicación Streamlit usando un componente:
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la biblioteca `streamlit` como `st`, así como otras bibliotecas utilizadas en la aplicación:
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

A esto le sigue la creación de un texto de encabezado para la aplicación:
```python
st.header('`streamlit_pandas_profiling`')
```

A continuación, cargamos el conjunto de datos de Penguins usando el comando `read_csv` de `pandas`.
```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

Finalmente, el informe de pandas se genera a través del comando `profile_report()` y se muestra usando `st_profile_report`:
```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Fabricación de sus propios componentes

Si está interesado en crear su propio componente, consulte los siguientes recursos:
- [Crear un componente](https://docs.streamlit.io/library/components/create)
- [Publicar un componente](https://docs.streamlit.io/library/components/publish)
- [API de componentes](https://docs.streamlit.io/library/components/components-api)
- [Publicación de blog sobre componentes](https://blog.streamlit.io/introducing-streamlit-components/)

Alternativamente, si prefiere aprender usando videos, nuestro ingeniero Tim Conkling ha creado algunos tutoriales increíbles:
- [Cómo construir un componente Streamlit | Parte 1: configuración y arquitectura](https://youtu.be/BuD3gILJW-Q)
- [Cómo construir un componente Streamlit | Parte 2: Parte 2: Hacer un control deslizante](https://youtu.be/QjccJl_7Jco)

## Más lecturas sobre Componentes
1. [Componentes Streamlit - Documentación API](https://docs.streamlit.io/library/components)
2. [Componentes destacados de Streamlit] (https://streamlit.io/components)
3. [Componentes Streamlit - Seguimiento de la comunidad](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)
