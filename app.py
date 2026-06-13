import streamlit as st
from datetime import date

st.set_page_config(page_title="마이너스 통장 이자 계산기", layout="centered")

st.title("📉 마이너스 통장 이자 계산기")
st.write("사용한 금액과 기간만큼만 계산하는 일할 계산기입니다.")

amount = st.number_input("사용 금액 (원)", min_value=0, value=10000000, step=1000000)
rate = st.number_input("연 금리 (%)", min_value=0.0, value=5.5, step=0.1)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("대출 시작일", date.today())
with col2:
    end_date = st.date_input("상환 예정일", date.today())

days = (end_date - start_date).days

if days > 0:
    # 이자 계산: 금액 * (금리/100) * (일수/365)
    interest = amount * (rate / 100) * (days / 365)
    
    st.markdown("---")
    st.metric(label="총 사용 일수", value=f"{days}일")
    st.metric(label="예상 발생 이자", value=f"{int(interest):,} 원")
else:
    st.warning("상환 예정일을 시작일 이후로 설정해주세요.")
