# st.cache

`st.cache` permite otimizar a performance da sua aplicação Streamlit.


O Streamlit fornece um mecanismo de cache que permite que sua aplicação mantenha a performance mesmo ao carregar dados da Web, manipular grandes conjuntos de dados(datasets) ou realizar cálculos caros. Isso é feito com o decorador(decorator) `@st.cache`.


Quando você marca uma função com o decorator @st.cache, ele informa ao Streamlit que sempre que a função é chamada, ele precisa verificar algumas coisas:

1. Os parâmetros de entrada com os quais você chamou a função
2. O valor de qualquer variável externa usada na função
3. O corpo da função
4. O corpo de qualquer função usada dentro da função cacheada

Se esta é a primeira vez que o Streamlit vê esses quatro componentes com esses exatos valores, nessa combinação e ordem exatas, ele executa a função e armazena o resultado em um cache local. Então, na próxima vez que a função em cache é chamada, se nenhum desses componentes for alterado, o Streamlit vai pular a execução da função e, em vez disso, retornará a saída armazenada anteriormente no cache.

A maneira como o Streamlit acompanha as mudanças nesses componentes é usando um hash. Pense no cache como um armazenamento chave-valor em memória, onde a chave é um hash de todos os itens acima e o valor é o objeto de saída real, passado por referência.

Finalmente, `@st.cache` suporta argumentos(parâmetros) para configurar o comportamento do cache. Você pode encontrar mais informações sobre eles na documentação da API.

## Como usar?

Você pode adicionar o decorator `st.cache` na linha anterior de uma função personalizada, que você define em sua aplicação Streamlit. Veja o exemplo abaixo.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## Código
Veja como usar o `st.cache`:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Usando cache
a0 = time()
st.subheader('Usando st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# sem usar cache
b0 = time()
st.subheader('Sem usar st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st` assim com as outras bibliotecas utilizadas na aplicação:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('Streamlit Cache')
```

Em seguida, vamos definir 2 funções personalizadas para gerar um grande DataFrame, onde a primeira faz uso do decorator `st.cache` e a segunda não:
```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

Finalmente, vamos executar a função personalizada, enquanto também cronometramos o tempo de execução usando o comando `time()`.
```python
# Usando cache
a0 = time()
st.subheader('Usando st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Sem usar cache
b0 = time()
st.subheader('Sem usar st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

Observe como a primeira execução pode fornecer um tempo de execução aproximadamente semelhante. Recarregue(refresh) a aplicação e observe como o tempo de execução muda ao usar o decorator `st.cache`. Você observou algum aumento de velocidade?

## Leitura complementar
- [`st.cache` Documentação da API](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [Otimize a performance com `st.cache`](https://docs.streamlit.io/library/advanced-features/caching)
- [Instruções primitivas de cache - Experimental](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
