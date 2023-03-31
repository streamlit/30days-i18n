# st.multiselect

`st.multiselect` exibe um componente de seleção múltipla

## Aplicação de Demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## Código
Como usar o  `st.multiselect`:
```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho'])

st.write('Você selecionou:', options)
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('st.multiselect')
```

Agora, nós vamos usar o componente `st.multiselect` para receber a entrada dos usuários, que escolherão uma ou mais cores. 

```python
options = st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho'])
```

Finalmente vamos imprimir as cores selecionadas:
```python
st.write('Você selecionou:', options)
```

## Leitura complementar
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
