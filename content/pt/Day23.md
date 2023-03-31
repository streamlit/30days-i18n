# st.experimental_get_query_params

`st.experimental_get_query_params` recupera parâmetros da consulta(query paramaters) diretamente da URL do navegador.

## Aplicação de demonstração

1. O seguinte link, carrega a aplicação sem parâmetros de consulta (observe a mensagem de erro):

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.experimental_get_query_params/)

2. Este link, carrega a aplicação com parâmetros de consulta (sem mensagem de erro):

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk)

## Código
Veha como usar o  `st.experimental_get_query_params`:
```python
import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('Sobre esta aplicação'):
  st.write("`st.experimental_get_query_params` recupera parâmetros da consulta(query paramaters) diretamente da URL do navegador.")

# 1. Instruções
st.header('1. Instruções')
st.markdown('''
Na barra de URL do seu navegador de internet, anexe o seguinte:
`?name=Jack&surname=Beanstalk`
depois da URL base `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
então ficará assim 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2. Conteúdos do st.experimental_get_query_params
st.header('2. Conteúdos do st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3. Recuperando e exibindo informações da URL
st.header('3. Recuperando e exibindo informações da URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Olá **{firstname} {surname}**, tudo bem?')
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('st.experimental_get_query_params')
```

Vamos também adicionar uma caixa drop-down:
```python
with st.expander('Sobre esta aplicação'):
  st.write("`st.experimental_get_query_params` recupera parâmetros da consulta(query paramaters) diretamente da URL do navegador.")
```

Em seguida, forneceremos instruções aos visitantes da aplicação, sobre como eles podem passar parâmetros de consulta(query paramaters) diretamente para na URL:
```python
# 1. Instructions
st.header('1. Instruções')
st.markdown('''
Na barra de URL do seu navegador de internet, anexe o seguinte:
`?name=Jack&surname=Beanstalk`
depois da URL base `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
então ficará assim 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')
```

Na sequência, exibiremos o conteúdo do comando `st.experimental_get_query_params`.
```python
# 2. Conteúdos do st.experimental_get_query_params
st.header('2. Conteúdos do st.experimental_get_query_params')
st.write(st.experimental_get_query_params())
```

Finalmente, vamos selecionar e exibir as informações dos parâmetros de consulta da URL:
```python
# 3. Recuperando e exibindo informações da URL
st.header('3. Recuperando e exibindo informações da URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Olá **{firstname} {surname}**, tudo bem?')
```

## Leitura complementar
- [`st.experimental_get_query_params`](https://docs.streamlit.io/library/api-reference/utilities/st.experimental_get_query_params)
