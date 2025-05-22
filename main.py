import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(page_title="나의 소개", page_icon="👤", layout="centered")

# ====== 여기에 정보를 입력하세요 ======
name = "이성호"
school = "영동일고등학교"
hobby = "바이브코딩, 입코딩"
email = "windowsp@ydi.hs.kr"
photo_path = "my_photo.jpg"  # 같은 폴더에 있는 이미지 파일명 (예: jpg, png)
# =====================================

# 스타일
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
    .profile-box {
        background-color: #fdfdfd;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목
st.markdown('<div class="title">👤 나의 소개 페이지</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">개인 프로필을 확인해보세요</div>', unsafe_allow_html=True)

# 프로필 박스
st.markdown('<div class="profile-box">', unsafe_allow_html=True)

st.markdown(f"### 🙋‍♂️ 이름: {name}")
st.markdown(f"🏫 학교: {school}")
st.markdown(f"🎯 취미: {hobby}")
st.markdown(f"📧 이메일: {email}")

# 이미지 표시
try:
    img = Image.open(photo_path)
    st.image(img, width=250, caption="내 사진")
except FileNotFoundError:
    st.warning("사진 파일을 찾을 수 없습니다. 사진 파일이 코드와 같은 폴더에 있는지 확인해주세요.")

st.markdown('</div>', unsafe_allow_html=True)
