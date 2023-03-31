# st.form

`st.form` cria um formulário que agrupa os elementos junto com o botão "Enviar".

Normalmente, quando um usuário interage com um componente a aplicação Streamlit é executada novamente.

Um formulário é um container que agrupa visualmente outros elementos e componentes e, também, contém um botão Enviar. Aqui, um usuário pode interagir com um ou mais widgets quantas vezes quiser sem causar uma reexecução. Por fim, quando o botão Enviar do formulário é clicado, todos os valores dos componentes, que estão dentro do formulári,o serão enviados para o Streamlit de uma vez.

Para adicionar elementos a um formulário, você pode usar a notação `with` (preferível) ou pode usá-lo como um objeto, apenas chamando métodos diretamente no formulário (primeiro atribuindo a uma variável e posteriormente aplicando métodos Streamlit). Veja na aplicação de exemplo.


Os formulários têm algumas restrições:
- Todo formulário deve conter um `st.form_submit_button`.
- `st.button` e `st.download_button` não podem ser adicionados a um formulário.
- Os formulários podem ser exibidos em qualquer lugar na sua aplicação (barra lateral, colunas, etc), mas não podem ser incorporados em outros formulários.

Para mais informação sobre formuários, veja o nosso [blog post](https://blog.streamlit.io/introducing-submit-button-and-forms/).

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## Código
Veja como usar o `st.form`:
```python
import streamlit as st

st.title('st.form')

# Exemplo completo usando a notação with
st.header('1. Exemplo usando a notação `with`')
st.subheader('Cafeteira')

with st.form('my_form'):
    st.subheader('**Escolha seu café**')
    
    # Componentes de entrada
    coffee_bean_val = st.selectbox('Grão', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Torra', ['Clara', 'Média', 'Escura'])
    brewing_val = st.selectbox('Método', ['Aeropress', 'Filtrado', 'Prensa Francesa', 'Cafeteira Italiana', 'Globo'])
    serving_type_val = st.selectbox('Formato', ['Quente', 'Gelado', 'Frapê'])
    milk_val = st.select_slider('Leite', ['Não', 'Pouco', 'Médio', 'Muito'])
    owncup_val = st.checkbox('Trouxe o meu copo!')
    
    # Todo formulário deve ter um botão enviar
    submitted = st.form_submit_button('Enviar')

if submitted:
    st.markdown(f'''
        ☕ Você pediu:
        - Grão: `{coffee_bean_val}`
        - Torra: `{coffee_roast_val}`
        - Método: `{brewing_val}`
        - Formato: `{serving_type_val}`
        - Leite: `{milk_val}`
        - Trouxe o meu copo: `{owncup_val}`
        ''')
else:
    st.write('☝️ Faça o seu pedido!')


# Pequeno exemplo usando objeto
st.header('2. Exemplo com objeto')

form = st.form('my_form_2')
selected_val = form.slider('Escolha um valor')
form.form_submit_button('Enviar')

st.write('Valor escolhido: ', selected_val)
```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.title('st.form')
```

### Primeiro exemplo
Vamos começar com o primeiro exemplo, aqui vamos aplicar o comando `st.form` através da notação `with`. Dentro do formulário, começaremos escrevendo um subtítulo `Escolha seu café` e então criaremos vários componentes de entrada (`st.selectbox`, `st.select_slider` e `st.checkbox`) para coletar informações sobre o pedido de café. Finalmente, um botão de envio é criado através do comando `st.form_submit_button`, que quando clicado enviará todas as informações do usuário, como um único lote de informações para a aplicação processar..

```python
# Exemplo completo usando a notação with
st.header('1. Exemplo usando a notação `with`')
st.subheader('Cafeteira')

with st.form('my_form'):
    st.subheader('**Escolha seu café**')
    
    # Componentes de entrada
    coffee_bean_val = st.selectbox('Grão', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Torra', ['Clara', 'Média', 'Escura'])
    brewing_val = st.selectbox('Método', ['Aeropress', 'Filtrado', 'Prensa Francesa', 'Cafeteira Italiana', 'Globo'])
    serving_type_val = st.selectbox('Formato', ['Quente', 'Gelado', 'Frapê'])
    milk_val = st.select_slider('Leite', ['Não', 'Pouco', 'Médio', 'Muito'])
    owncup_val = st.checkbox('Trouxe o meu copo!')
    
    # Todo formulário deve ter um botão enviar
    submitted = st.form_submit_button('Enviar')
```

Em seguida, vamos adicionar a lógica do que acontece depois que o botão de envio é clicado. Por padrão, sempre que a aplicação Streamlit for carregada, a instrução `else` será executada e veremos a mensagem `☝️ Faça o seu pedido!`. Considerando que, ao clicar no botão enviar, todas as informações fornecidas pelo usuário (através dos componentes) são armazenadas em variáveis ​​(por exemplo, `coffee_bean_val`, `coffee_roast_val`, etc.) e exibidas através do comando `st.markdown` com a ajuda de `f-strings`.

```python
if submitted:
    st.markdown(f'''
        ☕ Você pediu:
        - Grão: `{coffee_bean_val}`
        - Torra: `{coffee_roast_val}`
        - Método: `{brewing_val}`
        - Formato: `{serving_type_val}`
        - Leite: `{milk_val}`
        - Trouxe o meu copo: `{owncup_val}`
        ''')
else:
    st.write('☝️ Faça o seu pedido!')
```


### Segundo exemplo

Vamos agora prosseguir para o segundo exemplo usando o `st.form` como uma notação de objeto. Aqui, o comando `st.form` é atribuído à variável `form`. Em seguida, vários comandos Streamlit como `slider` ou `form_submit_button` são aplicados na variável `form`.

```python
# Pequeno exemplo usando objeto
st.header('2. Exemplo com objeto')

form = st.form('my_form_2')
selected_val = form.slider('Escolha um valor')
form.form_submit_button('Enviar')

st.write('Valor escolhido: ', selected_val)
```

## Leitura complementar
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [Introdução a formulários e botão de envio](https://blog.streamlit.io/introducing-submit-button-and-forms/)
