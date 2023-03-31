# A arte de criar aplicações Streamlit

Hoje é o dia 30 do desafio *#30DaysOfStreamlit*. Parabéns por chegar tão longe no desafio.

Neste tutorial, vamos colocar nosso conhecimento recém-descoberto desse desafio de aprendizado para criar aplicações Streamlit para resolver problemas do mundo real.

## Problema do mundo real.

Como criador de conteúdo, ter acesso a miniaturas (thumbnails) dos vídeos do YouTube são recursos úteis para promoção em redes sociais e criação de conteúdo.

Vamos descobrir como vamos resolver esse problema e construir uma aplicação Streamlit.

## Solução

Hoje, vamos construir o `yt-img-app`, que é uma aplicação Streamlit que pode extrair as miniaturas (thumbnails) de vídeos do YouTube.

Em poucas palavras, aqui estão as 3 etapas que queremos que a aplicação Streamlit faça:

1. Recebe uma URL do YouTube como entrada
2. Processa a URL para extrair o ID do vídeo do YouTube
3. Use o ID do vídeo do YouTube como uma entrada para a função que extrai e exibe as miniaturas (thumbnails) dos vídeos do YouTube

## Instruções

To get started in using the Streamlit app, copy and paste a YouTube URL into the input text box.
Para começar a usar o aplicação Streamlit, copie e cole a URL do YouTube na caixa de texto.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## Código
Veja como construir a aplicação Streamlit `yt-img-app`:
```python
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('Gerador de miniaturas (thumbnails) (thumbnails) de vídeos do YouTube')

with st.expander('Sobre'):
  st.write('Esta aplicação extrai miniaturas (thumbnails) de um vídeo do Youtube.')
  
# Configuração da imagem
st.sidebar.header('Configurações')
img_dict = {'Máxima': 'maxresdefault', 'Alta': 'hqdefault', 'Média': 'mqdefault', 'Padrão': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Selecione a qualidade da miniatura', ['Máxima', 'Alta', 'Média', 'Padrão'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Cole a URL do YouTube', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
    
# Exibe a imagem da miniatura
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('URL da miniatura (thumbnail) do vídeo do YouTube: ', yt_img)
else:
  st.write('☝️ Insira uma URL para continuar ...')
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Em seguida, exibimos o título do aplicativo e um cabeçalho:
```python
st.title('🖼️ yt-img-app')
st.header('Gerador de miniaturas (thumbnails) de vídeos do YouTube')
```
Enquanto estamos aqui, também podemos criar uma caixa expansível Sobre.
```python
with st.expander('Sobre'):
  st.write('Esta aplicação extrai miniaturas (thumbnails) de um vídeo do Youtube.')
 
Aqui, criamos uma caixa de seleção para receber a entrada do usuário sobre a qualidade da imagem a ser extraída.
```python
# Configuração da imagem
st.sidebar.header('Configurações')
img_dict = {'Máxima': 'maxresdefault', 'Alta': 'hqdefault', 'Média': 'mqdefault', 'Padrão': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Selecione a qualidade da miniatura', ['Máxima', 'Alta', 'Média', 'Padrão'])
img_quality = img_dict[selected_img_quality]
```

Uma caixa de texto é exibida para receber a entrada do usuário, a URL do vídeo do YouTube que será usada para extrair a imagem.
```python
yt_url = st.text_input('Cole a URL do YouTube', 'https://youtu.be/JwSS70SZdyM')
```

Uma função para executar o processamento da URL de entrada.
```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

Por fim, usamos o controle de fluxo para determinar se devemos exibir um lembrete para inserir a URL (como na instrução `else`) ou exibir a miniatura do vídeo YouTube (como na instrução `if`).
```python
# Exibe a imagem da miniatura
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('URL da miniatura (thumbnail) do vídeo do YouTube: ', yt_img)
else:
  st.write('☝️ Insira uma URL para continuar ...')
```

## Resumo

Em resumo, vimos que na criação de qualquer aplicação Streamlit, normalmente começamos por identificar e definir o problema. Em seguida, criamos uma solução para resolver o problema, dividindo-o em etapas menores, que implementamos na aplicação Streamlit.

Aqui, também temos que determinar quais dados ou informações precisamos como entrada dos usuários, a abordagem (e o método) a serem usados ​​no processamento da entrada para produzir a saída final desejada.

Espero que tenham gostado deste tutorial, Divirta-se com o Streamlit!
