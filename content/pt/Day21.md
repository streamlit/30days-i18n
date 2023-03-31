# st.progress

`st.progress` Exite uma barra de progresso, que é atualizada  graficamente a medida que iteração progride.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

## Código
Veja como usar o  `st.progress`:
```python
import streamlit as st
import time

st.title('st.progress')

with st.expander('Sobre esta aplicação'):
     st.write('Agora você pode exibir o progresso od seus calculosthe progress of your e, uma aplicação Streamlit com o comando `st.progress`.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st` junto com a biblioteca `time`:
```python
import streamlit as st
import time
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('st.progress')
```

Uma **caixa Sobre esta aplicação** é criada usando `st.expander` e a descrição é exbida via `st.write`:
```python
with st.expander('Sobre esta aplicação'):
     st.write('Agora você pode exibir o progresso od seus calculosthe progress of your e, uma aplicação Streamlit com o comando `st.progress`.')
```

Finalmente, nós definimos a barra de progresso e instaciamos ela com o valor inicial de `0`. Então, um loop `for` vai iterar de `0` a `100`. Em cada iteração, nos vamos usar o `time.sleep(0.05)` para a aplicação esperar `0.05` antes de adicionar o valor `1` à barra de progresso `my_bar`, assim a barra de progresso é incrementada a cada iteração.

```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## Leitura complementar
- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)
