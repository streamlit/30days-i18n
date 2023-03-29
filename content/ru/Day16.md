# День 16

# **Настройка темы приложений Streamlit**

Мы можем настроить тему, настроив параметры в `config.toml`, который представляет собой файл конфигурации хранящийся в той же папке что и приложение—в папке `.streamlit`.

## **Что мы строим?**

Простое приложение, которое показывает результат настройки нашей темы. Это стало возможным благодаря настройке HTML HEX-кода внутри [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) файла.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## **Код**

Вот код файла `[streamlit_app.py](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py)`:

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

Вот код файла [.streamlit/config.toml](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml):

```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
```

Затем следует создание текста заголовка для приложения:
```python
st.title('Theming with config.toml')
```

Далее мы собираемся показать содержимое файла `.streamlit/config.toml`, в котором мы сначала отобразим примечание через `st.write`, а затем сам код через `st.code`:

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

Наконец, мы создаем виджет slider на боковой панели, после чего отображается выбранный номер:
```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Теперь давайте посмотрим на пользовательские цвета, которые мы использовали в этом приложении, указанные в файле `.streamlit/config.toml`:

- `primaryColor="#F39C12"` – Это устанавливает оранжевый как основной цвет. Обратите внимание на оранжевые цвета в виджете slider.
- `backgroundColor="#2E86C1"` – Это устанавливает синий цвет фона. Обратите внимание, что основная панель имеет синий цвет фона.
- `secondaryBackgroundColor="#AED6F1"` – Это устанавливает темно-серый цвет вторичного фона. Обратите внимание на серый цвет фона боковой панели и цвет фона поля кода на главной панели.
- `textColor="#FFFFFF"` – Это устанавливает белый цвет текста.
- `font="monospace"` – Это устанавливает моноширинный шрифт.

## **Дальнейшее чтение**

- [Тематика](https://docs.streamlit.io/library/advanced-features/theming)
- [Цветовые коды HTML](https://htmlcolorcodes.com/) это отличный инструмент для выбора цветов.
