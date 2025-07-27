# Doosan Robotics Boot Camp(2025.01.06 ~ 2025.07.06)
## 3. ROKEY B-3조 협동-3 Project (디지털 트윈 기반 서비스 로봇 운영 시스템 구성) DigitalTwin_Simul
&nbsp;
## 🧠 Rokey 휴게소 : 차선, 신호등 인식 / 표지판 인식 parking / slam & nav tunnel


&nbsp;

## 🔗 참고자료
https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/

&nbsp;

## 📑 목차

1. [📌 프로젝트 개요](#1--프로젝트-개요)
2. [🔧 구성 요소](#2--구성-요소)  
3. [💻 사용 기술](#3--사용-기술)  
4. [🧭 동작 흐름 요약](#4--동작-흐름-요약)  
5. [💻 코드 실행 방법](#5--코드-실행-방법)  
6. [📷 시연 영상/이미지](#6--시연-영상--이미지)  
7. [🌟 기대 효과/ 한계점 및 개선점](#7--기대-효과)  

   
&nbsp;
## 1. 📌 프로젝트 개요

휴게소는 운전자와 차량이 잠시 정차하여 휴식을 취하는 중요한 공간이며, 자율주행 기술이 적용될 경우 이 과정 역시 자동화되어야 합니다.  
본 프로젝트 **Rokey 휴게소 Autodrive Simulation**은 AI Vision과 센서 기반 자율주행 기술을 활용하여  
차량이 휴게소 내 다양한 표지와 상황(신호등, 주차장, 공사구간, 터널 등)에 반응하여 동작하는 시뮬레이션 시스템입니다.


&nbsp;
### 🎯 기획 의도

- 신호등, 주차 표지, 공사 구간 등 **휴게소 내 도로 요소**를 인식하고 상황에 맞는 행동을 수행할 수 있도록 설계하였습니다.
- **AI Vision 기반 인식 기술**과 **센서 제어 기반 자율주행 기술**을 통해 차량이 다양한 조건에서 정확하게 주행합니다.
- **정지, 감속, 회피, 주차, 진입 판단** 등의 동작을 자동으로 수행함으로써 자율주행의 유연성을 높입니다.
- 실제 도로와 유사한 환경 속에서 **판단 기반 시뮬레이션 주행**을 구현하는 것이 목적입니다.
  
&nbsp;
### 🏭 기존 기술의 활용과 협동로봇의 확장 가능성
- 기존 자율주행 기술은 대부분 **차선 유지, 속도 제어, 충돌 회피** 등 직선 도로 위주로 구성되어 있으며,  
  **휴게소와 같은 복합 환경에서의 정적·동적 판단**은 미흡한 부분이 있었습니다.

- 본 프로젝트는 다음과 같은 방식으로 기존 기술을 확장하여 적용했습니다:
  - **AI Vision**으로 휴게소 내 다양한 도로 표지(신호등, 주차, 공사, 터널)를 정확히 인식하고,
  - **센서 기반 로직**을 통해 해당 표지에 따른 동작(정지, 회피, 진입 등)을 수행하며,
  - **정해진 시나리오 흐름도**에 따라 차량이 휴게소 내부를 스스로 판단하며 주행합니다.

- 본 시스템은 향후 다음과 같은 분야로도 확장 가능성이 있습니다:
  - 고속도로 휴게소 자율 정차 시스템
  - 자율주행차량 정적/동적 판단 시뮬레이터
  - 물류 이동 경로 내 정지 및 회피 자동화 시스템
  - 스마트 시티 주차 유도 시스템 등

- 향후 Rokey 휴게소 시스템은 정밀 자율주행, 스마트 정차, 경로 판단 로직이 필요한 다양한 영역에 확대 적용 가능성이 있으며, 특히 고속도로, 휴게소, 물류 환경에서의 **주행 안정성과 편의성 향상**에 실질적인 해결책을 제시할 수 있습니다.

&nbsp;
## 2. 🔧 구성 요소

| 구성 요소 | 설명 |
|-----------|------|
| 🛣 **휴게소 자율주행 맵 (Autorace Map)** | lane, 신호등, 주차, 공사, 터널 및 세차 구간 포함 |
| 🤖 **TurtleBot3 Burger** | ROS2 기반 자율주행 모바일 로봇 시뮬레이터 |
| 📷 **Simulation Camera Sensor** | 실시간 카메라 이미지 수신 (e.g. `/camera/image_raw, /camera/image_compressed`) |

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/98018846-5aa0-45cf-a81a-8327cb4d99f8" />

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/2bdcc159-9922-4614-971a-f1bf3a278007" />

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/759f2ef7-9cea-4a75-a0bc-38efd0bd3718" />

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/36a35747-fe6f-4266-91f3-00d8ab624752" />

&nbsp;
## 3. 💻 사용 기술

| 기술 | 내용 |
|------|------|
| 🖥 **OS 및 플랫폼** | Ubuntu 22.04, ROS2 Humble |
| 🤖 **시뮬레이터 툴** | Turlebot3, Gazebo, Slam, Navigation |
| 🧠 **FSM 기반 주행 제어** | lane → signal → parking → tunnel로 상태 기반 주행 흐름 전환 |
| 🚦 **HSV 기반 신호등 인식** | OpenCV HSV 마스킹으로 빨강/노랑/초록 신호 감지 및 속도 조절 |
| 🔍 **SIFT Keypoint 기반 표지판 인식** | 주차 / 공사 / 터널 표지판 인식을 위해 SIFT 특징점 추출 및 FLANN 매칭 수행 |
| 🗺️ **SLAM 기반 지도 작성** | 터널/세차장 내부 경로 파악 및 이동을 위한 `slam_toolbox` 활용 |
| 🎯 **Navigation 목표 지점 주행** | SLAM으로 생성한 맵 위에서 목표 좌표 설정 및 이동 (e.g. 세차구역, 복귀경로 등) |
| 🖥 **Rviz2** | SLAM 지도, 경로, 센서 정보 시각화 도구 |

&nbsp;
### 📷 Vision 
**1. HSV 기반 차선 인식 (detect_lane.py)**

- **목적**: 카메라 입력 영상을 HSV 색공간으로 변환하여 흰색 / 노란색 차선과 신호등 색상(빨강, 노랑, 초록)을 안정적으로 인식하고 주행 판단에 활용함

- **처리 흐름**:

- 색상 필터링 파라미터 선언 (`self.declare_parameters`)  
  - hue, saturation, lightness 값 범위를 흰색과 노란색 각각에 대해 정의  
  - 예시:  
    - 흰색: hue 0-179, saturation 0-30, lightness 190-255  
    - 노란색: hue 20-40, saturation 100-255, lightness 130-255  
  - `is_detection_calibration_mode`가 True일 경우, 실시간 HSV 범위 조절 가능

- 입력 및 출력 흐름  
  - `/camera/image_raw` 또는 `/detect/image_input/compressed` 토픽으로 실시간 이미지 수신  
  - 압축 여부에 따라 `raw` 혹은 `compressed` 이미지 수신 가능  
  - 이미지 처리 후 중심선 정보 `/detected_lane` 토픽으로 퍼블리시  
  - 결과 이미지는 `/detect/image_output` 토픽으로 퍼블리시되어 RQT 등에서 확인 가능

- 이미지 처리 과정(`cbFindLane`)
  - 성능 최적화를 위해 3프레임 중 1프레임만 처리  
  - 입력 이미지를 `cv2.cvtColor()`를 통해 HSV로 변환  
  - `cv2.inRange()`를 사용해 흰색과 노란색 차선을 각각 마스킹  
  - 각각 `maskWhiteLane()`, `maskYellowLane()` 함수로 처리

- 차선 검출 로직
  - 각 마스크의 픽셀 수(`fraction_num`)를 계산  
  - 특정 임계값(예: 3000) 이상일 경우 `fit_from_lines()`로 곡선 추정  
  - 임계값 미달이거나 예외 발생 시 `sliding_window()` 알고리즘으로 대체  
  - 차선 중심선을 계산하여 `/detected_lane` 토픽으로 Float64 타입으로 퍼블리시


&nbsp;
### 🤖 FSM
**2. 차선 추종 및 회피 제어 (control_lane.py)**

- **목적**:  차선 중심선 기반의 자율 주행과 장애물 회피 상황을 구분하여 차량의 속도 및 방향을 제어하고, 회피 중에도 즉각적인 대응이 가능하도록 MUX 구조를 활용한 토픽 전환 제어 수행

- **처리 흐름**:

- 제어 토픽 설정  
  - 차선 추종 및 회피 제어 결과는 모두 `/lane/cmd_vel`로 퍼블리시됨  
  - `/mode/cmd_source`에 따라 현재 상태(lane, traffic_light, parking 등)에 맞는 `cmd_vel`을 MUX를 통해 선택

- 기본 주행 제어 (`callback_follow_lane`)
  - 회피 모드(`avoid_active`)가 False일 때만 동작  
  - `/detected_lane`의 중심선 오차를 기준으로 선형 속도(`linear.x`)와 각속도(`angular.z`)를 계산하여 퍼블리시  
  - 차선 중심선 기반으로 방향을 조정하며 직진 주행 수행

- 장애물 회피 제어 (`callback_avoid_active`, `callback_avoid_cmd`)
  - `/avoid_active` 토픽을 통해 회피 모드 전환 여부를 Boolean으로 수신  
    - `True`: 회피 모드 진입 → 차선 추종 정지  
    - `False`: 기본 주행 모드 유지  
  - 회피 모드 진입 시, `/avoid_control`에서 받은 `Twist` 메시지를 즉시 `/lane/cmd_vel`로 퍼블리시  
    → 장애물을 회피하는 동작 수행 (회피 제어 우선)

- 긴급 정지 및 경고 시스템:

  - 사각지대 감지 (`cb_blind_spot`)
    - 후방 센서 등으로 사각지대 차량 탐지 시 `Blind-spot! Emergency brake.` 메시지와 함께 정지 동작 수행

  - 긴급 정지 (`cb_emergency`)
    - 외부에서 긴급 정지 신호 수신 시 즉시 차량 정지
    - `Emergency STOP activated!` 로그 출력 및 정지 수행

  - IMU 기반 경사 감지 (`cb_imu`)
    - IMU 센서의 쿼터니언 → Roll 각도로 변환
    - 일정 경사(`roll_angle_threshold`) 이상일 경우 클락션 울리고 속도 감속 (MAX_VEL의 0.5배)

  - 클락션 작동 (`sound_horn`)
    - Bool 타입 메시지를 `/pub_horn`으로 퍼블리시하여 경고음 발생
    - 사용 예: 경사 위험, 회피 중 신호 등

&nbsp;
### 📷 Vision 
**3. 신호등 인식 (detect_traffic_light.py)**

- **목적**: 빨강, 노랑, 초록 신호등 색상 인식을 위해 Hue(색상) 최소값과 최대값을 설정하여 감지함
  
- **처리 흐름**:
  
- 이미지 구독
  - 신호등 영상 입력을 `CompressedImage` 형식으로 구독함
  - 토픽 이름은 `/detect/image_input/compressed`이며, 실시간 이미지 데이터 수신

- 결과 퍼블리시
  - 감지된 신호등 색상 결과를 `String` 메시지로 변환
  - 토픽 `/traffic_light_color`에 퍼블리시하여 외부 시스템과 연동 가능

- 주기적 처리
  - 약 0.1초마다 신호등 색상 검사를 수행하는 타이머 생성
  - 일정 주기로 콜백 함수가 호출되어 이미지 처리를 반복

- 이미지 처리 흐름 (timer_callback)
  - 이미지 디코딩
    - 구독한 CompressedImage 데이터를 OpenCV에서 처리 가능한 BGR 이미지로 디코딩

  - 색상 마스크 검사
    - 디코딩된 이미지에 대해 빨강 → 노랑 → 초록 순서로 마스크 필터를 적용
    - 각 색상에 대해 픽셀 수가 일정 수치 이상이면 해당 색상으로 판단하여 결과 퍼블리시
    - 가장 먼저 감지된 색상 하나만 발행하고 종료 → 중복 감지 방지

&nbsp;
### 🤖 FSM
**4. 신호등 제어 (control_traffic_light.py)**
- **목적**:  신호등 색상에 따라 차량의 속도를 동적으로 조절하고, 일정 시간이 경과하거나 조건이 충족되면 `traffic_light` 모드와 `lane` 모드로 진행

- **처리 흐름**:
  
- `detect_traffic_light` 노드로부터 신호등 색상(`traffic_light_color`)이 감지되면  
  `lane` 모드에서 `traffic_light/cmd_vel` 모드로 전환되어 제어를 수행함

- `detect_traffic_light`는 지속적으로 신호등 색깔을 publish 하지만  신호등 색상이 변할 때에만 동작을 제어하도록 구성됨

- 색상에 따라 차량의 속도(`twist.linear.x`)가 아래와 같이 설정됨:
  - green 감지 → 속도 `0.15`
  - yellow 감지 → 속도 `0.03`
  - red 감지 → 속도 `0.0`

- 신호등 색상이 바뀔 경우:
  - 현재 색상을 이전 색상과 비교하여 변화가 있는 경우에만 제어 실행
  - 중복 감지 방지를 위해 이전 색상과 동일하면 무시됨

- 색상 감지 이후, `timer_callback`에서 4초가 지나도록 신호등 색상 변화가 없다면  
  다시 `lane` 모드로 복귀

- 단, 복귀 이후 5초가 지나면 더 이상 `traffic_light` 모드로 복귀하지 않도록 제한됨

- 이를 통해 신호등 제어 이후 일정 시간 내에서만 다시 lane 모드로 복귀 가능하며  
  일정 시간이 지나면 신호등 제어를 종료하고 lane 기반 제어로 고정됨

&nbsp;
### 📷 Vision 
**5. 표지판 인식 통합 (detect_signcombine.py)**
- **목적**: `detect_sign_parking`, `detect_sign_construction`, `detect_sign_tunnel` 노드를 하나로 통합한 노드로
세 가지 표지판(png 이미지)을 기준으로 현재 보고 있는 영상에서 일치 여부를 판단하여 감지된 표지판 정보를 퍼블리시하고, 시각화 결과를 전송

- **처리 흐름**:

- 이미지 수신
  - 카메라 또는 센서로부터 입력된 이미지(`raw` 또는 `compressed`)를 수신
  - 압축 여부에 따라 디코딩 방식이 달라짐

- SIFT Keypoint 추출 및 Descriptor 계산
  - 입력된 이미지에서 특징점(Keypoint) 추출
  - 각 특징점 주변 패턴을 숫자 벡터(Descriptor) 로 변환
    - 16x16 영역을 세분화한 뒤 방향성(Gradient) 정보를 이용해 129차원 벡터 생성

- 템플릿 이미지 매칭
  - 템플릿 이미지: `parking.png`, `construction.png`, `tunnel.png`  
  - 입력 이미지와 템플릿 이미지 간의 특징점 매칭 수행
    - FLANN 매칭 알고리즘을 사용하여 유사한 특징점을 연결
    - keypoint 수와 매칭 품질 기반으로 인식 여부 판단

- 매칭 기준 및 판단
  
  - 유효한 매칭(Good Match)이 8개 이상이고,  
    템플릿과 입력 이미지 사이의 MSE(평균제곱오차)가 5000 이하일 때 인식 성공으로 판단
  
  - 인식된 표지판에 따라 `UInt8` 메시지를 퍼블리시:
    - 주차 표지판 → `0`
    - 공사 표지판 → `1`
    - 터널 표지판 → `2`

- 결과 이미지 전송
  - 시각화용 drawMatches 이미지를 생성하여 `/detect/image_output`으로 전송
  - 이미지 압축 여부(`compressed`, `raw`)에 따라 전송 형식 결정됨

&nbsp;
### 🤖 FSM
**6. 주차 동작 제어 (detect_parking.py)**
- **목적**:  주차 관련 표지판 감지 후 실제 차량의 Twist 제어를 통해 주차 및 복귀 동작을 수행하는 노드

- **처리 흐름**:
  
- 주차 표지판 감지
  - `detect_signcombine` 등에서 Parking 표지판을 감지하면  
    `/parking/cmd_vel` 토픽으로 제어 mux가 전환됨

- 주차 시작 동작 실행
  - `detect_parking` 노드에서 Twist 메시지를 이용해 차량을 움직이며 주차 시퀀스를 실행함
  - 기본 주차 순서:  
    `전진 → 좌회전 → 전진`

- 공사(construction) 표지판 유무 확인
  
  - 주차 과정 중에 공사 표지판이 감지되는지 추가 확인 수행
  - 감지되면 별도의 경로로 진입하도록 분기 처리

- 공사 표지판 감지 시 동작
  - 감지된 방향에 따라 실제 주차 동작 실행
  - 일반 시퀀스:  
    `전진 → 우회전 (공사표지 반대방향) → 전진 → 후진 → 정지`

- 주차 완료 후 빠져나가기
  - 복귀 시퀀스:  
    `우회전 → 전진 → 우회전 → lane 모드 복귀`

- 복귀 완료 후 `/lane/cmd_vel` 토픽으로 MUX를 다시 전환하여  차선 주행 모드로 재진입
  
&nbsp;
### 🗺️ SLAM & Navigation
**7. 터널 구간 정지 제어 (detect_stop_tunnel.py)**
- **목적**: `tunnel` 표지판을 감지하면 차량을 완전히 정지시키는 역할을 수행하는 노드

- **처리 흐름**:

- 터널 표지판 감지
  - `detect_signcombine` 등에서 `tunnel` 표지판을 감지하면  
    `/tunnel/cmd_vel`로 MUX 제어 토픽이 전환됨

- 정지 동작 실행
  - `detect_stop_tunnel` 노드에서 해당 정보를 수신하면  
    Twist 메시지를 통해 정지 명령을 실행함
  
  - 속도 설정:
    - `twist.linear.x = 0.0` (선형 속도 0)
    - `twist.angular.z = 0.0` (회전 속도 0)
  
  - MUX 제어 소스를 `"tunnel"`로 설정하며  
    실제로 제어가 해당 노드에서 이루어지도록 전환됨
    
- 실제 정지 동작 수행
  - 설정된 Twist 메시지가 `/tunnel/cmd_vel`로 퍼블리시되며 TurtleBot3가 정지하는 물리적 동작을 수행
  
  - 이후에는 `self.stopped = True` 상태로 전환되어  
    동일한 터널 표지판에 대해 중복 정지 동작이 발생하지 않도록 방지

  
&nbsp;

## 4. 🧭 동작 흐름 요약
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/53e61b53-3e89-44b5-a0b5-f56c17f2c64f" />

### Autorace Map 휴게소 흐름도 순서
1. **Default**: 기본 `lane` 모드에서 차선 주행  
2. **Traffic Light**:  
   - 빨간불 → 정지  
   - 노란불 → 천천히 주행  
   - 초록불 → 빠르게 주행  
3. **Parking**:  
   - Parking sign 감지 시 → 주차 주행  
   - Construction sign 감지 시 → 반대 방향으로 회전 + 후면 주차  
4. **Stop Tunnel**:  
   - Tunnel sign 앞에서 정지 동작 수행  

&nbsp;
   
<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/f8ef1d66-7cc7-40a9-8767-2c9a3ef4c493" />

### 감지 → 명령 선택 → 제어 → 주행 실행

| 단계          | 설명                                                                 |
|---------------|----------------------------------------------------------------------|
| **1. 감지 (Detect)** | `detect_lane.py`, `detect_traffic_light.py`, `detect_sign_combine.py` |
| **2. MUX 선택**     | `/mode/cmd_source` 기준으로 하나의 `/cmd_vel`만 선택하여 출력             |
| **3. 제어 (Control)** | `control_lane.py`, `control_traffic_light.py`, `detect_parking.py`, `detect_stop_tunnel.py` |
| **4. 주행 (Drive)**   | 실제 Twist 메시지를 통해 로봇이 동작 수행     

&nbsp;

### Lane
<img width="300" height="600" alt="image" src="https://github.com/user-attachments/assets/415d72e3-ee14-4142-9070-d785122deb37" />

1. **카메라 영상 수신**  
   → `/camera/image_raw` 토픽으로 실시간 이미지 입력

2. **HSV 색공간 변환**  
   → OpenCV로 BGR 이미지를 HSV로 변환

3. **흰색/노란색 마스킹**  
   → HSV 범위 내 픽셀 필터링하여 차선만 추출

4. **곡선 피팅 및 시각화**  
   → 추출된 픽셀 기반으로 곡선을 추정 및 렌더링

5. **`detect_lane.py` 실행**  
   → 차선 정보 계산 및 퍼블리시

&nbsp;

### Traffic light
<img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/1db045b1-d5ca-4680-888e-1b37ebbe5020" />

1. **`detect_traffic_light.launch.py`**  
   → 신호등 감지 노드 실행, HSV 파라미터 설정

2. **`detect_traffic_light.py`**  
   → 카메라 영상 구독 및 OpenCV로 색상 감지 수행

3. **`/traffic_light_color` (토픽)**  
   → 감지된 색상 (`"RED"`, `"GREEN"` 등)을 퍼블리시

4. **감지 결과에 따라 속도 제어 or 정지 동작 수행**

5. **`control_traffic_light.launch.py`**  
   → 제어 노드 실행, 로봇 제어 명령 수행

&nbsp;

### Parking
<img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/b2d05606-93f5-408a-a950-ef579256b3e0" />

1. **`detect_signcombine.py`**  
   → 주차 표지판 감지  

2. **`/parking/cmd_vel`로 MUX 전환**  

3. **`detect_parking.py`**  
   → Twist로 전진 → 좌회전 → 전진 (초기 진입)  
   → construction sign 유무 확인  
   → 감지 시: 전진 → 우회전 → 전진 → 후진 → 주차  
   → 주차 완료 후: 우회전 → 전진 → 우회전 (lane 복귀)  

4. **`/lane/cmd_vel`로 MUX 전환**  
   → 차선 주행 모드 복귀
   
&nbsp;

### Tunnel
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/e6c79840-3cf0-45bb-b9c4-92cae988033b" />

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/0a2c3b3d-5910-4f89-a0ec-3231468ee26e" />

1. **`detect_signcombine.py`**
   → 터널 표지판 감지
2. **`/tunnel/cmd_vel`로 MUX 전환**  
3. **`detect_stop_tunnel.py`**  
   → Twist `linear.x = 0.0`, `angular.z = 0.0` 설정  
   → 로봇 실제 정지 수행

&nbsp;



## 5. 💻 코드 실행 방법

### 🚗 전체 시뮬레이션 실행 (Auto)
- 코드: [`turtlebot3_autorace_2020.launch.py`](./turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/worlds/turtlebot3_autorace_2020.world)

```bash
ros2 launch turtlebot3_gazebo turtlebot3_autorace_2020.world
```


&nbsp;

### 🎥 내부 카메라 캘리브레이션 (Intrinsic)
- 코드: [`intrinsic_camera_calibration.launch.py`](./turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_camera/launch/intrinsic_camera_calibration.launch.py)

```bash
ros2 launch turtlebot3_autorace_camera intrinsic_camera_calibration.launch.py
```

&nbsp;

### 📸 외부 카메라 캘리브레이션 (Extrinsic)
- 코드: [`extrinsic_camera_calibration.launch.py`](./turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_camera/launch/extrinsic_camera_calibration.launch.py)

```bash
ros2 launch turtlebot3_autorace_camera extrinsic_camera_calibration.launch.py
```

&nbsp;

### 🔀 MUX 제어 노드
- 코드: [`mux_node`](./turtlebot3_ws/src/cmd_vel_mux/cmd_vel_mux/mux_node.py)

```bash
ros2 run cmd_vel_mux mux_node
```

&nbsp;

### 🛣️ 차선 감지 (Detect Lane)
- 코드: [`detect_lane.launch.py`](./turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_detect/launch/detect_lane.launch.py)

```bash
ros2 launch turtlebot3_autorace_detect detect_lane.launch.py
```

&nbsp;

### 🧭 차선 제어 (Control Lane)
- 코드: [`control_lane.launch.py`](./turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_mission/launch/control_lane.launch.py)

```bash
ros2 launch turtlebot3_autorace_mission control_lane.launch.py
```

&nbsp;

### 🚦 신호등 감지 (Detect Traffic Light)
- 코드: [`detect_traffic_light.launch.py`](./turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_detect/launch/detect_traffic_light.launch.py)

```bash
ros2 launch turtlebot3_autorace_detect detect_traffic_light.launch.py
```

&nbsp;

### 🛑 신호등 제어 (Control Traffic Light)
- 코드: [`control_traffic_light.launch.py`](./turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_mission/launch/control_traffic_light.launch.py)

```bash
ros2 launch turtlebot3_autorace_mission control_traffic_light.launch.py
```

&nbsp;

### 🪧 표지판 감지 (Detect Sign Combine)
- 코드: [`detect_sign_combine.launch.py`](./turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_detect/launch/detect_signcombine.launch.py)

```bash
ros2 launch turtlebot3_autorace_detect detect_signcombine.launch.py
```

&nbsp;

### 🅿️ 주차 감지 및 제어 (Detect Parking)
- 코드: [`detect_parking.launch.py`](/turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_detect/launch/detect_parking.launch.py)

```bash
ros2 launch turtlebot3_autorace_detect detect_parking.launch.py
```

&nbsp;

### 🌉 터널 정지 감지 (Detect Stop Tunnel)
- 코드: [`detect_stop_tunnel.launch.py`](./turtlebot3_ws/src/turtlebot3_autorace/turtlebot3_autorace_detect/launch/detect_stop_tunnel.launch.py)

```bash
ros2 launch turtlebot3_autorace_detect detect_stop_tunnel.launch.py
```

&nbsp;
## 6. 📷 시연 영상 / 이미지
> https://youtu.be/A73iN4W6Q4w

&nbsp;
## 7. 🌟 기대 효과
### 📌 프로젝트 기대 효과

| 구분             | 효과                        | 설명                                             |
|------------------|-----------------------------|--------------------------------------------------|
| 기술 실현        | 라스트마일 자율주행         | 공공/상업 주차장, 물류창고 등에 적용 가능        |
| 사용자 편의성 향상 | 주차 스트레스 감소          | 주차 공간 탐색/충돌 위험 감소                    |
| 🅿️ 공간 효율성   | 주차 최적화                  | 경차/전기차 등 분류 주차로 공간 활용 극대화      |
| 사회적 포용성    | 교통 약자 고려              | 장애인·고령자 차량 자동 인식 및 근접 배치        |
| 지속가능성       | 전기차 충전 구역 자동 배정  | 탄소중립 도시교통 인프라와 연결 가능             |

&nbsp;

### 📌 사업화 가능성

| 구분 | 사업 모델                 | 주요 고객                      | 수익 구조                         | 핵심 가치                    |
|------|--------------------------|-------------------------------|----------------------------------|-----------------------------|
| B2G  | 공공 주차장 자동화 시스템 | 지자체, 공공기관               | 시스템 납품 + 유지보수 계약       | 스마트시티 인프라 연계       |
| B2B  | 대형 시설 자율주차 솔루션 | 쇼핑몰, 물류센터, 아파트 단지 | 솔루션 판매 + 구독형 유지비       | 운영 효율화 + 고객 경험 개선 |
| B2C  | 개인용 스마트 주차 로봇   | 고급 EV 사용자, 스마트홈 고객 | 로봇 판매 + 앱 서비스 구독        | 개인화된 편의성과 자동화     |

&nbsp;

### ⚠️ 잘한 점 / 아쉬운 점

- **신호등 감지, 주차, 신호탐지를 활용한 네비게이션 등등 목표 기능들을 대부분 구현함.**

🧩 **한계 및 개선점**:
- SIFT 기반 특징점 추출 -> Yolo 기반 신호등, 표지판 인식
- SLAM 기반 내비게이션 기술 자동화

&nbsp;
