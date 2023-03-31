# Como usar API criando a aplicatição Bored API

A aplicação Bored API sugere coisas divertidas para você fazer quando estiver com tédio!

Tecnicamente, também demonstra o uso de APIs de dentro de uma aplicação Streamlit.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## Código
Veja como implementar a Bored API:
```python
import streamlit as st
import requests

st.title('🏀 Bored API')

st.sidebar.header('Entrada')
selected_type = st.sidebar.selectbox('Escolha um tipo de atividade', ["educação", "recreação", "social", "faça você mesmo", "caridade", "cozinhar", "relaxar", "música", "tarefas pequenas"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('Sobre'):
    st.write('Você está com tédio? A **Bored API** fornece sugestões de atividades que você pode fazer quando estiver com tédio. Esta aplicação é alimentado pela API Bored.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
    
st.header('Atividade sugerida')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Número de Participantes', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Tipo da atividade', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Preço', value=suggested_activity['price'], delta='')
```

## Line-by-line explanation
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st` assim com as outras bibliotecas utilizadas na aplicação:
```python
import streamlit as st
import requests
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('🏀 Bored API')
```

Em seguida, vamos receber a entrada do usuário no **tipo de atividade** por meio do comando `st.selectbox`:
```python
st.sidebar.header('Entrada')
selected_type = st.sidebar.selectbox('Escolha um tipo de atividade', ["educação", "recreação", "social", "faça você mesmo", "caridade", "cozinhar", "relaxar", "música", "tarefas pequenas"])
```

A atividade selecionada, mencionada acima, é anexada a URL por meio de uma string f, que é usada para recuperar os dados do JSON que será retornado:
```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

Aqui, exibiremos informações sobre a aplicação e os dados JSON por meio do comando `st.expander`.
```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('Sobre'):
    st.write('Você está com tédio? A **Bored API** fornece sugestões de atividades que você pode fazer quando estiver com tédio. Esta aplicação é alimentado pela API Bored.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

Em seguida, exibiremos uma atividade sugerida:
```python
st.header('Atividade sugerida')
st.info(suggested_activity['activity'])
```

Por fim, exibiremos as informações que acompanham a atividade sugerida, como 'Número de participantes', 'Tipo de atividade' e 'Preço'.
```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Número de Participantes', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Tipo da atividade', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Preço', value=suggested_activity['price'], delta='')
```

## Leitura complementar
- [Bored API](http://www.boredapi.com/)
