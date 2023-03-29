# Setting up a local development environment

Before we can actually start building Streamlit apps, we will first have to setup a development environment.

Let's start by installing and setting up a conda environment.

## **Install conda**
- Install `conda` by going to https://docs.conda.io/en/latest/miniconda.html and choose your operating system (Windows, Mac or Linux). 
- Download and run the installer to install `conda`.

## **Create a new conda environment**
Now that you have conda installed, let's create a conda environment for managing all the Python library dependencies.

To create a new environment with Python 3.9, enter the following:
```bash
conda create -n stenv python=3.9
```

where `create -n stenv` will create a conda environment named `stenv` and `python=3.9` will setup the conda environment with Python version 3.9.

## **Activate the conda environment**

To use a conda environment that we had just created that is named `stenv`, enter the following into the command line:

```bash
conda activate stenv
```

## **Install the Streamlit library**

It's now time to install the `streamlit` library:
```bash
pip install streamlit
```

## **Launching the Streamlit demo app**
To launch the Streamlit demo app (Figure 1) type:
```bash
streamlit hello
```
