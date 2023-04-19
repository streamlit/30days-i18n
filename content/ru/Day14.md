# День 14

# **Компоненты Streamlit**

Компоненты—это сторонние модули для Python, расширяющие возможности Streamlit [[1](https://docs.streamlit.io/library/components)].

## **Какие компоненты Streamlit доступны?**

На сайте Streamlit [[2](https://streamlit.io/components)] представлено несколько десятков компонентов Streamlit.

Фанило (Streamlit Creator) курировал удивительный список компонентов Streamlit в вики-сообщении [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)], в котором перечислены около 85 компонентов Streamlit по состоянию на апрель 2022 года.

## **Как использовать?**

Компоненты Streamlit находятся всего в нескольких шагах от установки.

В этом руководстве мы познакомим вас с использованием компонента streamlit_pandas_profiling [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

### **Установить компонент**

```bash
pip install streamlit_pandas_profiling
```

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## **Код**

Как создать приложение Streamlit с помощью компонента:

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, а также другие библиотеки используемые в приложении, следующим образом:

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

Затем следует создание текста заголовка для приложения:

```python
st.header('`streamlit_pandas_profiling`')
```

Затем мы загружаем набор данных Penguins с помощью команды read_csv для pandas.

```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

Наконец, отчет о профилировании pandas создается с помощью команды `profile_report()` и отображается с помощью `st_profile_report`:

```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## **Создание собственных компонентов**

Если вы заинтересованы в создании собственного компонента, ознакомьтесь со следующими ресурсами:

- [Создать компонент](https://docs.streamlit.io/library/components/create)
- [Опубликовать компонент](https://docs.streamlit.io/library/components/publish)
- [API компонентов](https://docs.streamlit.io/library/components/components-api)
- [Блог о компонентах](https://blog.streamlit.io/introduction-streamlit-components/)

В качестве альтернативы, если вы предпочитаете учиться с помощью видео, наш инженер Тим Конклинг сделал несколько замечательных руководств:

- [Как создать компонент Streamlit | Часть 1: Настройка и архитектура](https://youtu.be/BuD3gILJW-Q)
- [Как создать компонент Streamlit | Часть 2: Часть 2: Создание виджета-слайдера](https://youtu.be/QjccJl_7Jco)

## **Дополнительная информация о компонентах**

1. [Компоненты Streamlit — Документация по API](https://docs.streamlit.io/library/components)
2. [Избранные компоненты Streamlit](https://streamlit.io/components) 
3. [Компоненты Streamlit — трекер сообщества](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)
