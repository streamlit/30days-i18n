# st.form

`st.form` crea un formulario que agrupa los elementos junto con un botón "Enviar".

Por lo general, cada vez que un usuario interactúa con un componente, Streamlit se vuelve a ejecutar.

Un formulario es un contenedor que agrupa visualmente otros elementos y componentes, y contiene un botón Enviar. Aquí, un usuario puede interactuar con uno o más componentes tantas veces como quiera sin provocar una repetición. Finalmente, cuando se presiona el botón Enviar del formulario, todos los valores dentro del formulario se enviarán a Streamlit en un solo lote.

Para agregar elementos a un objeto de formulario, puede usar la notación `with` (preferida) o puede usarla como un objeto simplemente llamando métodos directamente en el formulario (primero asignándolo a una variable y luego aplicando métodos subsecuentemente). Ver en la aplicación de ejemplo.

Los formularios tienen algunas restricciones:
- Cada formulario debe contener un `st.form_submit_button`.
- `st.button` y `st.download_button` no se pueden agregar a un formulario.
- Los formularios pueden aparecer en cualquier lugar de su aplicación (barra lateral, columnas, etc.), pero no se pueden incrustar dentro de otros formularios.

Para obtener más información sobre los formularios, consulte nuestra [publicación de blog](https://blog.streamlit.io/introducing-submit-button-and-forms/).

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## Código
He aquí cómo usar `st.form`:
```python
import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.write('**Order your coffee**')
    
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

A esto le sigue la creación de un título para la aplicación:
```python
st.title('st.form')
```

### Primer ejemplo
Comencemos con el primer ejemplo, aquí aplicaremos el comando `st.form` a través de la notación `write`. Dentro del formulario, comenzaremos escribiendo un subtítulo `Order your coffee` y luego crearemos varios componentes (`st.selectbox`, `st.select_slider` y `st.checkbox`) para recopilar información sobre el pedido de café. Finalmente, se crea un botón de envío a través del comando `st.form_submit_button`, que cuando se hace clic en él enviará todos los datos del usuario de una sola vez para su procesamiento.
```python
# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
```

A continuación, agregaremos la lógica de lo que sucede después de hacer clic en el botón Enviar. De forma predeterminada, cada vez que se carga Streamlit, se ejecutará la instrucción `else` y veremos el mensaje `☝️ Place your order!`. Mientras que al hacer clic en el botón Enviar, todas los datos proporcionadas por el usuario a través de los diversos componentes se almacenan en varias variables (por ejemplo, `coffee_bean_val`, `coffee_roast_val`, etc.) y se imprimen mediante el comando `st.markdown` con la ayuda de f-string.
```python
if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')
```


### Segundo ejemplo
Pasemos ahora al segundo ejemplo sobre el uso de `st.form` como una notación de objeto. Aquí, el comando `st.form` se asigna a la variable `form`. Posteriormente, se aplican varios comandos Streamlit como `slider` o `form_submit_button` en la variable `form`.
```python
# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## Otras lecturas
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [Presentamos el botón Enviar y los formularios](https://blog.streamlit.io/introducing-submit-button-and-forms/)
