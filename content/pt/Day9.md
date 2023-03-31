# st.line_chart

`st.line_chart` permite exibir um gráfico de linhas

Este é um [açúcar sintático](https://pt.wikipedia.org/wiki/A%C3%A7%C3%BAcar_sint%C3%A1tico) relacionado ao  `st.altair_chart`. A principal diferença é que este comando usa as colunas e índices dos próprios dados e tenta descobrir a melhora maneira de exibir o gráfico. Ou seja, é mais fácil de usar para os cenários "apenas exiba o gráfico", porém menos customizável.

Se o `st.line_chart` não acertar a melhor maneira de exibir o gráfico, ou o melhor tipo, tente usar o `st.altair_chart` e especifique a informação desejada.

## O que estamos construindo?

Uma aplicação simples para exibir um gráfico de linhas

Fluxo da aplicação:
1. Cria um DataFrame pandas com números gerados aleatoriamente pelo `NumPy`.
2. Cria e mostra um gráfico de linha usando o comando `st.line_chart()`.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## Código
Veja aqui mais informações sobre como usar o [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart):
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Gráfico de linhas')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
import pandas as pd
import numpy as np
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('Gráfico de linhas')
```

Agora, nós criamos o Dataframe de 3 colunas com números aleatórios. 
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

Finalmente, um gráfico de linhas é criado usando `st.line_chart()` com o DataFrame armazenado na variável `chart_data` como entrada:
```python
st.line_chart(chart_data)
```

## Leitura complementar
Leia mais sobre o comando abaixo, pois o [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) se baseia nele:
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
