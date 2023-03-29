# st.line_chart

`st.line_chart` muestra un gráfico de líneas.

Esto es un syntax-sugar en torno a `st.altair_chart`. La principal diferencia es que este comando utiliza la columna y los índices propios de los datos para determinar las especificaciones del gráfico. Como resultado, esto es más fácil de usar para muchos escenarios, mientras que es menos personalizable.

Si `st.line_chart` no adivina la especificación de datos correctamente, intente especificar su gráfico deseado usando `st.altair_chart`.

## Que estamos construyendo?

Una aplicación sencilla para mostrar un gráfico de líneas.

Comportamiento de la aplicación:
1. Cree un DataFrame `Pandas` a partir de números generados aleatoriamente usando `NumPy`.
2. Cree y muestre el gráfico de líneas mediante el comando `st.line_chart()`.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## Codigo
Aquí se explica cómo usar [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart):
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st`, así como otras de la siguiente manera:
```python
import streamlit as st
import pandas as pd
import numpy as np
```

A continuación, creamos un encabezado para la aplicación:
```python
st.header('Line chart')
```

Luego, creamos un DataFrame de números generados aleatoriamente que contiene 3 columnas.
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

Finalmente, se crea un gráfico de líneas usando `st.line_chart()` con el DataFrame almacenado en la variable `chart_data` como datos de entrada:
```python
st.line_chart(chart_data)
```

## Otras lecturas
Obtenga más información sobre el siguiente comando Streamlit relacionado en el que se basa [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart):
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
