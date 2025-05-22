import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="🌟 MBTI 직업 추천기",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #f72585;">🌈 MBTI 기반 직업 추천기 💼</h1>
        <h3 style="color: #7209b7;">당신의 성격에 딱 맞는 직업은? 지금 바로 확인해보세요! 🎯</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# 👉 MBTI 목록
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 🎯 추천 직업 매핑
mbti_jobs = {
    "ISTJ": ["🕵️‍♂️ 회계사", "👨‍⚖️ 공무원", "🏦 금융 분석가"],
    "ISFJ": ["🧑‍🏫 교사", "👩‍⚕️ 간호사", "🏠 사회복지사"],
    "INFJ": ["🎨 예술가", "🧠 심리상담사", "✍️ 작가"],
    "INTJ": ["🧪 과학자", "🧠 전략가", "💻 데이터 분석가"],
    "ISTP": ["🔧 기술자", "🚓 경찰", "🚗 자동차 정비사"],
    "ISFP": ["🎵 음악가", "📸 사진작가", "🌿 플로리스트"],
    "INFP": ["📚 소설가", "🎭 배우", "🧘‍♀️ 명상 지도자"],
    "INTP": ["👨‍💻 개발자", "🔬 연구원", "♟ 철학자"],
    "ESTP": ["🕺 이벤트 플래너", "📢 마케터", "💼 세일즈맨"],
    "ESFP": ["🎤 가수", "🎬 배우", "👠 패션 디자이너"],
    "ENFP": ["🎯 창업가", "🧗 활동가", "🎨 콘텐츠 크리에이터"],
    "ENTP": ["💡 발명가", "📺 방송인", "🧠 기획자"],
    "ESTJ": ["🏢 관리자", "👮‍♂️ 군인", "⚖️ 법률가"],
    "ESFJ": ["🧑‍🏫 교사", "👨‍🍳 셰프", "💁‍♀️ 고객 서비스 담당자"],
    "ENFJ": ["🌍 NGO 활동가", "🎤 연설가", "🎓 교육자"],
    "ENTJ": ["📈 CEO", "⚙️ 엔지니어", "💡 기획 관리자"]
}

# 👉 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 🔍", mbti_list)

if selected_mbti:
    st.markdown("## 🧑‍🚀 추천 직업 리스트")
    st.success(f"**{selected_mbti}** 타입에게 어울리는 직업은 다음과 같아요! 🚀")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

    st.balloons()

# 👇 하단 푸터
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 14px; color: gray;">
        만든이: 🧑‍💻 <b>당신의 이름</b> | 교육용 앱입니다 🎓<br>
        Powered by <a href="https://streamlit.io" target="_blank">Streamlit</a> 🚀
    </div>
    """,
    unsafe_allow_html=True
)
