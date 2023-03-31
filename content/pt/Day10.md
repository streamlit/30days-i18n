# st.selectbox

`st.selectbox` exibe um componente de seleção

## O que estamos construindo?

Uma aplicação simples que pergunta ao usuário qual a cor favorita dele.

Fluxo da aplicação:
1. Usuário seleciona a cor
2. Aplicação exibe a cor selecionada

## Aplicação de demonstração

Depois de feito o deploy a aplicação ficará semelhante a mostrada no link abaixo.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## Código
Aqui está o código para ser implementano na aplicação mencionada acima:
```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'Qual a sua cor favorita?',
     ('Azul', 'Vermelho', 'Verde'))

st.write('Sua cor favorita é ', option)
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('st.selectbox')
```

Em seguida, vamos criar uma variável chamada `option` que vai receber o valor do componente **selectbox** através do comando `st.selectbox()`.

```python
option = st.selectbox(
     'Qual a sua cor favorita?',
     ('Azul', 'Vermelho', 'Verde'))
```
Como você pode ver no código acima, o comando `st.selectbox()` aceita 2 argumentos (parâmetetros) de entrada:
1. O texto que vai acima do componente, ex: 'Qual a sua cor favorita?'
2. Os valores possíveis de serem selecionados `('Azul', 'Vermelho', 'Verde')`

Finalmente, vamos imprimir a cor selecionada:
```python
st.write('Sua cor favorita é ', option)
```

## Próximos passos
Agora que você criou essa aplicação Streamlit localmente, é hora de fazer deploy no [Streamlit Cloud](https://streamlit.io/cloud).


## Referências
Mais sobre [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)
