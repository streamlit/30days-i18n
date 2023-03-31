# st.write

`st.write` permite exibir textos e argumentos (parâmetros) na aplicação Streamlit

Além de exibir texto, o comando `st.write()` também pode exibir:
- strings; funciona semelhante ao `st.markdown()`
- Exibir dicionários (`dict`) Python
- Exibir Dataframes do `pandas` como uma tabela
- Plotar gráficos e figuras das seguinte bibliotecas: `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh`
- e mais (veja [st.write na documentação da API](https://docs.streamlit.io/library/api-reference/write-magic/st.write))

## O que estamos construindo?

Um aplicação simple mostrando diversas maneiras de como usar o comando `st.write()` para exibir texto, números,  Dataframes e gráficos.

## Aplicação de demonstração
Depois de feito o deploy a aplicação ficará semelhante a mostrada no link abaixo.
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Coódigo
Como usar o st.write:
```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Exemplo 1

st.write('Hello, *World!* :sunglasses:')

# Exemplo 2

st.write(1234)

# Exemplo 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Exemplo 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Exemplo 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('st.write')
```

**Exemplo 1**
Caso de uso mais básico, exibir texto e texto no formato Markdown:
```python
st.write('Hello, *World!* :sunglasses:')
```

**Exemplo 2**
Como mencionado acima, também podemos exibir outros foramdos, como números:
```python
st.write(1234)
```

**Exemplo 3**
DataFrames também podem ser exibidos:
```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
```

**Example 4**
Você pode passar múltiplos argumentos (parâmetros):
```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**Example 5**
Finalmente, você também pode exibir dados de gráficos, passando os dados para uma variável da seguinte maneira:
```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Aplicação de demonstração
Depois de feito o deploy a aplicação ficará semelhante a mostrada no link abaixo.
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Próximos passos

Agora que você crirou a aplicação Streamlit localmente, é hora de fazer deploy para o 
[Streamlit Cloud](https://streamlit.io/cloud) como será explicando em breve em um novo desafio.

Porque essa éa  primeira semana do desafio, nós estamos provendo o código fonte completo (nas caixas de código acima) e solução (a aplicação de exemplo) linkada nesta página. 

Mais adiante, nos próximos desafios, recomendamos que você primeiro tente implementar a aplicação Streamlit sozinho.

Não se preocupe, caso não consiha seguir adiante você sempre pode dar uma consultada na solução.

## Leitura complementar
Além do [`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write), você pode explorar outras maneiras de exibir texto:
- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)