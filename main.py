import streamlit as st


st.set_page_config(page_title="First Streamlit App")

st.title("AI 협업 개발 실습")
st.write("첫 번째 Streamlit 앱입니다.")

st.divider()
st.write("아래에 이름을 입력하고 실습을 시작해보세요.")

name = st.text_input("이름을 입력하세요")

if st.button("실습 시작"):
    if name:
        st.write(f"{name}님, 환영합니다! 실습을 시작해보세요.")
    else:
        st.write("이름을 입력한 뒤 실습 시작 버튼을 눌러주세요.")
