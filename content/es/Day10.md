# st.selectbox

`st.selectbox` permite la visualización de un componente de selección.

## Que estamos construyendo?

Una sencilla aplicación que pregunta al usuario cuál es su color favorito.

Comportamiento de la aplicación:
1. El usuario selecciona un color
2. La aplicación imprime el color seleccionado

## Demo app
La aplicación Streamlit implementada debería parecerse a la que se muestra en el siguiente enlace:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## Codigo
Aquí está el código para implementar la aplicación mencionada anteriormente:
```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

A esto le sigue la creación de un texto de encabezado para la aplicación:
```python
st.header('st.selectbox')
```

A continuación, crearemos una variable llamada `option` que aceptará la entrada del usuario a través del comando "st.selectbox()".

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```
Como podemos ver en el cuadro de código anterior, el comando `st.selectbox()` acepta 2 argumentos:
1. El texto que va encima del componente de selección, es decir, `'What is your favorite color?'`
2. Los valores posibles para seleccionar `('Blue', 'Red', 'Green')`

Finalmente, imprimiremos el color seleccionado de la siguiente manera:
```python
st.write('Your favorite color is ', option)
```

## Próximos pasos
Ahora que ha creado la aplicación Streamlit localmente, es hora de implementarla en [Streamlit Community Cloud](https://streamlit.io/cloud).

## Referencias
Más información sobre [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)
