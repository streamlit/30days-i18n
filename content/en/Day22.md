# st.form

`st.form` creates a form that batches elements together with a "Submit" button.

Typically, whenever a user interacts with a widget, the Streamlit app is rerun.

A form is a container that visually groups other elements and widgets together, and contains a Submit button. Herein, a user can interacts with one or more widgets for as many times as they like without causing a rerun. Finally, when the form's Submit button is pressed, all widget values inside the form will be sent to Streamlit in a single batch.

To add elements to a form object, you can use the `with` notation (preferred) or you could use it as an object notation by just calling methods directly on the form (by first assigning it to a variable and subsequently applying Streamlit methods on it). See in the example app.

Forms have a few constraints:
- Every form must contain a `st.form_submit_button`.
- `st.button` and `st.download_button` cannot be added to a form.
- Forms can appear anywhere in your app (sidebar, columns, etc), but they cannot be embedded inside other forms.

For more information about forms, check out our [blog post](https://blog.streamlit.io/introducing-submit-button-and-forms/).

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## Code
Here's how to use `st.form`:
```python
import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

This is followed by creating a title text for the app:
```python
st.title('st.form')
```

### First example
Let's start with the first example, here we'll apply the `st.form` command via the `with` notation. Inside the form, we'll start with writing a subheader `Order your coffee` then create several input widgets (`st.selectbox`, `st.select_slider` and `st.checkbox`) to collect information about the coffee order. Finally, a submit button is created via the `st.form_submit_button` command, which when clicked on will send all user input as a single batch of information to the app for processing.
```python
# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
```

Next, we'll add the logic of what happen's after the submit button is clicked on. By default, whenever the Streamlit app is loaded the `else` statement will be run and we see a message `☝️ Place your order!`. Whereas upon clicking on the submit button, all user provided input via the various widgets are stored in several variables (e.g. `coffee_bean_val`, `coffee_roast_val`, etc.) and printed out via the `st.markdown` command with the help of f-string.
```python
if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')
```


### Second example
Let's now proceed to the second example on using the `st.form` as an object notation. Here, the `st.form` command is assigned to the `form` variable. Subsequently, various Streamlit commands such as `slider` or `form_submit_button` is applied on the `form` variable.
```python
# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## Further reading
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [Introducing Submit button and Forms](https://blog.streamlit.io/introducing-submit-button-and-forms/)
