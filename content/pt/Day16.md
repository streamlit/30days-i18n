# Customizando o tema das aplicações Streamlit

Nós podemos cuistomizar o tema ajustando os parâmetros no arquivo de configuração chamado `config.toml`, que fica dentro da pasta `.streamlit`, na raiz da aplicação.

## O que estamos construindo?

Uma aplicação simples que exibe o resultado da nossa customização de tema. Isto é possível customizando o código HTML em Hexadecimal dentro do arquivo [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml).

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## Código
Segue o código para o arquivo [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py):
```python
import streamlit as st

st.title('Customizando o tema de aplicações Streamlit')

st.write('Conteúdo do arquivo `.streamlit/config.toml` desta aplicação')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Selecione um número:', 0, 10, 5)
st.write('O número selecionado no controle deslizante é:', number)
```

Este é o código do arquivo [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml):
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('Customizando o tema de aplicações Streamlit')
```

Agora, nós vamos exibir o conteúdo do arquivo `.streamlit/config.toml`, que primeiro vamos exibir uma texto usando o comando `st.write` e em seguida o arquivo atual usando o comando `st.code`:
```python
st.write('Conteúdo do arquivo `.streamlit/config.toml` desta aplicação')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

Finalmente, vamos criar um controle deslizante na barra lateral e exibir o número selecionado:
```python
number = st.sidebar.slider('Selecione um número:', 0, 10, 5)
st.write('O número selecionado no controle deslizante é:', number)
```

Vamos agora observar as cores customizadas que nós utilizamos nessa aplicação, elas estão no arquivo `.streamlit/config.toml`:
- `primaryColor="#F39C12"` - Configura a cor primária para laranja. Observe a cor do controle deslizante.
- `backgroundColor="#2E86C1"` - Configura a cor do plano de fundo para azul. Observe a cor azul no painel principal.
- `secondaryBackgroundColor="#AED6F1"` - Configura a cor secundária de planop de fundo para cinza claro. Observe a cor da barra lateral e da caixa de texto com código no painel principal.
- `textColor="#FFFFFF"` - Configura a cor de texto para branca.
- `font="monospace"` - Configura a fonte para monospace.


## Leitura complementar
- [Customizando Temas](https://docs.streamlit.io/library/advanced-features/theming)
- [Códigos de cor em HTML](https://htmlcolorcodes.com/) é uma ótima ferramenta para selecionar cores do seu interesse.
