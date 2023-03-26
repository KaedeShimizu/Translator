# 使用的是Streamlit 来构建用户界面
# 主要是因为这个会方便很多
import streamlit as st

from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer

# 网页标题
st.title("中-英互译")
st.text("by Kaede")

# 提供一个选择框,每次选择重新加载对应模型
select = st.selectbox("选择语言", ["中-英", "英-中"])
if select == "中-英":
    model = AutoModelWithLMHead.from_pretrained("model/opus-mt-zh-en")
    tokenizer = AutoTokenizer.from_pretrained("model/opus-mt-zh-en")
    translation = pipeline("translation_zh_to_en", model=model, tokenizer=tokenizer)
elif select == "英-中":
    model = AutoModelWithLMHead.from_pretrained("model/opus-mt-en-zh")
    tokenizer = AutoTokenizer.from_pretrained("model/opus-mt-en-zh")
    translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)


# 给一个翻译函数,用来吧内容翻译到需要的语言
def get_translate(Itext):
    return translation(Itext, max_length=40)[0]['translation_text']


# 输入框
text = st.text_input("需要翻译的内容", placeholder="输入需要翻译的内容")
# 输出内容
f"> {get_translate(text)}"
