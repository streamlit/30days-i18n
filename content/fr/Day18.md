# st.file_uploader

`st.file_uploader` affiche un widget qui vous permet d'uploader des fichiers [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

Par défaut, les fichiers uploadés sont limités à `200` Mo. Néanmoins, vous pouvez configurer l'uploader à l'aide de l'option  `server.maxUploadSize`. Pour plus d'informations sur les options de configuration, consultez [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## Code
Voici comment utiliser `st.file_uploader` :
```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Explication ligne par ligne

La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st`, ainsi que les autres bibliothèques requises, comme suit :

```python
import streamlit as st
import pandas as pd
```

Ensuite, créons un titre pour l'application :
```python
st.title('st.file_uploader')
```

Maintentenant, utilisons `st.file_uploader` :
```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

Enfin, définissons des instructions conditionnelles (`if`/`else`) pour afficher un message de bienvenue invitant les utilisateurs à uploader leurs fichiers.

Lors de l'upload du fichier, les instructions du bloc `if` sont activées, le fichier CSV est lu par la bibliothèque Pandas, et affiché via la commande `st.write`:

```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Lectures complémentaires
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [Définir les options de configuration](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)