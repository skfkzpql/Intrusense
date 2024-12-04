import streamlit as st
import plotly.graph_objects as go

# 메인 페이지
st.title("Intrusense")

# 사이드바에 "Intrusense" 텍스트 넣기
st.sidebar.markdown("## **Intrusense**", unsafe_allow_html=True)

# 사이드바 탭 생성
page = st.sidebar.radio("", ["메인 페이지", "데이터 분석 및 탐색", "모델", "보고서"])

# 메인 페이지
if page == "메인 페이지":
    st.markdown("<h4>프로젝트의 목적 및 팀명 의미</h4>", unsafe_allow_html=True)
    # 팀명 소개
    st.markdown("""
    - **팀명**: Intrusense
    - 팀명 의미: Intrusense는 'Intrusion(침입)'과 'Sense(감각)'의 합성어로, 사이버 침입을 감지하겠다는 의미를 담은 팀명입니다.
    - **팀원 소개**:
        1. **이지아 (PM)**: 프로젝트 총괄 및 관리
        2. **손윤기 (ML 엔지니어)**: 데이터 전처리 및 시각화
        3. **조현 (ML 엔지니어)**: 모델 분석 및 프레임워크 개발
        4. **문경은 (ML 엔지니어)**: 데이터 전처리 지원 및 분석
    """)

    # 서브탭 설정
    tabs = st.tabs(["프로젝트 개요", "데이터셋 요약", "전체 워크플로 다이어그램"])

    # 프로젝트 개요 탭
    with tabs[0]:
        st.markdown("<h4>목적 및 목표</h4>", unsafe_allow_html=True)
        st.info("네트워크 트래픽 기반 침입 탐지 모델을 만들자")
        st.info("정확도 99프로이상에 모델을 만들어보자")

        st.markdown("<h4>데이터</h4>", unsafe_allow_html=True)
        st.markdown("""<span style="background-color: grey; text-decoration: underline; font-weight: bold;">CIC-IDS 2017</span>""", unsafe_allow_html=True)
        st.markdown("<h4>데이터 설명 및 차용 이유</h4>", unsafe_allow_html=True)
        st.write("CIC(Canadian Institute for Cybersecurity)은 사이버 공격 유형을 포함한 데이터셋을 제공하여 보안 연구와 머신러닝 모델 개발에 활용되기떄문에 데이터에 신뢰도가 높습니다.")
        st.write("현실적인 데이터 구조 CIC 데이터셋은 현실적인 네트워크 환경에서 생성된 데이터이기 때문에, 학습 모델이 실제 네트워크 환경에서도 성능을 낼 수 있도록 돕습니다.")
        st.write('단일 유형의 공격만 포함된 데이터셋과는 달리, CIC 데이터셋은 여러 공격 유형을 포함하고 있어 다양한 연구와 실험이 가능합니다.')
    # 데이터셋 요약 탭
    with tabs[1]:
        
        # 샘플 데이터
        st.markdown("<h4>샘플데이터</h4>", unsafe_allow_html=True)
        st.write("네트워크 트래픽 데이터셋의 샘플 데이터  \n주요 변수와 레이블(Label)을 포함하며, 침입 탐지 모델의 학습에 사용")

        # 샘플 데이터 정의
        import pandas as pd

        sample_data = pd.DataFrame({
            "Destination Port": [0, 0, 0, 0], # 목적지 포트
            "Flow Duration": [0, 0, 0, 0], # 플로우 지속 시간
            "Packet Length Mean": [0, 0, 0, 0], # 패킷 길이 평균
            "IAT Mean": [0, 0, 0, 0], # IAT 평균
            "Label": ["정상(Benign)", "DDoS", "Web Attack", "SQL Injection"] #레이블
        })

        # 하이라이트 스타일 정의
        def highlight_attack(row):
            return ['background-color: #002187' if row['Label'] != "정상(Benign)" else '' for _ in row]

        # 하이라이트 스타일이 적용된 데이터프레임 표시
        st.dataframe(sample_data.style.apply(highlight_attack, axis=1))

        st.write("공격 유형(Label)이 정상이 아닌 경우 하이라이트되며, 이 데이터는 `Destination Port`, `Flow Duration`, `Packet Length Mean`, `IAT Mean`와 같은 주요 변수로 구성됨.")


        st.markdown("<h4>변수 설명</h4>", unsafe_allow_html=True)
        st.write("네트워크 트래픽 데이터셋에서 각 변수의 유효 데이터 수와 누락 데이터를 요약한 통계")

        # 변수 유효/누락 데이터 통계 요약
        variable_stats = pd.DataFrame({
            "Variable": ["Destination Port", "Flow Duration", "Packet Length Mean", "IAT Mean", "Label"], # 변수
            "Valid Data Count": [0, 0, 0, 0], # 유효 데이터 수
            "Missing Data Count": [0, 0, 0, 0], # 누락 데이터 수 
            "Missing Data Percentage (%)": [0, 0, 0, 0] # 누락 데이터 비율(%)
        })

        st.table(variable_stats)

        st.write("중요한 변수는 침입 탐지 모델의 성능에 영향을 미침.  \n데이터셋에서 `Flow Duration`, `Packet Length Mean`, `IAT Mean`은 일부 누락된 데이터를 포함하며, 누락 비율은 각각 0.02%, 0.1%, 0.15%임. 이러한 변수는 모델의 학습에 유효한 정보를 제공")


    # 전체 워크플로 다이어그램 탭
    with tabs[2]:
        st.markdown("<h4>단계별 프로세스</h4>", unsafe_allow_html=True)
        st.plotly_chart(go.Figure(), use_container_width=True)

