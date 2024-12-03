Intrusense

□ 개요
산출물 단계 : 결과보고 
평가 산출물 : 프로젝트 시각화
제출 일자 : 12/5
깃허브 경로 https://github.com/JiAhLee903/Intrusense/pulls
작성 팀원 : 조현,손윤기,이지아,문경은


# 프로젝트 개요: 네트워크 트래픽 기반 침입 탐지 모델 개발

## 프로젝트 목표
CIC-IDS2017 데이터셋을 활용하여 네트워크 트래픽 기반 침입 탐지 모델을 개발한다. 이 모델은 다음과 같은 기능을 수행한다:
1. **정상/비정상 트래픽 분류**  
2. **연속적인 공격 패턴 식별**  
3. **이상 트래픽 탐지**

결과적으로 하나의 트래픽이라도 침입으로 탐지된다면, 침입으로 판단하여 경고를 출력한다.


## 시장 분석

### 1. **시장 배경**
- **네트워크 침입 탐지 시장 성장세:**  
  전 세계적으로 네트워크 보안 위협이 증가함에 따라 침입 탐지 시스템(IDS) 및 이상 탐지 솔루션에 대한 수요가 빠르게 증가하고 있다.
  - 시장 규모: 2023년 기준 약 **47억 USD**로 추정  
  - 연평균 성장률(CAGR): **12.5% 이상** (2023~2030)  
- **위협 환경:**  
  - 새로운 공격 유형 증가: 제로데이 공격, 랜섬웨어, 피싱 공격 등  
  - 네트워크 트래픽의 복잡성 증가: 클라우드 전환 및 IoT 디바이스 사용 증가  

### 2. **기술 동향**
- 머신러닝과 딥러닝을 활용한 **지능형 침입 탐지 시스템** 개발이 활발히 진행 중이다.  
  - 특히, 비지도 학습 기반의 이상 탐지와 실시간 탐지 기술이 주목받고 있음.  
- 전통적인 규칙 기반 IDS보다 높은 **정확도**와 **유연성**을 제공하는 **AI 기반 솔루션**의 채택률 증가.  

### 3. **경쟁 분석**
- **주요 경쟁 기술:**  
  - 기존 상용 제품: Snort, Suricata, Cisco Stealthwatch 등  
  - Open-source IDS: Zeek(Bro), OSSEC 등  
- **차별화 포인트:**  
  - 본 프로젝트는 머신러닝, 딥러닝, 비지도 학습을 조합한 **하이브리드 방식**을 사용하여 높은 탐지율과 낮은 오탐률을 목표로 한다.  
  - 실시간 시각화를 지원하여 결과 해석이 용이하며, 사용자의 요구에 따라 **확장 가능**한 구조 제공.  

---

## 고객 파악

### 1. **타겟 고객**
- **기업 네트워크 보안 팀:**  
  - 중소기업(SMB): 제한된 자원으로 효율적인 침입 탐지가 필요한 기업  
  - 대기업: 대규모 네트워크 환경에서 신뢰도 높은 IDS 솔루션을 요구하는 기업  
- **보안 솔루션 제공 업체:**  
  - 침입 탐지 및 보안 모니터링 서비스 제공 기업  
  - 데이터 분석 및 네트워크 관리 소프트웨어 기업  

### 2. **고객 니즈**
- **정확한 탐지:**  
  - 오탐(False Positive)을 최소화하고 탐지 정확도 향상  
- **모델 확인 시각화 도구:**  
  - 모델의 성능과 탐지 결과를 직관적으로 확인할 수 있는 대시보드

### 3. **기대 효과**
- 침입 탐지 시스템 도입을 통해 기업은 네트워크 보안을 강화하고, 잠재적인 위협에 대한 신속한 대응 능력을 확보할 수 있다.  
- 고객의 네트워크 환경에 맞춘 맞춤형 솔루션 제공 가능.



### 선택훈련 사용기술
⦁	주요 라이브러리:
⦁	Pandas 및 NumPy: 데이터 조작 및 분석
     # 데이터로드, 
     # 데이터분할(x,y 변수분리), 
     # 학습(trian)_테스트(test)세트로 분할 
     # 데이터 표준화, #표준화데이터 저장 #결과 저장 경로 생성
⦁	scikit-learn: 머신러닝 및 전처리
     # PCA
⦁	Streamlit : 시각화
     # 주요시각화 
        1. EDA데이터결과
        2. 모델성능지표 (Precision,Recall,F1-score등)
        3. 탐지된 침입 패턴과 이상트래픽 정보
⦁	PyTorch (선택): AutoEncoder와 같은 딥러닝 모델 구현
⦁	모델 - 하이브리드
⦁	정상/비정상 트래픽 분류: 
⦁	(지도 학습) 로지스틱, 랜덤 포레스트, Support Vector Machine, XGBoost
⦁	연속적인 공격 패턴 식별: (딥러닝) LSTM, ANN, CNN
⦁	이상 탐지(미리 정의되지 않은 새로운 공격 패턴 탐지): (비지도 학습) Isolation Forest, Autoencoders


