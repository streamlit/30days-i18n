# st.button

`st.button` permite mostrar un botón.

## Que estamos construyendo?

Una simple aplicación que imprime condicionalmente diferentes mensajes dependiendo si el botón fue presionado o no.


Comportamiento de la aplicación:

1. Por defecto, la aplicación imprime `Goodbye`
2. Una vez que se hace click sobre el botón, la aplicación imprime `Why hello there`

## Demo app

La aplicación de Streamlit debería verse como la mostrada en el siguiente link:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## Código

Aquí tenemos el código para implementar la aplicación previamente mencionada:

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## Explicación linea por linea


Lo primero que tenemos que hacer cuando creamos una aplicación de Streamlit es comenzar importando la librería `streamlit` de la siguiente manera:

```python
import streamlit as st
```

Seguimos por crear un encabezado de texto para la aplicación:

```python
st.header('st.button')
```

Siguiente, vamos a usar los condicionales `if` y `else` para imprimir los correspondientes mensajes.

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

Como podemos ver en el anterior código, el comando `st.button()` admite el argumento `label` con el valor `Say hello`, el cual es el texto que el botón muestra.

El comando `st.write` es usado para imprimir mensajes tales como `Why hello there` o `Goodbye` dependiendo si el botón fue presionado o no, lo cual es implementado de la siguiente manera:


```python
st.write('Why hello there')
```

y

```python
st.write('Goodbye')
```

Es importante tener en cuenta que los `st.write` están colocados debajo de las condiciones `if` y `else` para realizar el mencionado proceso de mostrar mensajes alternativos.

## Siguientes pasos

Ahora que has creado la app localmente, es hora de desplegarla en [Streamlit Community Cloud](https://streamlit.io/cloud) como lo vamos a mencionar en un próximo desafío.

Como esta es la primer semana de tu desafío, nosotros proveemos el código completo (como es mostrado en el código anterior) y la solución (la app de ejemplo) dentro de esta web.

Avanzando en el próximo desafío, es recomendable que intentes implementar la Streamlit app por vos mismo.

No te preocupes si te trabas, tu siempre puedes tomar un vistazo a la solución. 

## Referencias

Lee acerca [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) en la documentación de Streamlit.
