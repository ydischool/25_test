import streamlit as st
from PIL import Image

st.set_page_config(page_title="나의 소개", page_icon="👤", layout="centered")

st.markdown(
    """
    <style>
    .title {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 40px;
    }
    .section {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">👤 나의 소개 페이지</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">자기소개를 입력해 보세요</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)

    name = st.text_input("이름")
    school = st.text_input("학교")
    hobby = st.text_input("취미")
    email = st.text_input("이메일")
    photo = st.file_uploader("사진 업로드", type=["jpg", "jpeg", "png"])

    st.markdown("</div>", unsafe_allow_html=True)

    if all([name, school, hobby, email]):
        st.markdown("## ✨ 나의 프로필")
        st.markdown(f"- **이름:** {name}")
        st.markdown(f"- **학교:** {school}")
        st.markdown(f"- **취미:** {hobby}")
        st.markdown(f"- **이메일:** {email}")
        if photo:
            img = Image.open(photo)
            st.image(img, width=200, caption="내 사진")

    else:
        st.info("모든 정보를 입력하면 프로필이 보여집니다.")