# 데이터 분석 및 탐색
elif page == "데이터 분석 및 탐색":
    
    st.markdown("<h4>데이터 분석 및 탐색</h4>", unsafe_allow_html=True)
    
    # 서브탭 설정
    analysis_tabs = st.tabs(["데이터 분포 및 변수별 요약 통계", "데이터 탐색", "데이터 전처리 및 준비"])

    # 데이터 분포 탭
    with analysis_tabs[0]:
        analysis_radio = st.radio("데이터 분석 옵션 선택", [
            "포트 및 트래픽량 관련", "패킷 길이 관련", "플래그 및 헤더 관련",
            "속도 및 비율 관련", "세그먼트 및 하위 플로우 관련",
            "시간 관련", "윈도우 크기 및 기타", "레이블"
        ])
        st.write(f"{analysis_radio}에 대한 히스토그램 및 박스플롯을 여기에 표시합니다.")

    # 데이터 탐색 탭
    with analysis_tabs[1]:
        exploration_radio = st.radio("탐색 옵션 선택", ["결측치, 이상치", "상관관계"])
        if exploration_radio == "결측치, 이상치":
            st.subheader("결측치 탐지")
            st.write("결측치 히트맵을 여기에 표시합니다.")

            st.subheader("이상치 탐지")
            st.write("Z-Score 기반 시각화를 표시합니다.")

        elif exploration_radio == "상관관계":
            st.subheader("상관 행렬")
            st.write("상관 행렬 및 클러스터 맵을 표시합니다.")

    # 데이터 전처리 탭
    with analysis_tabs[2]:
        preprocessing_radio = st.radio("전처리 옵션 선택", ["제거된 칼럼/데이터", "스케일링 및 차원 축소", "샘플링 (UDBB)"])
        if preprocessing_radio == "제거된 칼럼/데이터":
            st.subheader("제거된 데이터")
            st.write("파이 차트를 표시합니다.")

        elif preprocessing_radio == "스케일링 및 차원 축소":
            st.subheader("스케일링 전후 비교")
            st.write("스케일링 전후의 분포를 비교합니다.")

        elif preprocessing_radio == "샘플링 (UDBB)":
            st.subheader("샘플링 비율")
            st.write("샘플 수 비율 바 차트를 표시합니다.")

# 모델
elif page == "모델":
    
    st.markdown("<h4>모델</h4>", unsafe_allow_html=True)

    # 서브탭 설정
    model_tabs = st.tabs(["모델 성능 비교", "최종 모델"])

    # 모델 성능 비교 탭
    with model_tabs[0]:
        model_radio = st.radio("모델 선택", ["RF", "S + RF", "AE + RF", "AE + PCA + RF", "전체 모델 성능 비교"])
        st.subheader(f"{model_radio} 성능")
        st.write("성능 테이블 및 그래프를 표시합니다.")

    # 최종 모델 탭
    with model_tabs[1]:
        st.subheader("최종 모델 성능")
        st.write("성능 지표 및 ROC 곡선을 표시합니다.")

# 보고서
else:
    
    st.markdown("<h4>보고서</h4>", unsafe_allow_html=True)
    
    # 서브탭 설정
    report_tabs = st.tabs(["논의점 및 미래 작업"])

    with report_tabs[0]:
        st.markdown("<h4>논의점</h4>", unsafe_allow_html=True)
        st.write("특정 소수 클래스(10개 이하의 칼럼)의 경우 표본 수가 너무 적어 패턴을 분석하기에는 데이터가 부족할 수 있다.")
        st.write("데이터의 편차가 큰 특징때문에 Ddos쪽으로 군집되어 web attack과 sql attack 같은 공격에취약하다")
        st.write('공격을 당했을때 ddos 공격 보다 web attack 이나 database 쪽이 피해를 입었을떄 더 큰 피해를 보기에 적은 표본이더라도 주의를 해야한다')
        st.write('xgboost도 좋은 성능을 보였지만 여기에 시계열 데이터를 추가하는것역시 고려 해봐야할거같다')
        st.markdown("<h4>미래 작업</h4>", unsafe_allow_html=True)
        st.write("향후 계획을 작성합니다.")
