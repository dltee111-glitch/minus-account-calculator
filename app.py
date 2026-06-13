import streamlit as st
from datetime import date

st.set_page_config(page_title="마이너스 통장 이자 계산기", layout="centered")

st.title("📉 마이너스 통장 이자 계산기")
st.write("사용한 금액과 기간만큼만 계산하는 스마트한 일할 계산기입니다.")

# 입력 영역
col1, col2 = st.columns(2)
with col1:
    total_limit = st.number_input("마통 전체 한도 (원)", min_value=0, value=50000000, step=1000000)
with col2:
    amount = st.number_input("현재 사용 금액 (원)", min_value=0, value=10000000, step=1000000)

rate = st.number_input("연 금리 (%)", min_value=0.0, value=5.5, step=0.1)

c1, c2 = st.columns(2)
with c1:
    start_date = st.date_input("대출 시작일", date.today())
with c2:
    end_date = st.date_input("상환 예정일", date.today())

days = (end_date - start_date).days

if days > 0:
    # 1. 이자 계산
    interest = amount * (rate / 100) * (days / 365)
    
    # 2. 한도 사용률 계산
    usage_rate = (amount / total_limit) * 100 if total_limit > 0 else 0
    
    st.markdown("---")
    # 대시보드
    m1, m2 = st.columns(2)
    m1.metric("총 사용 일수", f"{days}일")
    m2.metric("예상 발생 이자", f"{int(interest):,} 원")
    
    # 게이지 차트 (한도 사용률)
    st.write(f"**한도 사용률: {usage_rate:.1f}%**")
    st.progress(min(usage_rate/100, 1.0))
    
    # 3. 상세 계산식 보기
    with st.expander("이자 계산식 자세히 보기"):
        st.write(f"""
        - 사용 금액: {amount:,}원
        - 적용 금리: {rate}%
        - 사용 기간: {days}일
        - **계산식**: {amount:,}원 * ({rate}/100) * ({days}/365)
        - **결과**: 약 {int(interest):,}원
        """)
else:
    st.warning("상환 예정일을 시작일 이후로 설정해주세요.")
