# st.latex

`st.latex` exibe expressões matématicas formatadas como LaTeX.

## O que estamos construindo?

Uma aplicação simples que exibe uma equação matemática usando sintaxe LaTeX com o comando `st.latex`.

## Aplicação de demonstração
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## Código
Veja como usar o `st.latex`:
```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('st.latex')
```

Agora, vamos exbir a equação matemática usando `st.latex`:
```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Referências
- Leia mais sobre [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex) na Documentação da API Streamlit.
