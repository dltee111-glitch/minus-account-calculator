import streamlit as st
from datetime import date

st.set_page_config(page_title="마이너스 통장 이자 계산기", layout="centered")

# 헤더 섹션
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
    interest = amount * (rate / 100) * (days / 365)
    usage_rate = (amount / total_limit) * 100 if total_limit > 0 else 0
    
    st.markdown("---")
    m1, m2 = st.columns(2)
    m1.metric("총 사용 일수", f"{days}일")
    m2.metric("예상 발생 이자", f"{int(interest):,} 원")
    
    st.write(f"**한도 사용률: {usage_rate:.1f}%**")
    st.progress(min(usage_rate/100, 1.0))
    
    with st.expander("이자 계산식 자세히 보기"):
        st.write(f"계산식: {amount:,}원 * ({rate}/100) * ({days}/365) = 약 {int(interest):,}원")
else:
    st.warning("상환 예정일을 시작일 이후로 설정해주세요.")

# 화면을 채워주는 정보 섹션 추가
st.markdown("---")
st.subheader("💡 마이너스 통장 관리 꿀팁")
tab1, tab2, tab3 = st.tabs(["금리 인하 요구권", "한도 관리", "이자 절약법"])

with tab1:
    st.write("본인의 신용 상태가 개선되었다면(승진, 급여 인상 등) 은행에 **금리 인하 요구권**을 행사해 보세요.")
with tab2:
    st.write("마이너스 통장 한도를 다 채우지 말고 **평소 80% 이하로 유지**해야 신용 점수 관리에 유리합니다.")
with tab3:
    st.write("매달 이자가 나가는 날, 계좌 잔액이 부족하면 **연체 이자**가 발생하니 꼭 여유 잔액을 유지하세요.")

st.markdown("---")
st.info("이 계산기는 이해를 돕기 위한 모의 계산 결과이며, 실제 은행의 계산 방식(일할 계산 적용 시점 등)과 다를 수 있습니다.")
