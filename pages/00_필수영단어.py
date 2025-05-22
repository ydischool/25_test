import streamlit as st
import random

# 단어 리스트 (영단어, 뜻)
words = [
    ("analyze", "분석하다"),
    ("approach", "접근하다; 접근"),
    ("assume", "추정하다, 가정하다"),
    ("benefit", "이익, 혜택; 이익을 주다"),
    ("claim", "주장하다; 요구하다"),
    ("compare", "비교하다"),
    ("condition", "조건; 상태"),
    ("confirm", "확인하다"),
    ("consider", "고려하다"),
    ("contribute", "기여하다; 원인이 되다"),
    ("critical", "비판적인; 중요한"),
    ("define", "정의하다"),
    ("demonstrate", "증명하다; 시위하다"),
    ("determine", "결정하다; 알아내다"),
    ("effective", "효과적인"),
    ("emphasize", "강조하다"),
    ("environment", "환경"),
    ("estimate", "추정하다; 견적"),
    ("evidence", "증거"),
    ("examine", "조사하다; 시험하다"),
    ("experiment", "실험"),
    ("explain", "설명하다"),
    ("factor", "요소"),
    ("focus", "집중하다; 초점"),
    ("generate", "발생시키다"),
    ("identify", "확인하다; 동일시하다"),
    ("impact", "영향"),
    ("imply", "암시하다"),
    ("indicate", "나타내다, 가리키다"),
    ("individual", "개인; 개인의"),
    ("influence", "영향; 영향을 미치다"),
    ("maintain", "유지하다"),
    ("mention", "언급하다"),
    ("occur", "발생하다"),
    ("participate", "참여하다"),
    ("policy", "정책"),
    ("potential", "잠재력; 잠재적인"),
    ("predict", "예측하다"),
    ("prevent", "막다, 예방하다"),
    ("propose", "제안하다"),
    ("prove", "증명하다"),
    ("provide", "제공하다"),
    ("range", "범위; 다양성"),
    ("reduce", "줄이다"),
    ("reflect", "반영하다; 반사하다"),
    ("require", "요구하다"),
    ("respond", "반응하다"),
    ("significant", "중요한, 의미 있는"),
    ("source", "근원, 출처"),
    ("support", "지지하다; 지원"),
    ("vary", "다르다; 변화를 주다"),
]

# 명언 리스트
quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "You are capable of amazing things.",
    "Push yourself, because no one else is going to do it for you."
]

# 앱 제목과 명언
st.title("📘 고3 필수 영단어 퀴즈")
st.markdown(f"> 💡 *{random.choice(quotes)}*")

# 상태 초기화
if 'quiz' not in st.session_state:
    st.session_state.quiz = random.sample(words, 10)
    st.session_state.user_answers = [""] * 10
    st.session_state.submitted = False

# 문제 풀이
st.write("다음 단어의 뜻을 한국어로 고르세요:")

for i, (eng, kor) in enumerate(st.session_state.quiz):
    st.text_input(f"{i+1}. {eng}", key=f"answer_{i}")

# 제출 버튼
if st.button("제출하기"):
    st.session_state.user_answers = [st.session_state[f"answer_{i}"].strip() for i in range(10)]
    st.session_state.submitted = True

# 결과 표시
if st.session_state.submitted:
    correct = 0
    st.subheader("📊 결과")
    for i, (eng, kor) in enumerate(st.session_state.quiz):
        user = st.session_state.user_answers[i]
        if user == kor:
            st.markdown(f"✅ {i+1}. {eng} - {user}")
            correct += 1
        else:
            st.markdown(f"❌ {i+1}. {eng} - 당신의 답: {user} / 정답: {kor}")
    st.success(f"총 {correct}개 맞았습니다! 🎉")

    if st.button("다시 풀기"):
        st.session_state.quiz = random.sample(words, 10)
        st.session_state.user_answers = [""] * 10
        st.session_state.submitted = False

