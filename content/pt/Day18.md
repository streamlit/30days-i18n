# st.file_uploader

`st.file_uploader` exibe um componente de upload de arquivo [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

Por padrão, o tamanho dos arquivos para upload é limitado em 200MB. Você pode definir isto usando a opção de configuração `server.maxUploadSize`. Para mais informações sobre opções de configuração, acesse [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## Código
Veja como usar o `st.file_uploader`:
```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Upload de CSV')
uploaded_file = st.file_uploader("Escolha um arquivo")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Estatístiscas descritivas')
  st.write(df.describe())
else:
  st.info('☝️ Faça upload de um arquivo CSV')
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st` assim com as outras bibliotecas utilizadas na aplicação:
```python
import streamlit as st
import pandas as pd
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('st.file_uploader')
```

Agora vamos usar o `st.file_uploader` para exibir um componente de upload de arquivo para receber o arquivo do usuários:
```python
st.subheader('Upload de CSV')
uploaded_file = st.file_uploader("Escolha um arquivo")
```

Finalmente, temos um condicional que inicialmente mostra uma mensagem de boas vindas convidando o usuário a fazer upload de um arquivo (como implementando na condição `else`). Após o upload do arquivo o `if` é ativado, o arquivo CSV é lido pela bilbioteca `pandas` e exibido pelo comando `st.write`.

```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Estatístiscas descritivas')
  st.write(df.describe())
else:
  st.info('☝️ Faça upload de um arquivo CSV')
```

## Leitura complementar
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [OpçÕes de configuração](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
