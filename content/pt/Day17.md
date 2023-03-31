# st.secrets

`st.secrets` permite que você armazene informações confidenciais (segredos) como chaves de API, senhas de bancos de dados e outras credenciais.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## Código
Veja como usar o `st.secrets`:
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('st.secrets')
```

Finalmente, vamos exibir as informações confidenciais armazenadas:
```python
st.write(st.secrets['message'])
```

As informações confidenciais (segredos) podem ser armazenados no Streamlit Cloud como mostrados nas capturas de tela mencionadas abaixo.

Caso esteja trabalhando localmente, as informações podem ser armazenadas em `.streamlit/secrets.toml`, tome muito cuidado para não fazer upload desse arquivo para o GitHub quando estiver fazendo um deploy.


## Leitura complementar
- [Adicionando segredos às suas aplicações](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [Gerenciamento de segredos](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
