# Configurando tu entorno de desarrollo local

Antes de empezar a desarrollar nuestras aplicaciones, vamos a necesitar primero configurar el entorno de desarrollo.

Comencemos instalando y configurando el entorno Conda. 

## **Instalar conda**
- Para instalar `conda` diríjase a https://docs.conda.io/en/latest/miniconda.html y seleccione su sistema operativo (Windows, Mac o Linux). 
- Descargue y ejecute el instalador para instalar `conda`.

## **Crear un nuevo entorno conda**
Una vez que haz instalado conda, comencemos creando un entorno para gestionar todas las dependencias de la librería Python.

Para crear un nuevo entorno con Python 3.9, ejecute lo siguiente:
```bash
conda create -n stenv python=3.9
```

donde `create -n stenv` va a crear un entorno conda llamado `stenv` y `python=3.9` va a especificar que se utilice la version 3.9 de Python en el entorno conda.

## **Activar el entorno conda**

Para utilizar el entorno conda llamado `stenv` que acabamos de crear, ejecute lo siguiente en su terminal:

```bash
conda activate stenv
```

## **Instalar la librería Streamlit**

Es tiempo de instalar la librería `streamlit`:
```bash
pip install streamlit
```

## **Ejecutar la aplicación demo de Streamlit**
Para ejecutar la aplicación demo (Figura 1) ingrese:
```bash
streamlit hello
```
