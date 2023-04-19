# Componentes do Streamlit

Componentes são módulos Python desenvolvidos por terceiro que ampliam as possibilidades do Streamlit [[1](https://docs.streamlit.io/library/components)].

## Quais componentes estão disponíveis?

Existe algumas dezenas de componentes em destaque no site do Streamlit [[2](https://streamlit.io/components)].

Fanilo (um [Streamlit Creator](https://streamlit.io/creators)) fez a curadoria de uma lista de componentes do Streamlit nesse post [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)]. Em abril de 2022 essa lista tinha aproximadamente 85 componentes.

## Como usar?

Componentes do Streamlit estão a distância de um pip-install.

Neste tutorial, vamos utilizar o componente `streamlit_pandas_profiling`. [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

#### Instalando o componente

```bash
pip install streamlit_pandas_profiling
```

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## Código
Como contruir uma aplicação utilizando um componente
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st` assim com as outras bibliotecas utilizadas na aplicação:
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('`streamlit_pandas_profiling`')
```

Agora, nós vamos carregar o dataset de Pinguins  usando o comando `read_csv` do `pandas`.
```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

Finalmente, o relatório de perfil do pandas é gerado através do comando `profile_report()` e exibido usando `st_profile_report`:
```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Desenvolvendo seus próprios Componentes

Se você está interessado em desenvolver seu próprio componente, veja abaixo os seguintes recursos (em inglês):
- [Criando um Componentes](https://docs.streamlit.io/library/components/create)
- [Publicando um Componentes](https://docs.streamlit.io/library/components/publish)
- [API dos Componentes](https://docs.streamlit.io/library/components/components-api)
- [Blog post sobre Componentes](https://blog.streamlit.io/introducing-streamlit-components/)

Alternativamente, se você prefere aprender com vídeos, nosso engenheiro Tim Conkling juntou alguns ótimos tutoriais
- [Como desenvolver um componente Streamlit | Parte 1: Setup e Arquitetura](https://youtu.be/BuD3gILJW-Q)
- [Como desenvolver um componente Streamlit | Parte 2: Fazendo um controle deslizante](https://youtu.be/QjccJl_7Jco)

## Leitura complementar sobre Componentes
1. [Componentes do Streamlit - Documentação da API](https://docs.streamlit.io/library/components)
2. [Componentes Streamlit em destaque](https://streamlit.io/components)
3. [Componentes Streamlit - Rastreados pela comunidade](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)
