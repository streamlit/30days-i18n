# st.secrets

`st.secrets` vous permet de stocker des informations confidentielles telles que des clés API, des mots de passe de base de données ou d'autres informations d'identification.

## Démo

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## Code
Voici comment utiliser `st.secrets` :
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Ensuite, créons un titre pour l'application :
```python
st.title('st.secrets')
```

Enfin, nous afficherons les secrets stockés :
```python
st.write(st.secrets['message'])
```

Il convient de noter que les secrets peuvent être stockés dans Streamlit Community Cloud, comme indiqué dans les captures d'écran ci-dessous.

Si vous travaillez localement, ils peuvent être stockés dans `.streamlit/secrets.toml`, mais évitez de les télécharger sur un repo GitHub lors du déploiement!

## Lectures complémentaires
- [Ajouter des secrets à vos applications Streamlit](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [Gestion des secrets](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)