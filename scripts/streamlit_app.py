import os
import re
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from matplotlib import font_manager, rc
import requests

def get_file_path(local_path: str, cloud_path: str) -> str:
    #이미지 경로를 반환하는 함수.
    if os.path.exists(local_path):
        return local_path
    elif os.path.exists(cloud_path):
        return cloud_path
    else:
        raise FileNotFoundError(f"Neither '{local_path}' nor '{cloud_path}' exists.")

# 이미지 경로 배열
image_files = [
    ("images/개요.png", "scripts/images/개요.png"),
    ("images/워크플로우.png", "scripts/images/워크플로우.png"),
    ("../results/figures", "results/figures"),
    ("../results/figures/negative_data_ratio.png", "results/figures/negative_data_ratio.png"),
    ("../results/figures/negative_columns_top2.png", "results/figures/negative_columns_top2.png"),
    ("../results/figures/negative_columns_rest.png", "results/figures/negative_columns_rest.png"),
    ("../results/figures/corr.png", "results/figures/corr.png"),
    ("../results/figures/corr_network.png", "results/figures/corr_network.png"),
    ("../results/figures/col_drop.png", "results/figures/col_drop.png"),
    ("../results/reports/models_scores.csv", "results/reports/models_scores.csv"),
    ("../results/reports/xgb_scaler_None_pca_None_report.txt", "results/reports/xgb_scaler_None_pca_None_report.txt")
]

# 한글 폰트 경로 설정
# font_path = os.path.join(os.getcwd(), get_file_path("fonts", "scripts/fonts"), "BATANG.TTC")
# font_name = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font_name)

def download_font(url, save_path):
    if not os.path.exists(save_path):
        print(f"Downloading font from {url}...")
        response = requests.get(url)
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Font downloaded to {save_path}")
        
# 폰트 다운로드
font_url = "https://github.com/JiAhLee903/Intrusense/tree/main/scripts/fonts/BATANG.TTC"  # 폰트 파일 URL
font_path = os.path.join(get_file_path("fonts", "scripts/fonts"), "BATANG.TTC")
download_font(font_url, font_path)
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 메인 페이지
st.title("Intrusense")

pages = st.tabs(["🏠메인 페이지", "🔍데이터 분석 및 탐색", "📊모델", "📄보고서"])

# 메인 페이지
with pages[0]:
    # 팀명 의미
    st.markdown("<h4>팀명 의미</h4>", unsafe_allow_html=True)
    st.markdown("""Intrusense**는 Intrusion(침입)+Sense(감각)의 합성어로, 사이버 침입을 감지**하겠다는 의미""")

    # 팀원 소개
    st.markdown("<h4>팀원 소개</h4>", unsafe_allow_html=True)
    team_members = [
        {"name": "이지아", "role": "PM", "description": "프로젝트 총괄 및 관리"},
        {"name": "손윤기", "role": "ML 엔지니어", "description": "데이터 전처리 및 시각화"},
        {"name": "조현", "role": "ML 엔지니어", "description": "모델 분석 및 프레임워크 개발"},
        {"name": "문경은", "role": "ML 엔지니어", "description": "데이터 전처리 지원 및 분석"}
    ]

    # 팀원 정보를 열로 정리
    cols = st.columns(len(team_members))  
    for col, member in zip(cols, team_members):
        with col:
            st.markdown(f"**{member['name']}**")
            st.markdown(f"*{member['role']}*")
            st.write(member['description'])

    # 서브탭 설정
    tabs = st.tabs(["프로젝트 개요", "데이터셋 요약", "전체 워크플로 다이어그램"])

    # 프로젝트 개요 탭
    with tabs[0]:
        st.markdown("<h4>프로젝트 개요</h4>", unsafe_allow_html=True)
        st.markdown('사이버 보안 위협이 점점 더 복잡하고 정교해짐에 따라, 효율적이고 신뢰성 있는 침입 탐지 시스템의 필요성이 강조되고 있습니다. 이에 우리 팀은 다양한 사이버 공격 유형을 포함한 현실적인 네트워크 데이터셋을 활용하여, 실제 환경에서도 높은 정확도를 보이는 머신러닝 딥러닝 기반의 침입 탐지 모델을 구축하고자 합니다.')
        st.markdown("<h5>- 전통적 탐지기법말고 ai를 왜 활용해야할까?</h5>", unsafe_allow_html=True)
        st.info("💡실제 ai 기반 보안 산업에 **정확도**와 **유연성**을 바탕으로하는 **AI 기반 솔루션**의 채택률 증가하는 추세입니다.")
        # 이미지 삽입
        local, cloud = image_files[0]
        st.image(get_file_path(local, cloud), caption="AI 보안 시장 출처: 정보통신신문 (https://www.koit.co.kr/news/articleView.html?idxno=126833)", use_container_width=True)
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

    # 전체 워크플로 다이어그램 탭
    with tabs[2]:
        st.markdown("<h4>단계별 프로세스</h4>", unsafe_allow_html=True)
        local, cloud = image_files[1]
        st.image(get_file_path(local, cloud), use_container_width=True)


