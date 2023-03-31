# st.checkbox

`st.checkbox` exibe um componente de caixa de seleção.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## Código
Veja como usar o `st.checkbox`:
```python
import streamlit as st

st.header('st.checkbox')

st.write ('O que você gostaria de pedir?')

icecream = st.checkbox('Sorvete')
coffee = st.checkbox('Café')
cola = st.checkbox('Refrigerante')

if icecream:
     st.write("Sucesso! Aqui está o seu 🍦")
    
if coffee: 
     st.write("Ok, aqui está o seu café ☕")

if cola:
     st.write("E lá vamos nós 🥤")
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('st.checkbox')
```

Agora, nós vamos perguntar ao usuário usando o `st.write`:
```python
st.write ('O que você gostaria de pedir?')
```

Em seguida vamos mostrar algumas opções do menu que podem ser selecionadas:
```python
icecream = st.checkbox('Sorvete')
coffee = st.checkbox('Café')
cola = st.checkbox('Refrigerante')
```

Finalmente, nós vamos imprimir uma mensagem customizada, dependendo das caixas de seleções que foram marcadas:
```python
if icecream:
     st.write("Sucesso! Aqui está o seu 🍦")
    
if coffee: 
     st.write("Ok, aqui está o seu café ☕")

if cola:
     st.write("E lá vamos nós 🥤")
```  

## Leitura complementar
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
