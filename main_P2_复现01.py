# import streamlit as st
# from utils_P2_复现01 import generate_xiaohongshu
#
# st.header("小红书文案生成器")
#
# with st.sidebar:
#     openai_api_key = st.text_input("请输入您的OPENAI API 密钥：",type="password"),
#     st.markdown("[点击获取DASHSCOPE密钥](https://aliyun.com/account/api-keys)")
#
# theme = st.text_input("请输入您的小红书主题")
# submit = st.button("开始创作")
#
# if submit and not openai_api_key:
#     st.info("请输入您的DASHSCOPE密钥")
#     st.stop()
# if submit and not theme:
#     st.info("请输入小红书的主题")
#     st.stop()
# if submit:
#     with st.spinner("你的小红书标题和正文正在生成中，请稍候"):
#         result = generate_xiaohongshu(theme, openai_api_key)
#         st.divider()
#     column1,column2=st.columns(2)
#     with column1:
#         st.markdown("#### 小红书标题1")
#         st.write(result.titles[0])
#         st.markdown("#### 小红书标题2")
#         st.write(result.titles[1])
#         st.markdown("#### 小红书标题3")
#         st.write(result.titles[2])
#         st.markdown("#### 小红书标题4")
#         st.write(result.titles[3])
#         st.markdown("#### 小红书标题5")
#         st.write(result.titles[4])
#     with column2:
#         st.markdown("小红书正文")
#         st.write(result.content)

import streamlit as st

from utils_P2_复现01 import generate_xiaohongshu


st.header("爆款小红书AI写作助手 ✏️")
with st.sidebar:
    api_key = st.text_input("请输入dashscope密钥：", type="password")
    st.markdown("[获取dashscope API密钥](https://platform.openai.com/account/api-keys)")

theme = st.text_input("主题")
submit = st.button("开始写作")

if submit and not api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not theme:
    st.info("请输入生成内容的主题")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_xiaohongshu(theme, api_key)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("##### 小红书标题1")
        st.write(result.titles[0])
        st.markdown("##### 小红书标题2")
        st.write(result.titles[1])
        st.markdown("##### 小红书标题3")
        st.write(result.titles[2])
        st.markdown("##### 小红书标题4")
        st.write(result.titles[3])
        st.markdown("##### 小红书标题5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### 小红书正文")
        st.write(result.content)
