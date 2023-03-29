# 设置本地开发环境

在我们正式开始构建 Streamlit 应用之前，我们需要首先设置一个开发环境。

让我们从安装和配置 conda 环境开始。

## **安装 conda**

- 前往 https：//docs.conda.io/en/latest/miniconda.html ，选择与你操作系统（Windows, Mac 或 Linux）对应的 `conda` 版本
- 下载安装器并运行，完成 `conda` 的安装

## **新建一个 conda 环境**

现在你已经装好了 conda ，让我们来创建一个 conda 环境来管理所有 Python 库依赖。

比如按照如下指令，使用 Python 3.9 版本创建一个新的环境：

```bash
conda create -n stenv python=3.9
```

其中 `create -n stenv` 表示创建一个名为 `stenv` 的 conda 环境，而 `python=3.9` 会指定 conda 环境使用 3.9 版本的 Python。

## **激活 conda 环境**

要使用上一步刚创建好的名为 `stenv` 的 conda 环境，则需要使用如下的命令：

```bash
conda activate stenv
```

## **安装 Streamlit 库**

激活环境之后就是时候安装 `streamlit` 库了：

```bash
pip install streamlit
```

## **启动示例 Streamlit 应用**

用如下指令来启动示例 Streamlit 应用（图 1）：

```bash
streamlit hello
```
