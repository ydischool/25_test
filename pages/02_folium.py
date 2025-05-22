import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
import json
import os

SAVE_FILE = "saved_locations.json"

def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

st.set_page_config(page_title="지도 메모 앱", layout="wide")
st.title("📍 한국 명소 위치 찾기 및 메모 앱")

locations = load_data()

query = st.text_input("🔎 새로운 장소 검색 (예: 광화문, 남산타워 등)", "")

geolocator = Nominatim(user_agent="my_unique_app_2025")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=3)

def do_geocode(address):
    try:
        return geolocator.geocode(address, exactly_one=False, addressdetails=True, limit=5, timeout=10)
    except GeocoderTimedOut:
        st.error("서버 응답이 지연되고 있습니다. 잠시 후 다시 시도해주세요.")
        return None

if query:
    with st.spinner("장소 검색 중..."):
        results = do_geocode(query + ", South Korea")

    if not results:
        st.error("장소를 찾을 수 없습니다.")
    else:
        option = st.selectbox("📍 정확한 장소를 선택하세요", [res.address for res in results])
        selected = next((res for res in results if res.address == option), None)

        if selected:
            memo = st.text_area("✏️ 이 장소에 대한 메모를 입력하세요", "")
            if st.button("저장하기"):
                new_entry = {
                    "name": option,
                    "lat": selected.latitude,
                    "lon": selected.longitude,
                    "memo": memo
                }
                locations.append(new_entry)
                save_data(locations)
                st.success("✅ 저장되었습니다! 아래 지도에서 확인하세요.")

m = folium.Map(location=[36.5, 127.8], zoom_start=7)

for loc in locations:
    popup_text = f"<b>{loc['name']}</b><br>📝 {loc['memo']}" if loc["memo"] else loc["name"]
    folium.Marker(
        [loc["lat"], loc["lon"]],
        popup=popup_text,
        tooltip=loc["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

st.markdown("🗺️ 저장된 위치들을 지도에서 확인하세요:")
st_data = st_folium(m, width=700, height=500)
