import streamlit as st
import plotly.graph_objects as go

# 메인 페이지
st.title("Intrusense")

# 페이지 선택을 탭 형식으로 구현
main_tabs = st.tabs(["메인 페이지", "데이터 분석 및 탐색", "모델", "보고서"])

# 메인 페이지
with main_tabs[0]:
    st.subheader("프로젝트의 목적 및 팀명 의미")
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
        st.subheader("목적 및 목표 ")
        st.info("네트워크 트래픽 기반 침입 탐지 모델을 만들자")
        st.info("정확도 99프로이상에 모델을 만들어보자")

        st.subheader("데이터")
        st.write("CIC-IDS 2017")
        st.subheader("데이터 설명 및 데이터 차용이유")
        st.write("CIC(Canadian Institute for Cybersecurity)은 사이버 공격 유형을 포함한 데이터셋을 제공하여 보안 연구와 머신러닝 모델 개발에 활용되기떄문에 데이터에 신뢰도가 높습니다.")
        st.write("현실적인 데이터 구조 CIC 데이터셋은 현실적인 네트워크 환경에서 생성된 데이터이기 때문에, 학습 모델이 실제 네트워크 환경에서도 성능을 낼 수 있도록 돕습니다.")
        st.write('단일 유형의 공격만 포함된 데이터셋과는 달리, CIC 데이터셋은 여러 공격 유형을 포함하고 있어 다양한 연구와 실험이 가능합니다.')
    # 데이터셋 요약 탭
    with tabs[1]:
        st.subheader("샘플 데이터")
        st.write("샘플 데이터를 표시하고 하이라이트 스타일을 추가합니다.")

        st.subheader("변수 설명")
        st.write("유효/누락 데이터 통계 요약을 여기에 표시합니다.")

    # 전체 워크플로 다이어그램 탭
    with tabs[2]:
        st.subheader("단계별 프로세스")
        st.plotly_chart(go.Figure(), use_container_width=True)

# 데이터 분석 및 탐색
with main_tabs[1]:

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
with main_tabs[2]:

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
with main_tabs[3]:
 
    # 서브탭 설정
    report_tabs = st.tabs(["논의점 및 미래 작업"])

    with report_tabs[0]:
        st.subheader("논의점")
        st.write("특정 소수 클래스(10개 이하의 칼럼)의 경우 표본 수가 너무 적어 패턴을 분석하기에는 데이터가 부족할 수 있다.")
        st.write("데이터의 편차가 큰 특징때문에 Ddos쪽으로 군집되어 web attack과 sql attack 같은 공격에취약하다")
        st.write('공격을 당했을때 ddos 공격 보다 web attack 이나 database 쪽이 피해를 입었을떄 더 큰 피해를 보기에 적은 표본이더라도 주의를 해야한다')
        st.write('xgboost도 좋은 성능을 보였지만 여기에 시계열 데이터를 추가하는것역시 고려 해봐야할거같다')
        st.subheader("미래 작업")
        st.write("향후 계획을 작성합니다.")