## 예상 문제점
- **데이터 불균형**
  - 일반적으로 정상 트래픽이 공격 트래픽에 비해 훨씬 많음
  - 해결 방법: 오버 샘플링(소수 클래스 복제), 모델의 가중치 조정(소수 클래스에 높은 가중치 부여), 모델 평가지표를 정확도 외에 다른 지표도 사용 (Precision, Recall, F1-score, AUC_ROC 등), 새로운 데이터셋을 평가 데이터로 사용
- **많은 데이터 수와 칼럼 수**
  - 모델 학습 저하와, 차원의 저주, 메모리 문제등 발생 가능
  - 해결 방법: 상관관계가 높은 칼럼을 제거하거나, 중요한 정보만 남기도록 차원 축소, 배치 학습으로 나누어 학습

##프로젝트 진행방향
[[[[[ E D A ]]]]] 데이터 탐색, 시각화, 상관 분석, 이상치 탐지

  - **data_summary.ipynb**: 데이터셋에 대한 기본적인 요약(행, 열, 데이터 타입, 결측값 등)을 확인하는 노트북
- **missing_values_analysis.ipynb**: 결측값 확인 및 처리 방법 분석
- **correlation_analysis.ipynb**: 피처 간 상관관계를 분석하여 중요한 변수나 다중공선성 문제를 파악
- **distribution_visualization.ipynb**: 각 피처의 분포를 시각화 (히스토그램, 박스플롯 등)
- **target_analysis.ipynb**: 타겟 변수에 대한 분석 (클래스 분포, 통계적 특성 등)
- **clustering_analysis.ipynb**: 군집 분석을 통해 
 패턴을 찾는 분석 (KMeans, DBSCAN 등)
- **outlier_detection.ipynb**: 이상치 탐지 및 시각화 (IQR, Z-Score 등)
- **feature_distribution_transformation.ipynb**: 피처의 분포를 변환 (로그 변환, 제곱근 변환 등)
- **visualization.ipynb**: 전반적인 데이터 시각화 및 주요 패턴을 발견하기 위한 분석


[[[[[ Preprocessing ]]]]]
     데이터 정리, 전처리, 피처 엔지니어링, 스케일링
     - **data_cleaning.ipynb**: 결측값 처리, 이상치 처리, 중복 데이터 처리 등 데이터 정리
- **feature_engineering.ipynb**: 새로운 피처 생성, 변수 변환, 파생 변수 생성 등
- **scaling_and_normalization.ipynb**: 데이터 표준화 및 정규화 (StandardScaler, MinMaxScaler 등)
- **handling_missing_values.ipynb**: 결측값 처리 기법 (평균/중앙값 대체, 예측 모델 사용 등)
- **feature_selection.ipynb**: 중요한 피처를 선택하기 위한 기법 (특징 선택, 차원 축소 등)

[[[[[ Modeling ]]]]] 모델 훈련, 하이퍼파라미터 튜닝, 성능 평가

- **model_training.ipynb**: 다양한 분류/회귀 모델을 훈련하는 노트북 (랜덤포레스트, SVM, XGBoost 등)
- **hyperparameter_tuning.ipynb**: 모델의 하이퍼파라미터 튜닝을 위한 그리드 서치나 랜덤 서치
- **model_evaluation.ipynb**: 모델 성능 평가 (정확도, F1 Score, ROC-AUC 등)
- **model_comparison.ipynb**: 여러 모델의 성능 비교 및 분석

[[[[[ Visualization ]]]]] 데이터 및 모델 성능 시각화
- **data_visualization.ipynb**: 데이터 탐색과 전처리 단계에서의 주요 시각화 작업
- **model_performance_visualization.ipynb**: 모델 성능 평가 지표를 시각화 (Confusion Matrix, ROC Curve, Feature Importance 등)


## 프로젝트 구성