# 데이터 분석 및 탐색
with pages[1]:
    
    st.markdown("<h4>데이터 분석 및 탐색</h4>", unsafe_allow_html=True)
    
    # 서브탭 설정
    analysis_tabs = st.tabs(["데이터 분포 및 변수별 요약 통계", "데이터 탐색", "데이터 전처리 및 준비"])

    # 데이터 분포 탭
    with analysis_tabs[0]:
        analysis_radio = st.radio("데이터 분석 옵션 선택", [
            "포트 및 트래픽량 관련", "패킷 길이 관련", "플래그 및 헤더 관련",
            "속도 및 비율 관련", "세그먼트 및 하위 플로우 관련",
            "시간 관련", "윈도우 크기 및 기타", "활동 및 휴면 시간 관련", "레이블"
        ])

        columns_dict = {
            "포트 및 트래픽량 관련": [
                "Flow Duration",  # 주요 칼럼
                "Total Fwd Packets",  # 주요 칼럼
                "Total Backward Packets",  # 주요 칼럼
                "Flow Bytes/s",  # 주요 칼럼
                "Flow Packets/s",  # 주요 칼럼
                "Destination Port"],
            "패킷 길이 관련": [
                "Fwd Packet Length Max",  # 주요 칼럼
                "Fwd Packet Length Mean",  # 주요 칼럼
                "Bwd Packet Length Max",  # 주요 칼럼
                "Bwd Packet Length Mean",  # 주요 칼럼
                "Total Length of Fwd Packets",
                "Total Length of Bwd Packets",
                "Fwd Packet Length Min",
                "Fwd Packet Length Std",
                "Bwd Packet Length Min",
                "Bwd Packet Length Std",
                "Min Packet Length",
                "Max Packet Length",
                "Packet Length Mean",
                "Packet Length Std",
                "Packet Length Variance"],
            "플래그 및 헤더 관련": [
                "PSH Flag Count",  # 주요 칼럼
                "URG Flag Count",  # 주요 칼럼
                "SYN Flag Count",  # 주요 칼럼
                "FIN Flag Count",  # 주요 칼럼
                "RST Flag Count",  # 주요 칼럼
                "Fwd PSH Flags",
                "Bwd PSH Flags",
                "Fwd URG Flags",
                "Bwd URG Flags",
                "Fwd Header Length",
                "Bwd Header Length",
                "Fwd Header Length.1",
                "ACK Flag Count",
                "CWE Flag Count",
                "ECE Flag Count"],
            "속도 및 비율 관련": [
                "Flow Bytes/s",  
                "Flow Packets/s",  
                "Down/Up Ratio",
                "Average Packet Size",
                "Fwd Avg Bytes/Bulk",
                "Fwd Avg Packets/Bulk",
                "Fwd Avg Bulk Rate",
                "Bwd Avg Bytes/Bulk",
                "Bwd Avg Packets/Bulk",
                "Bwd Avg Bulk Rate"],
            "세그먼트 및 하위 플로우 관련": [
                "Avg Fwd Segment Size",
                "Avg Bwd Segment Size",
                "Subflow Fwd Packets",
                "Subflow Fwd Bytes",
                "Subflow Bwd Packets",
                "Subflow Bwd Bytes"],
            "시간 관련": [
                "Flow IAT Mean",  # 주요 칼럼
                "Flow IAT Std",  # 주요 칼럼
                "Flow IAT Max",
                "Flow IAT Min",
                "Fwd IAT Total",
                "Fwd IAT Mean",
                "Fwd IAT Std",
                "Fwd IAT Max",
                "Fwd IAT Min",
                "Bwd IAT Total",
                "Bwd IAT Mean",
                "Bwd IAT Std",
                "Bwd IAT Max",
                "Bwd IAT Min"],
            "윈도우 크기 및 기타": [
                "Init_Win_bytes_forward",
                "Init_Win_bytes_backward",
                "act_data_pkt_fwd",
                "min_seg_size_forward"],
            "활동 및 휴면 시간 관련": [
                "Active Mean",
                "Active Std",
                "Active Max",
                "Active Min",
                "Idle Mean",
                "Idle Std",
                "Idle Max",
                "Idle Min"],
            "레이블": [
                "Label"]  # 주요 칼럼
            }
        
        # 선택된 카테고리에 따른 칼럼 리스트
        if analysis_radio in columns_dict:
            selected_columns = columns_dict[analysis_radio]
            
            # 선택된 칼럼에 대해 히스토그램과 박스플롯을 가로로 배치
            for column in selected_columns:
                st.subheader(f"{column} 분석")

                # 가로로 두 개의 영역 배치
                col1, col2 = st.columns(2)
                
                safe_column_name = re.sub(r'[<>:"/\\|?*]', '_', column) 

                if column == 'Label':
                    # 이미지 파일 경로
                    local, cloud = image_files[2]
                    col1_image = get_file_path(os.path.join(local, f"{analysis_radio}_{safe_column_name}_pie_chart.png"),
                                                os.path.join(cloud, f"{analysis_radio}_{safe_column_name}_pie_chart.png"))
                    col2_image = get_file_path(os.path.join(local, f"{analysis_radio}_{safe_column_name}_bar_chart.png"),
                                                os.path.join(cloud, f"{analysis_radio}_{safe_column_name}_bar_chart.png"))
                else:
                    # 이미지 파일 경로
                    local, cloud = image_files[2]
                    col1_image = get_file_path(os.path.join(local, f"{analysis_radio}_{safe_column_name}_histogram.png"),
                                                os.path.join(cloud, f"{analysis_radio}_{safe_column_name}_histogram.png"))
                    col2_image = get_file_path(os.path.join(local, f"{analysis_radio}_{safe_column_name}_boxplot.png"),
                                                os.path.join(cloud, f"{analysis_radio}_{safe_column_name}_boxplot.png"))
                
                if os.path.exists(col1_image):
                    with col1:
                        st.image(col1_image)
                else:
                    with col1:
                        st.write(f"'{col1_image}' 파일이 존재하지 않습니다.")
                
                
                if os.path.exists(col2_image):
                    with col2:
                        st.image(col2_image)
                else:
                    with col2:
                        st.write(f"'{col2_image}' 파일이 존재하지 않습니다.")


    # 데이터 탐색 탭
    with analysis_tabs[1]:
        exploration_radio = st.radio("탐색 옵션 선택", ["음수 값", "상관관계"])

        if exploration_radio == "음수 값":
            st.subheader("음수 데이터 비율")
            local, cloud = image_files[3]
            st.image(get_file_path(local, cloud), use_container_width=True)
            # st.image("../results/figures/negative_data_ratio.png")

            st.subheader("음수 값 상위 2개 칼럼")
            local, cloud = image_files[4]
            st.image(get_file_path(local, cloud), use_container_width=True)
            # st.image("../results/figures/negative_columns_top2.png")

            st.subheader("음수 값 칼럼2")
            local, cloud = image_files[5]
            st.image(get_file_path(local, cloud), use_container_width=True)
            # st.image("../results/figures/negative_columns_rest.png")

        elif exploration_radio == "상관관계":
            st.subheader("상관계수 절대값 기준 상위 30개")
            local, cloud = image_files[6]
            st.image(get_file_path(local, cloud), use_container_width=True)
            # st.image("../results/figures/corr.png")

            st.subheader("상관계수 0.9이상 네트워크 그래프")
            local, cloud = image_files[7]
            st.image(get_file_path(local, cloud), use_container_width=True)
            # st.image("../results/figures/corr_network.png")

    # 데이터 전처리 탭
    with analysis_tabs[2]:
        preprocessing_radio = st.radio("전처리 옵션 선택", ["제거된 칼럼", "제거된 데이터"])
        if preprocessing_radio == "제거된 칼럼":
            st.subheader("제거된 칼럼")
            local, cloud = image_files[8]
            st.image(get_file_path(local, cloud), use_container_width=True)
            # st.image("../results/figures/col_drop.png")
            st.markdown("#### 단 하나의 값으로만 이루어진 칼럼 제거")
            st.code(body="""
                    # 단 하나의 값으로만 이루어진 칼럼 찾기
                    single_value_columns = [col for col in df.columns if df[col].nunique() == 1]
                    df_cleaned = df.drop(columns=single_value_columns)
                    """, language="python")
            
            single_value_colums = ['Bwd PSH Flags', 'Bwd URG Flags', 'Fwd Avg Bytes/Bulk', 'Fwd Avg Packets/Bulk', 'Fwd Avg Bulk Rate', 'Bwd Avg Bytes/Bulk', 'Bwd Avg Packets/Bulk', 'Bwd Avg Bulk Rate']
            df_single_value_colums = pd.DataFrame(single_value_colums, columns=["제거된 칼럼"])
            st.write(df_single_value_colums)

            st.markdown("#### 동일한 칼럼 제거")
            st.code(body="""
                    # 각 칼럼의 값을 tuple로 변환하여 비교
                    grouped_columns = {}

                    for col in df_cleaned.columns:
                        col_values = tuple(df_cleaned[col].values)  # 각 칼럼의 값을 tuple로 변환
                        if col_values in grouped_columns:  # 동일한 값이 이미 존재하는지 확인
                            grouped_columns[col_values].append(col)  # 그룹에 추가
                        else:
                            grouped_columns[col_values] = [col]  # 새로운 그룹 생성

                    # 그룹화된 칼럼 중 2개 이상 포함된 것만 추출
                    grouped_result = [group for group in grouped_columns.values() if len(group) > 1]
                    """, language="python")
            
            grouped_columns = [
                ['Total Fwd Packets', 'Subflow Fwd Packets'],
                ['Total Backward Packets', 'Subflow Bwd Packets'],
                ['Fwd Packet Length Mean', 'Avg Fwd Segment Size'],
                ['Bwd Packet Length Mean', 'Avg Bwd Segment Size'],
                ['Fwd PSH Flags', 'SYN Flag Count'],
                ['Fwd URG Flags', 'CWE Flag Count'],
                ['Fwd Header Length', 'Fwd Header Length.1']
            ]

            # DataFrame 생성
            df_grouped_columns = pd.DataFrame(grouped_columns, columns=["칼럼1", "제거된 칼럼1과 동일한 칼럼"])
            st.write(df_grouped_columns)

        elif preprocessing_radio == "제거된 데이터":
            st.subheader("제거된 데이터")
            st.markdown("#### 음수가 포함된 칼럼의 음수 데이터의 Label 칼럼 unique 값이 0 하나인 데이터 삭제")
            st.code("""
                    # 음수가 포함된 칼럼들 추출
                    negative_columns = df.columns[df.min() < 0]

                    # 'Label' 칼럼의 unique 값이 0 하나인 음수가 포함된 칼럼 추출
                    negative_columns_with_only_zero_label = [
                    col for col in negative_columns
                    if df[df[col] < 0]['Label'].nunique() == 1 
                    and df[df[col] < 0]['Label'].unique()[0] == 0]
                    """, language="python")
            
            negative_columns_with_only_zero_label = ['Flow Duration', 'Flow Bytes/s', 'Flow Packets/s', 'Flow IAT Mean', 'Flow IAT Max', 'Fwd Header Length', 'Bwd Header Length', 'Fwd Header Length.1', 'min_seg_size_forward']
            df_negative_columns_with_only_zero_label = pd.DataFrame(negative_columns_with_only_zero_label, columns=["해당 칼럼의 음수 데이터 삭제"])

            st.write(df_negative_columns_with_only_zero_label)
            st.text("제거된 데이터 수: 150 개")

