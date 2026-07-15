import streamlit as st
import random

st.set_page_config(
    page_title="💖 MBTI 캐릭터 추천",
    page_icon="🌸",
    layout="centered"
)

st.title("🌸 MBTI 캐릭터 & 직업 추천 🌸")
st.markdown("### 🩷 나의 MBTI에 어울리는 귀여운 캐릭터와 직업을 찾아보자!")

mbti_data = {
    "INTJ": {
        "character": "🦊 지혜로운 여우",
        "jobs": ["변호사", "정책연구원", "데이터 분석가"]
    },
    "INTP": {
        "character": "🦉 호기심 많은 부엉이",
        "jobs": ["프로그래머", "연구원", "대학교수"]
    },
    "ENTJ": {
        "character": "🦁 당당한 사자",
        "jobs": ["행정공무원", "CEO", "기획자"]
    },
    "ENTP": {
        "character": "🐵 장난꾸러기 원숭이",
        "jobs": ["마케팅 전문가", "창업가", "변호사"]
    },
    "INFJ": {
        "character": "🦄 신비로운 유니콘",
        "jobs": ["상담사", "사회복지사", "작가"]
    },
    "INFP": {
        "character": "🐰 말랑말랑 토끼",
        "jobs": ["작가", "일러스트레이터", "심리상담사"]
    },
    "ENFJ": {
        "character": "🐼 다정한 판다",
        "jobs": ["교사", "공무원", "인사담당자"]
    },
    "ENFP": {
        "character": "🦋 자유로운 나비",
        "jobs": ["유튜버", "광고기획자", "기자"]
    },
    "ISTJ": {
        "character": "🐻 성실한 곰",
        "jobs": ["경찰관", "공무원", "회계사"]
    },
    "ISFJ": {
        "character": "🐹 따뜻한 햄스터",
        "jobs": ["간호사", "사회복지사", "초등교사"]
    },
    "ESTJ": {
        "character": "🐯 듬직한 호랑이",
        "jobs": ["행정공무원", "경찰간부", "기업 관리자"]
    },
    "ESFJ": {
        "character": "🐥 상냥한 병아리",
        "jobs": ["승무원", "간호사", "교사"]
    },
    "ISTP": {
        "character": "🐺 멋진 늑대",
        "jobs": ["파일럿", "엔지니어", "경찰특공대"]
    },
    "ISFP": {
        "character": "🐱 귀여운 고양이",
        "jobs": ["디자이너", "사진작가", "플로리스트"]
    },
    "ESTP": {
        "character": "🐸 씩씩한 개구리",
        "jobs": ["소방관", "경찰관", "운동선수"]
    },
    "ESFP": {
        "character": "🐧 사랑스러운 펭귄",
        "jobs": ["배우", "MC", "이벤트 기획자"]
    }
}

mbti = st.selectbox(
    "✨ MBTI를 선택하세요!",
    list(mbti_data.keys())
)

if st.button("🎁 결과 보기"):
    st.balloons()
    st.snow()

    info = mbti_data[mbti]

    st.success(f"🎉 당신의 MBTI는 **{mbti}**!")

    st.markdown("---")

    st.header("🧸 어울리는 캐릭터")
    st.markdown(f"## {info['character']}")

    st.markdown("---")

    st.header("💼 추천 직업 TOP 3")

    for i, job in enumerate(info["jobs"], 1):
        emoji = random.choice(["🌟", "💖", "✨", "🎈", "🍀"])
        st.markdown(f"### {emoji} {i}. {job}")

    st.markdown("---")

    st.info("🌈 자신만의 강점을 살려 꿈을 향해 도전해 보세요! 💕")

    st.markdown("## 🩷 오늘의 응원 한마디")
    messages = [
        "🌸 오늘도 반짝이는 하루가 될 거예요!",
        "🍀 당신의 가능성은 무한합니다!",
        "💖 자신감을 가지고 도전해 보세요!",
        "🌟 당신은 분명 멋진 미래를 만들어 갈 거예요!",
        "🦄 꿈을 향해 한 걸음씩 나아가 보세요!"
    ]
    st.success(random.choice(messages))