### 1. **데이터셋**
- 사용 데이터셋: **CIC-IDS2017**
- 데이터 저장 방식: **MySQL 데이터베이스**
- 칼럼 구성: 78개의 피처와 타겟 레이블 / 225,745개 Row
**피처 종류:
포트 및 트래픽량
패킷 길이
플래그 및 헤더
속도 및 비율
세그먼트 및 하위 플로우
시간
**대표 공격 5가지 :
**주요 칼럼:
  - **Flow Duration**: 흐름의 지속 시간, 공격과 정상 트래픽 간 차이를 파악할 수 있는 중요한 지표입니다.
  - **Total Fwd Packets**, **Total Backward Packets**: 전송된 총 패킷 수 및 수신된 패킷 수는 네트워크 트래픽 분석 시 중요한 역할을 합니다. 예를 들어, DDoS 공격은 패킷 수가 급격히 증가할 수 있습니다.
  - **Flow Bytes/s**, **Flow Packets/s**: 초당 바이트 수와 패킷 수는 흐름의 속도와 강도를 나타냅니다. 이상 트래픽에서는 이러한 값들이 급격히 달라질 수 있습니다.
  - **Flow IAT Mean**, **Flow IAT Std**: 흐름 간 간격은 트래픽의 시간 간격을 나타냅니다. 공격 시에는 이 간격이 일정하지 않거나 비정상적으로 변할 수 있습니다.
  - **Fwd Packet Length Max**, **Fwd Packet Length Mean**: 순방향 패킷의 최대 및 평균 길이는 트래픽의 특성을 파악하는 중요한 요소입니다.
  - **Bwd Packet Length Max**, **Bwd Packet Length Mean**: 역방향 패킷의 길이 역시 네트워크의 정상/비정상 패턴을 파악하는 데 유용한 특성입니다.
  - **PSH Flags Count**, **URG Flags Count**: 푸시(PSH)와 긴급(URG) 플래그가 설정된 패킷 수는 공격 식별에 중요한 역할을 합니다.
  - **SYN Flag Count**, **FIN Flag Count**, **RST Flag Count**: 연결 요청 및 종료에 관련된 플래그들은 공격을 구별하는 데 중요한 정보를 제공합니다.
  - **Label**: 각 트래픽 레이블 (정상, 공격 유형)은 모델 학습에 있어 필수적인 대상 변수로 작용합니다.
- 타겟 레이블: 
  - **BENIGN**: 정상 트래픽.  
  - **DDoS**: 분산 서비스 거부(Distributed Denial of Service) 공격.  
  - **PortScan**: 네트워크 포트를 스캔하여 취약점을 탐색하는 공격.  
  - **Bot**: 악성 봇에 감염된 장치가 네트워크에서 활동하는 공격.  
  - **Infiltration**: 네트워크 내부로 침투하여 권한을 탈취하거나 악성 활동을 수행.  
  - **Web Attack – Brute Force**: 비밀번호 등을 무차별 대입으로 추측하려는 웹 공격.  
  - **Web Attack – XSS**: 크로스 사이트 스크립팅을 통한 웹 공격.  
  - **Web Attack – SQL Injection**: SQL 문법을 이용해 데이터베이스를 공격하는 웹 공격.  
  - **FTP-Patator**: FTP 서버를 대상으로 하는 무차별 대입 공격.  
  - **SSH-Patator**: SSH 서버를 대상으로 하는 무차별 대입 공격.  
  - **DoS slowloris**: HTTP 연결을 과도하게 점유하여 서비스 장애를 유발하는 DoS 공격.  
  - **DoS Slowhttptest**: HTTP 헤더 등을 이용해 서버를 마비시키는 DoS 공격.  
  - **DoS Hulk**: 서버를 초과 부하 상태로 만들어 서비스 거부를 유발하는 DoS 공격.  
  - **DoS GoldenEye**: HTTP GET 요청을 남발하여 서버를 마비시키는 DoS 공격.  
  - **Heartbleed**: OpenSSL 라이브러리의 취약점을 악용해 민감한 정보를 유출하는 공격.  

### 데이터셋 ###
-**Drop Columns

### 표준화 ###
-**XGBoost


###PCA###
-**주성분 48개
-**HavingGridSearchCV
-**음수값처리 / 이상치제거 / 표준화 / 무한대값, NaN값 처리


### 2. **모델 개발**
-**가설**-
트래픽 데이터를 기반으로 침입 공격을 탐지 할 수 있을까?
1차 반박자료
-귀무가설(HO) 트래픽 데이터를 사용한 침입 공격 탐지 모델은
 정상트래픽/공격트래픽 간의 차이를 구별하지 못한다.
-상관계수와 IAT가 유효변수로 떠오르는 것
-공격은 패킹, 즉 트래픽과 관련없다 가설 반박
2차 반박자료
-T검정을 사용하여 PVALUE값 근거로 밀접함을 증명
-COMPARISON자료로 1차 반박에 있던 IAT변수에 평균과분산을
확인하면 확연한 차이
- **지도 학습 모델:**  
  - 머신러닝 기반 앙상블 모델
    (LogisticRegression, Random Forest, XGBoost)
     로지스틱 회귀결과 -
     랜덤포레스트 결과 -
      XGboost 결과 - 
- **딥러닝 모델:**  
  - 예: LSTM(Long Short-Term Memory), DNN(Deep Neural Network), ANN(Artificial Neural Network)
- **비지도 학습 모델:**  
  - 예: Isolation Forest, Autoencoders, Local Outlier Factor 등 이상 탐지 모델
- **결과 결합 방식:**  
  - 각 모델의 결과를 **OR 결정**(하나라도 침입으로 탐지 시 침입으로 판단)

### 3. **결과 시각화**
- **도구:** Streamlit
- **주요 시각화 항목:**  
  - 데이터 EDA 결과  
  - 모델별 성능 지표(Precision, Recall, F1-score 등)  
  - 탐지된 침입 패턴과 이상 트래픽 세부 정보  