# 모델
with pages[2]:
    st.markdown("<h4>모델</h4>", unsafe_allow_html=True)

    # 서브탭 설정
    model_tabs = st.tabs(["모델 성능 비교", "최종 모델"])

    # 모델 성능 비교 탭
    with model_tabs[0]:
        local, cloud = image_files[9]
        df_models_scores = pd.read_csv(get_file_path(local, cloud), converters={
            'Scaler': str,  # 'Scaler' 컬럼은 문자열로 처리
            'PCA': str       # 'PCA' 컬럼도 문자열로 처리
        })
        
        # 모델 타입 선택 (이진/다중 분류)
        model_type = st.radio("모델 타입 선택", ["Binary", "Multi"])
        
        if model_type == "Multi":
            # 다중 분류 모델에 대한 설정
            st.subheader("다중 분류 모델 필터링")
            
            # 스케일러 버튼 (None, MinMax, Standard)
            scaler_type = st.radio("스케일러 선택", ['None', 'MinMaxScaler()', 'StandardScaler()'], index=0)

            # PCA 버튼 (None, 분산 0.99, 주성분 10)
            pca_type = st.radio("PCA 선택", ['None', '0.99', '10'], index=0)
            
            # 다중 분류 모델 필터링 (Type이 Multi인 모델만)
            multi_models = df_models_scores[df_models_scores['Type'] == "multiclass"]

            # 다중 분류 모델을 다중 선택할 수 있게 하기
            selected_models = st.multiselect("다중 분류 모델 선택", multi_models['Model'].unique(), default=multi_models['Model'].unique())
            
            # 선택된 모델에 맞게 필터링
            filtered_data = df_models_scores[
                (df_models_scores['Type'] == "multiclass") &
                (df_models_scores['Scaler'] == str(scaler_type)) &
                (df_models_scores['PCA'] == str(pca_type)) &
                (df_models_scores['Model'].isin(selected_models))
            ]
            
            # 성능 지표 4개 (Accuracy, F1 Score, MSE, R2)를 꺾은선 그래프로 시각화
            if not filtered_data.empty:
                st.subheader(f"성능 지표 (모델: {', '.join(selected_models)})")
                metrics = ['Accuracy', 'F1 Score', 'R2', 'MSE']
                
                plt.figure(figsize=(12, 6))
                
                # 각 모델에 대해 성능 지표를 꺾은선 그래프로 그리기
                for model in selected_models:
                    model_data = filtered_data[filtered_data['Model'] == model]
                    sns.lineplot(x='Metric', y='Value', data=model_data.melt(id_vars=["Model"], value_vars=metrics, var_name="Metric", value_name="Value"), label=model)
                
                plt.title(f"다중 분류 모델 성능 비교 (스케일러: {scaler_type}, PCA: {pca_type})")
                plt.xlabel('성능 지표')
                plt.ylabel('성능 값')
                plt.legend(title='모델', bbox_to_anchor=(1.05, 1), loc='upper left')
                st.pyplot(plt)

            else:
                st.write("선택한 조건에 맞는 모델이 없습니다.")
        
        elif model_type == "Binary":
            # 이진 분류 모델에 대한 설정
            st.subheader("이진 분류 모델 필터링")
            
            # 이진 분류 모델 필터링 (Type이 Binary인 모델만)
            binary_models = df_models_scores[df_models_scores['Type'] == "binary"]

            # 선택된 모델에 맞게 필터링
            filtered_data = df_models_scores[
                (df_models_scores['Type'] == "binary") &
                (df_models_scores['Scaler'] == "StandardScaler()") &
                (df_models_scores['PCA'] == str(None))
            ]
            
            # 성능 지표 4개 (Accuracy, F1 Score, MSE, R2)를 꺾은선 그래프로 시각화
            if not filtered_data.empty:
                st.markdown('#### 스케일러: StandardScaler(), PCA: None)')
                
                # 데이터 변형 (melt로 성능 지표를 길게 변환)
                filtered_data_melted = filtered_data.melt(id_vars=["Model"], value_vars=['Accuracy', 'F1 Score', 'R2', 'MSE'],
                                                          var_name="Metric", value_name="Value")
                
                # 성능 지표를 꺾은선 그래프로 그리기
                plt.figure(figsize=(12, 6))
                sns.lineplot(x="Metric", y="Value", hue="Model", data=filtered_data_melted, marker='o')
                
                plt.title(f"이진 분류 모델 성능 비교")
                plt.xlabel('성능 지표')
                plt.ylabel('값')
                plt.legend(title='모델', bbox_to_anchor=(1.05, 1), loc='upper left')
                st.pyplot(plt)
            
    # 최종 모델 탭
    with model_tabs[1]:
        st.subheader("최종 모델 성능")
        # 최종 모델 성능을 찾기
        best_model = df_models_scores[(df_models_scores['Model'] == 'xgb') & 
                                    (df_models_scores['Scaler'] == 'None') & 
                                    (df_models_scores['PCA'] == 'None')]

        # 성능 지표
        accuracy = best_model['Accuracy'].values[0]
        f1_score = best_model['F1 Score'].values[0]
        mse = best_model['MSE'].values[0]
        r2 = best_model['R2'].values[0]

        # 성능 지표를 시각화
        fig, ax = plt.subplots()
        metrics = ['Accuracy', 'F1 Score', 'R2', 'MSE']
        values = [accuracy, f1_score, r2, mse]

        ax.bar(metrics, values, color=['blue', 'green', 'orange', 'red'])
        ax.set_ylabel('Score')
        ax.set_title('Model Performance Metrics')
        st.pyplot(fig)

        # classification_report 파일 경로
        local, cloud = image_files[10]
        report_path = get_file_path(local, cloud)
        

        # classification_report 읽기
        with open(report_path, "r") as f:
            report_content = f.read()

        # classification_report를 Streamlit에 표시
        st.subheader("Classification Report")
        st.text(report_content)

# 보고서
with pages[3]:
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