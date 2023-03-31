# Configurando o seu ambiente local de desenvolvimento

Antes de começarmos a desenvolver aplicações com Streamlit, primeiro vamos configurar o nosso ambiente de desenvolvimento

Vamos começar instalando e configurando um ambiente conda.

## **Instalando conda**
- Para instalar o `conda` abra o site https://docs.conda.io/en/latest/miniconda.html e escolha o seu sistema operacional (Windows, Mac ou Linux). 
- Faça o download e rode o instalador.

## **Criando um novo ambiente conda**
Agora que o conda está instalado, vamos criar um ambiente conda para gerenciar todas as dependências de bilbiotecas python.

Para criar um ambiente com o Python 3.9, use o seguinte comando:
```bash
conda create -n stenv python=3.9
```

onde `create -n stenv` vai criar um ambiente conda chamado `stenv` e `python=3.9` vai configurar o ambiente para usar a versão 3.9 do Python.

## **Ativando o ambiente conda**

Para usar o ambiente conda que acabamos de criar, chamado `stenv`, use o seguinte comando:

```bash
conda activate stenv
```

## **Instalando a biblioteca Streamlit**

Agora vamos instalar a biblioteca `streamlit`:
```bash
pip install streamlit
```

## **Inciando a aplicação de demonstração do Streamlit**
Para iniciar a aplicação de demonstração (Figura 1), use o seguinte comando:
```bash
streamlit hello
```
