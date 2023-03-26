# 使用方法

1. 在对应的文件夹打开控制台

2. 输入`streamlit run webui.py`

3. 直接运行，使用即可

<font color=gray>注意，使用之前你需要从Hugging Face下载使用到的模型，在这里只提供一个链接 [中译英](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en) 以及 [英译中](https://huggingface.co/Helsinki-NLP/opus-mt-en-zh) ，下载好了以后，你只需要把对应的文件夹放入model文件夹中即可</font>

# 报错了？

1. 首先，确保你安装了Python，我的版本是`3.10.9`

2. 在当前目录打开控制台，并输入`pip install -r requirements.txt`来安装需要的包

3. 再次尝试运行`streamlit run webui.py`

如果还是报错，请查看是否是自己电脑的问题。

<font color=red>注意，本程序不需要使用互联网，是本地运行的，如果运行缓慢，说明电脑配置较低；如果申请互联网，立刻删除软件</font>