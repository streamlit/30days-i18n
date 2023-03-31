# st.button

`st.button` permite exibir um botão.

## O que estamos construindo?

Uma aplicação simples que imprime condicionalmente mensages alternadas, dependendo se o botão estão pressionado ou não.

Fluxo da aplicação:
1. Por padrão, a aplicação imprime `Goodbye`
2. Após clicar no botão, a aplicação imprime `Why hello there`

## Aplicação de Demonstração
Depois de feito o deploy a aplicação ficará semelhante a mostrada no link abaixo.
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## Código
Aqui está o código para ser implementano na aplicação mencionada acima:
```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('st.button')
```

Agora, vamos utilizar condicionais `if` e `else` para imprimir as mensagens alternadamente.

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```
Como podemos ver no código acima, o comando `st.button()` recebe `Say hello` como argumento de entrada, que é o texto que o botão exibirá. 

O comando `st.write` é usado para imprimir mensages de texto, no caso `Why hello there` ou `Goodbye`, dependendo se o botão foi clicado ou não, que é implementando assim:

```python
st.write('Why hello there')
```
e
```python
st.write('Goodbye')
```

É importante mencionar que os comandos `st.write` estão dentro das condicionais `if` e `else` para poder imprimir as mensages alternadamente, conforme mencionado acima.

## Próximos passos

Agora que você crirou a aplicação Streamlit localmente, é hora de fazer deploy para o 
[Streamlit Cloud](https://streamlit.io/cloud) como será explicando em breve em um novo desafio.

Porque essa éa  primeira semana do desafio, nós estamos provendo o código fonte completo (nas caixas de código acima) e solução (a aplicação de exemplo) linkada nesta página. 

Mais adiante, nos próximos desafios, recomendamos que você primeiro tente implementar a aplicação Streamlit sozinho.

Não se preocupe, caso não consiha seguir adiante você sempre pode dar uma consultada na solução.

## Referências
Leia sobre o [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) na documentação da API do Strealit