import streamlit as st


st.set_page_config(page_title="First Streamlit App", page_icon="🤝", layout="centered")

st.title("AI 협업 개발 실습")
st.write("첫 번째 Streamlit 앱입니다.")

user_name = st.text_input("이름을 입력하세요", placeholder="예: SeungMin")

if user_name:
    st.success(f"환영합니다, {user_name}님.")
else:
    st.info("이름을 입력하면 환영 메시지가 표시됩니다.")
