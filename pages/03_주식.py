import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

# 시가총액 Top 10 티커
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",  # 오류 발생 가능성 있음
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta": "META",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

st.title("📈 글로벌 시가총액 Top 10 기업의 주가 변화")
st.markdown("최근 1년간의 주가 추이를 Plotly 그래프로 시각화합니다.")

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# Plotly 그래프 객체 생성
fig = go.Figure()

for name, ticker in top10_tickers.items():
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        
        if data.empty or 'Adj Close' not in data.columns:
            st.warning(f"⚠️ {name} ({ticker}) 데이터 누락 또는 'Adj Close' 없음. 건너뜁니다.")
            continue

        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['Adj Close'],
            mode='lines',
            name=name
        ))
    except Exception as e:
        st.error(f"❌ {name} ({ticker}) 데이터 처리 중 오류 발생: {e}")
        continue

fig.update_layout(
    title="Top 10 글로벌 기업의 최근 1년간 주가 변화",
    xaxis_title="날짜",
    yaxis_title="조정 종가 (USD)",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)
