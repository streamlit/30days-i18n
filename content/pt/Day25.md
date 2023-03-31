# st.session_state

Definimos o acesso a uma aplicação Streamlit, em uma aba do navegador, como uma sessão. Cada aba do navegador que se conecta ao servidor Streamlit, uma nova sessão é criada. Streamlit executa novamente seu script (de cima para baixo) toda vez que você interage com sua aplicação. Cada reexecução ocorre em uma lousa em branco: nenhuma variável é compartilhada entre as execuções.

Session State (ou em português estado da sessão) é uma maneira de compartilhar variáveis ​​entre reexecuções, para cada sessão do usuário. Além da capacidade de armazenar e persistir estado, o Streamlit também tem a capacidade de manipular o estado usando Callbacks.

Neste tutorial, camos islustrar o uso de Session State e Callbacks à medida que criamos uma aplicação de conversão de peso.

`st.session_state` permite a implementação de Session State em uma aplicação Streamlit.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## Código
Veja como usar o `st.session_state`:
```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Entrada')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Libras:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kg:", key = "kg", on_change = kg_to_lbs)

st.header('Saída')
st.write("Objeto st.session_state:", st.session_state)
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('st.session_state')
```

Em seguida, vamos definir funções customizadas para a conversão de peso de libras para kg e vice-versa
```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

Aqui, vamos usar `st.number_input` para receber entradas numéricas dos valores de peso:
```python
st.header('Entrada')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Libras:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kg:", key = "kg", on_change = kg_to_lbs)
```
As 2 funções customizadas acima serão chamadas assim que um valor numérico for inserido na caixa de número, criada usando o comando `st.number_input`. Observe como a opção `on_change` especifica as 2 funções personalizadas `lbs_to_kg` e `kg_to_lbs`).

Resumindo, ao inserir um número na caixa `st.number_input`, o número é convertido por essas funções customizadas.

Finalmente, os valores de peso em unidades `kg` e `lbs` armazenados no estado da sessão como `st.session_state.kg` e `st.session_state.lbs` serão exibidos via `st.write`:
```python
st.header('Saída')
st.write("Objeto st.session_state:", st.session_state)
```

## Leitura complementar
- [Session State](https://docs.streamlit.io/library/api-reference/session-state)
- [Adicionar estado às aplicações](https://docs.streamlit.io/library/advanced-features/session-state)
