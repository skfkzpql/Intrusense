import streamlit as st
from PIL import Image
import os
import re

# 결과 이미지 경로 설정
output_folder = '../../results/figures/column_visualizations/'

st.title("Intrusense: Data Visualization")

# 카테고리별 칼럼 분류
categories = {
    "포트 및 트래픽량 관련": [ 
        'Destination Port', 'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
        'Total Length of Fwd Packets', 'Total Length of Bwd Packets', 'Flow Bytes/s', 'Flow Packets/s'
    ],
    "패킷 길이 관련": [
        'Fwd Packet Length Max', 'Fwd Packet Length Min', 'Fwd Packet Length Mean',
        'Fwd Packet Length Std', 'Bwd Packet Length Max', 'Bwd Packet Length Min',
        'Bwd Packet Length Mean', 'Bwd Packet Length Std', 'Min Packet Length', 'Max Packet Length',
        'Packet Length Mean', 'Packet Length Std', 'Packet Length Variance'
    ],
    "플래그 및 헤더 관련": [
        'Fwd PSH Flags', 'Bwd PSH Flags', 'Fwd URG Flags', 'Bwd URG Flags',
        'Fwd Header Length', 'Bwd Header Length', 'FIN Flag Count', 'SYN Flag Count',
        'RST Flag Count', 'PSH Flag Count', 'ACK Flag Count', 'URG Flag Count',
        'CWE Flag Count', 'ECE Flag Count', 'Fwd Header Length.1'
    ],
    "속도 및 비율 관련": [
        'Fwd Packets/s', 'Bwd Packets/s', 'Down/Up Ratio', 'Average Packet Size',
        'Avg Fwd Segment Size', 'Avg Bwd Segment Size'
    ],
    "세그먼트 및 하위 플로우 관련": [
        'Fwd Avg Bytes/Bulk', 'Fwd Avg Packets/Bulk', 'Fwd Avg Bulk Rate',
        'Bwd Avg Bytes/Bulk', 'Bwd Avg Packets/Bulk', 'Bwd Avg Bulk Rate',
        'Subflow Fwd Packets', 'Subflow Fwd Bytes', 'Subflow Bwd Packets', 'Subflow Bwd Bytes'
    ],
    "시간 관련": [
        'Flow IAT Mean', 'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Total',
        'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min', 'Bwd IAT Total',
        'Bwd IAT Mean', 'Bwd IAT Std', 'Bwd IAT Max', 'Bwd IAT Min', 'Active Mean',
        'Active Std', 'Active Max', 'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min'
    ],
    "윈도우 크기 및 기타": [
        'Init_Win_bytes_forward', 'Init_Win_bytes_backward', 'act_data_pkt_fwd',
        'min_seg_size_forward'
    ],
    "레이블 및 메타정보": ['Label', 'source', 'id']
}

# 탭 생성
tabs = st.tabs(list(categories.keys()))

# 각 탭에서 시각화 표시 및 검색 기능 추가
for tab, (category_name, columns) in zip(tabs, categories.items()):
    with tab:
        st.header(f"{category_name}")
        
        # 검색 상자
        search_query = st.text_input(f"Search in {category_name}", key=category_name).strip().lower()
        
        # 검색어로 필터링
        filtered_columns = [col for col in columns if search_query in col.lower()] if search_query else columns
        
        if filtered_columns:
            for column in filtered_columns:
                safe_column_name = re.sub(r'[\\/:"*?<>|]', '_', column)
                
                # 박스플롯 시각화
                boxplot_path = os.path.join(output_folder, f"{safe_column_name}_boxplot.png")
                if os.path.exists(boxplot_path):
                    st.subheader(f"{column} - Boxplot")
                    st.image(Image.open(boxplot_path), use_column_width=True)
                
                # 파이 차트 시각화
                pie_chart_path = os.path.join(output_folder, f"{safe_column_name}_pie_chart.png")
                if os.path.exists(pie_chart_path):
                    st.subheader(f"{column} - Pie Chart")
                    st.image(Image.open(pie_chart_path), use_column_width=True)
        else:
            st.warning(f"No visualizations found for '{search_query}' in {category_name}.")
