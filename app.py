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
```

#### 3단계: 필수 설정 파일 생성
* `requirements.txt` 파일을 생성하고 내용에 `streamlit` 한 단어만 적어서 저장합니다.

#### 4단계: Streamlit Cloud 배포
* [Streamlit Cloud](https://share.streamlit.io/)에 접속하여 **[Create app]**을 클릭합니다.
* 연결된 GitHub 저장소(`minus-account-calculator`)와 `app.py`를 선택하고 **[Deploy]**를 누릅니다.
* 배포가 완료되면 생성된 **웹 주소(URL)**를 복사합니다.

#### 5단계: 블로그 위젯 코드 적용
* 아래 HTML 코드를 복사하여 블로그 위젯 등록 창에 넣습니다.
* `https://본인의_마통_앱_주소/` 부분만 4단계에서 만든 URL로 바꿔주세요.

```html
<table width="170" bgcolor="#1e2229" cellpadding="15" cellspacing="0" style="border-collapse:collapse; border-radius:8px; text-align:center; font-family:sans-serif;">
  <tr>
    <td align="center" style="padding-top:20px; padding-bottom:5px;">
      <span style="color:#00c73c; font-weight:bold; font-size:14px;">마통 이자 계산기</span>
    </td>
  </tr>
  <tr>
    <td align="center" style="padding-top:0px; padding-bottom:15px;">
      <span style="color:#9aa0a6; font-size:11px; line-height:1.4;">사용한 만큼만 계산하는<br>일할 이자 분석기</span>
    </td>
  </tr>
  <tr>
    <td align="center" style="padding-top:0px; padding-bottom:20px;">
      <a href="https://본인의_마통_앱_주소/" target="_blank" style="text-decoration:none;">
        <div style="background-color:#00c73c; color:#ffffff; font-weight:bold; font-size:12px; padding:8px 0px; width:100%; border-radius:4px;">
          실시간 계산기 켜기
        </div>
      </a>
    </td>
  </tr>
</table>
