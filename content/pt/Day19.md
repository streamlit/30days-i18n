# Como definir o layout da sua aplicação Streamlit

Neste tutorial, n'so vamos usar os seguintes comando para definir o layout da sua aplicação Streamlit.
- `st.set_page_config(layout="wide")` - Exibe os conteúdos da aplicação em modo *wide (amplo)*, caso contrário, por padrão, os conteúdos serão encapsulados em uma caixa com largura fixa.
- `st.sidebar` - Coloca os componentes, texto e imagens na barra lateral.
- `st.expander` - Coloca texto e images dentro de uma caixa (container) flexível.
- `st.columns` - Cria uma coluna onde os conteúdos podem ser adicionados.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## Código
Veja como definir o layout de uma aplicação Streamlit
```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('Como customizar o Layout de uma aplicação Streamlit')

with st.expander('Sobre esta aplicação'):
  st.write('Esta aplicação demonstra diversas maneiras de como você pode definir o layout da sua aplicação Streamlit')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Entrada')
user_name = st.sidebar.text_input('Qual o seu nome?')
user_emoji = st.sidebar.selectbox('Escolha um emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('Qual a sua comida favorita?', ['', 'Feijoada', 'Burrito', 'Lasanha', 'Hamburger', 'Pizza'])

st.header('Saída')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Olá {user_name}!')
  else:
    st.write('👈  Por favor escreva seu **nome**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} é o seu **emoji** favorito!')
  else:
    st.write('👈 Por favor escolha um **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** é a sua **comida** favorita!')
  else:
    st.write('👈 Por favor escolha sua **comida** favorita!')
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Nós vamos começar definindo que o layout da página deve ser exibido no modo `wide`, que permite o conteúdo expandir e ocupar toda a largura do browser.
```python
st.set_page_config(layout="wide")
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('Como customizar o Layout de uma aplicação Streamlit')
```

Uma caixa (container) flexível chamada `Sobre esta aplicação` será colocada baixo do do cabeçalho. Após a expansão dele, nós veremos algumas informações adicionais.
```python
with st.expander('Sobre esta aplicação'):
  st.write('Esta aplicação demonstra diversas maneiras de como você pode definir o layout da sua aplicação Streamlit')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

Componentes de entrada, para receber os dados dos usuários, são colocados na barra lateral com o uso do comando `st.sidebar` antes dos comandos `text_input` e `selectbox`. Os valores escolhidos (ou digitados) pelo usuário serão armazenados nas variáveis `user_name`, `user_emoji` e `user_food`.
```python
st.sidebar.header('Entrada')
user_name = st.sidebar.text_input('Qual o seu nome?')
user_emoji = st.sidebar.selectbox('Escolha um emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('Qual a sua comida favorita?', ['', 'Feijoada', 'Burrito', 'Lasanha', 'Hamburger', 'Pizza'])
```

Finalmente, nós vamos criar 3 colunas usando o comando `st.columns`, respectivamente `col1`, `col2` e `col3`. Então, nós vamos atribuir à cada uma das colunas um bloco de código individual usando o `with`. Por baixo dele, nós vamos criar uma condicional `if` que exibe uma das duas alternativas, dependendo se o usuário entrou, ou não, com alguma informação (na barra lateral). Por padrão, a página exibe o texto que está no `else`. Após o usuário entrar com a informação, ela será exibida abaixo do cabeçalho `Saída`.

```python
st.header('Saída')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Olá {user_name}!')
  else:
    st.write('👈  Por favor escreva seu **nome**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} é o seu **emoji** favorito!')
  else:
    st.write('👈 Por favor escolha um **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** é a sua **comida** favorita!')
  else:
    st.write('👈 Por favor escolha sua **comida** favorita!')
```
Vale lembrar que foi usado o `f` antes de strings, também conhecido como *f-strings*, para combinar textos e as variáveis com os dados de entrada do usuário.

## Leitura complementar
- [Layouts e Containers](https://docs.streamlit.io/library/api-reference/layout)
- [f-strings](https://peps.python.org/pep-0498/)
