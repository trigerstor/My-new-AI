import streamlit as st

st.title("AI大模型应用产品网")
col, col1 = st.columns(2)

# 语言大模型应用程序功能入口
with col:
    st.image(
        "https://haowallpaper.com/link/common/file/previewFileImg/15691092177686848",
        use_column_width=True)
    flag = st.button("慧言")
    if flag:
        st.switch_page("pages/demo3.py")

with col1:
    st.image(
        "https://haowallpaper.com/link/common/file/previewFileImg/15691092177686848",
        use_column_width=True)
    flag = st.button("绘图")
    if flag:
        st.switch_page("pages/textToimage.py")