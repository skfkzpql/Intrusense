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
        st.markdown("<h4>프로젝트 개요</h4>", unsafe_allow_html=True)
        st.markdown('사이버 보안 위협이 점점 더 복잡하고 정교해짐에 따라, 효율적이고 신뢰성 있는 침입 탐지 시스템의 필요성이 강조되고 있습니다. 이에 우리 팀은 다양한 사이버 공격 유형을 포함한 현실적인 네트워크 데이터셋을 활용하여, 실제 환경에서도 높은 정확도를 보이는 머신러닝 딥러닝 기반의 침입 탐지 모델을 구축하고자 합니다.')
        st.markdown("<h5>- 전통적 탐지기법말고 ai를 왜 활용해야할까?</h5>", unsafe_allow_html=True)
        st.info("💡실제 ai 기반 보안 산업에 **정확도**와 **유연성**을 바탕으로하는 **AI 기반 솔루션**의 채택률 증가하는 추세입니다.")
    # 이미지 삽입
        st.image("개요.png", caption="AI 보안 시장 출처: 정보통신신문 (https://www.koit.co.kr/news/articleView.html?idxno=126833)")
        st.markdown("<h4>목적 및 목표</h4>", unsafe_allow_html=True)
        st.info("✔️ 네트워크 트래픽 기반 침입 탐지 모델을 만들기")
        st.info("✔️ 정확도 99% 이상에 모델을 만들기")

    # 데이터셋 요약 탭
    with tabs[1]:
        
        st.markdown("<h4>데이터셋</h4>", unsafe_allow_html=True)
        st.markdown("""<span style="background-color: grey; text-decoration: underline; font-weight: bold;">CIC-IDS 2017</span> : Canadian Institute for Cybersecurity에서 제공하는 데이터셋
                      \n- **데이터 저장 방식**: MySQL 데이터베이스
          \n- **데이터 규모**: 78개의 피처, 1개의 타겟 레이블, 총 225,745개의 행(Row)""", unsafe_allow_html=True)
       
        # st.markdown("<h4>데이터 설명 및 차용 이유</h4>", unsafe_allow_html=True)
        # st.write("CIC(Canadian Institute for Cybersecurity)은 사이버 공격 유형을 포함한 데이터셋을 제공하여 보안 연구와 머신러닝 모델 개발에 활용되기떄문에 데이터에 신뢰도가 높습니다.")
        # st.write("현실적인 데이터 구조 CIC 데이터셋은 현실적인 네트워크 환경에서 생성된 데이터이기 때문에, 학습 모델이 실제 네트워크 환경에서도 성능을 낼 수 있도록 돕습니다.")
        # st.write('단일 유형의 공격만 포함된 데이터셋과는 달리, CIC 데이터셋은 여러 공격 유형을 포함하고 있어 다양한 연구와 실험이 가능합니다.')
        
    #     st.markdown("""
    #     #### **피처 종류**
    #     - **포트 및 트래픽량**
    #     - **패킷 길이**
    #     - **플래그 및 헤더**
    #     - **속도 및 비율**
    #     - **세그먼트 및 하위 플로우**
    # """)
        
        import pandas as pd

        # 대표 공격 데이터
        attacks_data = {
            "공격 유형": [
                "DDoS", 
                "PortScan", 
                "Bot", 
                "Web Attack SQL Injection", 
                "Heartbleed"
            ],
            "설명": [
                "분산 서비스 거부 공격.", 
                "네트워크 포트를 스캔하여 취약점을 탐색하는 공격.", 
                "악성 봇에 감염된 장치의 네트워크 활동.", 
                "SQL 문법을 악용한 데이터베이스 공격.", 
                "OpenSSL 취약점을 악용해 민감 정보를 유출하는 공격."
            ]
        }

        # 주요 칼럼 데이터
        columns_data = {
            "칼럼명": [
                "Flow Duration", 
                "Total Fwd Packets, Total Backward Packets", 
                "Flow Bytes/s, Flow Packets/s", 
                "Flow IAT Mean, Flow IAT Std", 
                "Fwd Packet Length Max, Fwd Packet Length Mean", 
                "Bwd Packet Length Max, Bwd Packet Length Mean", 
                "PSH Flags Count, URG Flags Count", 
                "SYN Flag Count, FIN Flag Count, RST Flag Count", 
                "Label"
            ],
            "설명": [
                "흐름의 지속 시간. 공격과 정상 트래픽의 차이를 분석할 수 있는 중요한 지표.",
                "전송 및 수신된 총 패킷 수. 예) DDoS 공격 시 패킷 수 급증.",
                "초당 바이트 및 패킷 수. 이상 트래픽에서 값이 급격히 변할 가능성이 큼.",
                "트래픽의 시간 간격. 공격 시 간격의 일정치 않음이 나타날 수 있음.",
                "순방향 패킷의 최대 및 평균 길이.",
                "역방향 패킷의 최대 및 평균 길이.",
                "푸시(PSH)와 긴급(URG) 플래그가 설정된 패킷 수.",
                "연결 요청 및 종료 관련 플래그. 공격 탐지에 활용 가능.",
                "각 트래픽의 레이블(정상/공격 유형)."
            ]
        }

        # 타겟 레이블 데이터
        target_labels_data = {
            "타겟 레이블": [
                "BENIGN", 
                "DDoS", 
                "PortScan", 
                "Bot", 
                "Infiltration", 
                "Web Attack Brute Force", 
                "Web Attack XSS", 
                "Web Attack SQL Injection", 
                "FTP-Patator", 
                "SSH-Patator", 
                "DoS slowloris", 
                "DoS Slowhttptest", 
                "DoS Hulk", 
                "DoS GoldenEye", 
                "Heartbleed"
            ],
            "설명": [
                "정상 트래픽.", 
                "분산 서비스 거부(Distributed Denial of Service) 공격.", 
                "네트워크 포트 스캔 공격.", 
                "악성 봇 활동.", 
                "네트워크 침투 및 권한 탈취.", 
                "무차별 대입 공격.", 
                "크로스 사이트 스크립팅.", 
                "SQL 문법을 이용한 공격.", 
                "FTP 서버 대상 무차별 대입 공격.", 
                "SSH 서버 대상 무차별 대입 공격.", 
                "HTTP 연결 점유로 서비스 장애 유발.", 
                "HTTP 헤더 기반 DoS 공격.", 
                "서버 부하 초래 DoS 공격.", 
                "HTTP GET 요청 남발로 서버 마비.", 
                "OpenSSL 취약점 악용 공격."
            ]
        }

        # DataFrames 생성
        attacks_df = pd.DataFrame(attacks_data)
        columns_df = pd.DataFrame(columns_data)
        target_labels_df = pd.DataFrame(target_labels_data)

        # 출력
        st.markdown("<h5>대표 공격</h5>", unsafe_allow_html=True)
        st.dataframe(attacks_df)
        st.markdown("<h5>주요 컬럼</h5>", unsafe_allow_html=True)
        st.dataframe(columns_df)
        st.caption("""### 💡알고 가면 좋은 정보 3가지 ###
        1. 패킷(Packet): 네트워크를 통해 전송되는 데이터의 단위입니다. 네트워크 패킷은 보통 헤더(송수신자 정보, 프로토콜 등의 메타 데이터 포함)와 페이로드(실제 전송할 데이터)를 포함합니다.
    2. IAT (Inter-Arrival Time): 연속적인 패킷들 사이의 도착 시간 간격입니다. IAT는 네트워크 트래픽의 패턴을 분석할 때 사용되며, 예를 들어 DDoS 공격과 같은 비정상적인 트래픽 플로우를 감지하는데 도움을 줍니다.
    3. 길이(Length): 패킷의 크기를 의미하며, 보통 바이트 단위로 측정됩니다. 패킷의 길이는 네트워크의 부하, 전송 속도, 그리고 사용된 프로토콜에 대한 정보를 제공할 수 있습니다.""")
        st.markdown("<h5>타겟 레이블</h5>", unsafe_allow_html=True)
        st.dataframe(target_labels_df)

        
        # # 샘플 데이터
        # st.markdown("<h4>샘플데이터</h4>", unsafe_allow_html=True)
        # st.write("네트워크 트래픽 데이터셋의 샘플 데이터  \n주요 변수와 레이블(Label)을 포함하며, 침입 탐지 모델의 학습에 사용")

        # # 샘플 데이터 정의
        # import pandas as pd

        # sample_data = pd.DataFrame({
        #     "Destination Port": [0, 0, 0, 0], # 목적지 포트
        #     "Flow Duration": [0, 0, 0, 0], # 플로우 지속 시간
        #     "Packet Length Mean": [0, 0, 0, 0], # 패킷 길이 평균
        #     "IAT Mean": [0, 0, 0, 0], # IAT 평균
        #     "Label": ["정상(Benign)", "DDoS", "Web Attack", "SQL Injection"] #레이블
        # })

        # # 하이라이트 스타일 정의
        # def highlight_attack(row):
        #     return ['background-color: #002187' if row['Label'] != "정상(Benign)" else '' for _ in row]

        # # 하이라이트 스타일이 적용된 데이터프레임 표시
        # st.dataframe(sample_data.style.apply(highlight_attack, axis=1))

        # st.write("공격 유형(Label)이 정상이 아닌 경우 하이라이트되며, 이 데이터는 `Destination Port`, `Flow Duration`, `Packet Length Mean`, `IAT Mean`와 같은 주요 변수로 구성됨.")


        # st.markdown("<h4>변수 설명</h4>", unsafe_allow_html=True)
        # st.write("네트워크 트래픽 데이터셋에서 각 변수의 유효 데이터 수와 누락 데이터를 요약한 통계")

        # # 변수 유효/누락 데이터 통계 요약
        # variable_stats = pd.DataFrame({
        #     "Variable": ["Destination Port", "Flow Duration", "Packet Length Mean", "IAT Mean", "Label"], # 변수
        #     "Valid Data Count": [0, 0, 0, 0, 0], # 유효 데이터 수
        #     "Missing Data Count": [0, 0, 0, 0, 0], # 누락 데이터 수 
        #     "Missing Data Percentage (%)": [0, 0, 0, 0, 0] # 누락 데이터 비율(%)
        # })

        # st.table(variable_stats)

        # st.write("중요한 변수는 침입 탐지 모델의 성능에 영향을 미침.  \n데이터셋에서 `Flow Duration`, `Packet Length Mean`, `IAT Mean`은 일부 누락된 데이터를 포함하며, 누락 비율은 각각 0.02%, 0.1%, 0.15%임. 이러한 변수는 모델의 학습에 유효한 정보를 제공")


    # 전체 워크플로 다이어그램 탭
    with tabs[2]:
        st.markdown("<h4>단계별 프로세스</h4>", unsafe_allow_html=True)
        # 노드 이름 정의
        node_labels = ['수집', '점검 및 탐색', '전처리 및 정제', '모델링 및 훈련', '평가', '배포', '테스트 데이터']

        # 흐름 (간단한 방향성 연결 설정)
        links = [
            {'source': 0, 'target': 1, 'value': 1},  # 수집 -> 점검 및 탐색
            {'source': 1, 'target': 2, 'value': 1},  # 점검 및 탐색 -> 전처리 및 정제
            {'source': 2, 'target': 3, 'value': 1},  # 전처리 및 정제 -> 모델링 및 훈련
            {'source': 3, 'target': 4, 'value': 1},  # 모델링 및 훈련 -> 평가
            {'source': 4, 'target': 5, 'value': 1},  # 평가 -> 배포
            {'source': 1, 'target': 6, 'value': 1},  # 점검 및 탐색 -> 테스트 데이터
            {'source': 6, 'target': 4, 'value': 1},  # 테스트 데이터 -> 평가
        ]

        # 노드와 링크 데이터 정의
        nodes = {
            'label': node_labels,
            'color': ['#68b3a3', '#ff8000', '#ffcc66', '#66b3ff', '#1f77b4', '#003366', '#00b3b3'],
        }

        # 링크에 대한 출발지, 도착지, 값 설정
        link_sources = [link['source'] for link in links]
        link_targets = [link['target'] for link in links]
        link_values = [link['value'] for link in links]

        # Sankey Diagram 그리기
        fig = go.Figure(go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                color=nodes['color'],
                label=nodes['label']
            ),
            link=dict(
                source=link_sources,
                target=link_targets,
                value=link_values
            )
        ))

        # 레이아웃 설정
        fig.update_layout(

            font_size=12,
            height=600,
            width=800
        )

        # Plotly 차트 표시
        st.plotly_chart(fig)


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

    # 첫 번째 서브탭 내용
    with report_tabs[0]:
        st.subheader("추후 논의점")
        st.markdown("""
        - **소수 클래스의 표본 부족**: 특정 소수 클래스(10개 이하의 데이터)의 경우, 표본 수가 너무 적어 패턴 분석에 어려움이 있었습니다.
        - **데이터 편차로 인한 모델 편향**: 데이터의 편차로 인해 DDoS 쪽에 모델이 편향되어 Web Attack 및 SQL Attack과 같은 공격에 상대적으로 약한 성능을 보였습니다.
        - **공격 유형별 피해 정도**: DDoS 공격보다 Web Attack이나 Database 관련 공격이 더 큰 피해를 유발할 수 있습니다. 따라서, 적은 표본이더라도 이러한 공격 유형에 대한 분석을 강화해야 합니다.
        - **시계열 데이터 추가**: 시계열 데이터를 추가하여, 모델의 성능 및 이상 탐지 능력을 개선할 필요가 있습니다.
        """)

        st.subheader("회고 및 개선점")
        st.markdown("""
        - **아쉬웠던 점**: 2017년과 2018년의 데이터셋이 제공되었지만, 칼럼 구조의 차이로 인해 2018년 데이터를 검증용 데이터셋으로 활용할 수 없었습니다.
        - **배운 점**: 팀원들과 함께 작업하면서 많은 것을 배웠습니다. 예를 들어, 동일한 데이터셋을 사용했음에도 불구하고 수치 차이가 발생하는 문제를 발견하고 해결하면서 데이터의 일관성을 유지하는 방법을 학습했습니다.
        - **협업의 중요성**: Git을 활용한 협업을 통해 팀원 간 소통과 배려의 중요성을 깨달았습니다. 서로의 작업 내용을 공유하며 프로젝트를 성공적으로 진행할 수 있었습니다.""")
