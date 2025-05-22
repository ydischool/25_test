import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 시가총액 기준 Top 10 글로벌 기업 (2025년 기준 추정)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

st.title("📈 글로벌 시가총액 Top 10 기업의 주가 변화")
st.markdown("최근 1년간의 주가 추이를 Plotly 그래프로 시각화합니다.")

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 데이터 수집 및 시각화
fig = go.Figure()

for name, ticker in top10_tickers.items():
    data = yf.download(ticker, start=start_date, end=end_date)
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data["Adj Close"],
        mode="lines",
        name=name
    ))

fig.update_layout(
    title="Top 10 글로벌 기업의 최근 1년간 주가 변화",
    xaxis_title="날짜",
    yaxis_title="조정 종가 (USD)",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

