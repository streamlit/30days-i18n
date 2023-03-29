# Personalización del tema de las aplicaciones Streamlit

Podemos personalizar el tema ajustando los parámetros en `config.toml`, que es un archivo de configuración almacenado en la misma carpeta que la aplicación en la carpeta `.streamlit`.

## What we're building?

Una simple aplicación que muestra el resultado de la personalización de nuestro tema. Esto fue posible gracias a la personalización de código HTML HEX dentro del archivo [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml).

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## Código
Aquí está el código del archivo [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py):
```python
import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Aquí está el código del archivo [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml):
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

A esto le sigue la creación de un título para la aplicación:
```python
st.title('Theming with config.toml')
```

A continuación, vamos a mostrar el contenido del archivo `.streamlit/config.toml` por medio de `st.write` seguido por el código real via `st.code`:
```python
st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

Finalmente, estamos creando un control deslizante en la barra lateral seguido de mostrar el número seleccionado:
```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Ahora echemos un vistazo a los colores personalizados que hemos usado en esta aplicación, que se especifica en el archivo `.streamlit/config.toml`:
- `primaryColor="#F39C12"` - Esto establece el color primario en naranja. Observe los colores naranjas en el control deslizante.
- `backgroundColor="#2E86C1"` - Esto establece el color de fondo en azul. Observe que el panel principal tiene un color de fondo azul.
- `secundarioBackgroundColor="#AED6F1"` - Esto establece el color de fondo secundario en gris oscuro. Observe el color de fondo gris de la barra lateral y el color de fondo del cuadro de código en el panel principal.
- `textColor="#FFFFFF"` - El color del texto se establece en blanco.
- `font="monospace"` - Esto establece la fuente en monoespaciado.


## Otras lecturas
- [Tematización](https://docs.streamlit.io/library/advanced-features/theming)
- [Códigos de color HTML](https://htmlcolorcodes.com/) es una gran herramienta para seleccionar colores de interés.
