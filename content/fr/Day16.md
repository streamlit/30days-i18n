# Personnalisez le thème de vos applications Streamlit

Nous pouvons personnaliser le thème de l'app (c'est à dire les couleurs et la police de caractère) en ajustant les paramètres dans le fichier `config.toml`, qui est un fichier de configuration stocké dans le dossier `.streamlit`.

## Que construisons nous ?

Une app qui montre comment personnaliser vos thèmes. Ceci est possible en modifiant une ou plusieurs lignes de codes HEX à l'intérieur du fichier [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml).

## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## Code
Voici le code qui se trouve dans le fichier [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py) :
```python
import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Voici le code se trouvant dans [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) :
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Ensuite, créons un titre pour l'application :
```python
st.title('Theming with config.toml')
```

Maintenant, nous allons afficher le contenu du fichier `.streamlit/config.toml` via `st.write`, suivi de la commande `st.code` :

```python
st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

Enfin, créons un slider dans la barre latérale et affichons le nombre sélectionné :

```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Constatons les couleurs personnalisées que nous avons creé, spécifiées dans le fichier `.streamlit/config.toml` :
- `primaryColor="#F39C12"` - Définit la couleur primaire `orange`. Notez la couleur `orange` du slider.
- `backgroundColor="#2E86C1"` - Définit la couleur d'arrière-plan: `bleu`. Notez que le panneau principal est désormais de couleur bleue.
- `secondaryBackgroundColor="#AED6F1"` - Définit la couleur d'arrière-plan (ou secondaire): `gris foncé`. Remarquez la couleur d'arrière-plan grise de la barre latérale.
- `textColor="#FFFFFF"` - Définit la couleur texte, ici `blanc`.
- `font="monospace"` - Définit la police de caractère, ici `monospace`.


## Lectures complémentaires
- [Theming](https://docs.streamlit.io/library/advanced-features/theming)
- [HTML Color Codes](https://htmlcolorcodes.com/) est un excellent outil pour sélectionner les couleurs qui vous intéressent.