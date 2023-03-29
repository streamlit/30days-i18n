# Customizing the theme of Streamlit apps

We can customize the theme by adjusting parameters in `config.toml`, which is a configuration file stored in the same folder as the app in the `.streamlit` folder.

## What we're building?

A simple app that shows the result of our theme customization. This is made possible by customizing the HTML HEX code inside the [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) file.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## Code
Here's the code to the [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py) file:
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

Here's the code to the [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) file:
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

This is followed by creating a title text for the app:
```python
st.title('Theming with config.toml')
```

Next, we're going to show the contents of the `.streamlit/config.toml` file which we'll first display a note of this via `st.write` followed by the actual code via `st.code`:
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

Finally, we're creating a slider widget in the sidebar followed by displaying the selected number:
```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Let's now take a look at the custom colors that we've used in this app, which is specified in the `.streamlit/config.toml` file:
- `primaryColor="#F39C12"` - This sets the primary color to orange. Notice the orange colors in the slider widget.
- `backgroundColor="#2E86C1"` - This sets the background color to blue. Notice the main panel has a blue background color.
- `secondaryBackgroundColor="#AED6F1"` - This sets the secondary background color to dark gray. Notice the gray background color of the sidebar and the background color of the code box in the main panel.
- `textColor="#FFFFFF"` - The text color is set to white.
- `font="monospace"` - This sets the font to monospace.


## Further reading
- [Theming](https://docs.streamlit.io/library/advanced-features/theming)
- [HTML Color Codes](https://htmlcolorcodes.com/) is a great tool for selecting colors of interest.
