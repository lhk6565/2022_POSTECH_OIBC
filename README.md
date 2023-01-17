# 2022_POSTECH_OIBC

<p align='center'>
    <img src='poster.jfif' width='250' height='350'>
</p>

[2022 POSTECH OIBC CHALLENGE 태양광 발전량 예측 경진대회](https://o.solarkim.com/cmpt2022)에서 장려상:trophy: (7등 / 63팀)을 받은 Duck Cureve팀의 발표 자료입니다.
- 이형권 (IT경영) ![:github:](https://github.com/lhk6565)
- 김태연 (IT경영)
- 장성호 (산업경영) ![:github:](https://github.com/Jjineeq)
- 김현진 (에너지전기공학)

## 대회 소개
- 기술로 전력 시장을 개방하는 H Energy와 POSTECH 오픈이노베이션 빅데이터 센터(OIBC), 산업 인공지능 프로그램이 함께 미래 전력 시장을 이끌어갈 인재를 발굴, 지원하기 위해 대학 및 대학원생 대상으로 제4회 OIBC CHALLENGE를 주최
- 타 지역 태양광 발전소들의 발전량 데이터를 활용하여 신규 설치된 광명시 태양광 발전소의 다음 날 24시간 동안의 매시간 발전량 구간 예측

## 대회 기간
- 2022년 10월 24일 ~ 2022년 11월 12일: 사전 대회 기간
- 2022년 11월 14일 ~ 2022년 11월 18일: 경진 대회 기간
- 2022년 12월 01일: 발표 평가
- 2022년 12월 02일: 결과 발표

## 대회 미션
- "타 지역 태양광 발전소들의 발전량 데이터를 활용하여 신규 설치된 광명시 태양광 발전소의 다음날 24시간 동안의 매시간 발전량 구간 예측"

## 대회 규칙
1. 대회 기간 동안의 광명시 태양광 발전소의 시간 별 발전량을 전날 10시와 17시 각각 총 두 번 API를 통해 매일 입력
2. 예측된 발전량의 범위를 구간(상계값 및 하계값)으로 입력
3. 입력한 태양광 발전량 예측값은 변경할 수 있으며, 최종 입력된 값을 기준으로 평가
4. 전날 10시, 17시 예측된 발전량과 실제 발전량의 차이를 비교하여 평가
5. 구간 예측의 정확도는 실제 발전량이 구간 내에 포함되면서 예측 범위가 좁고 구간 평균이 실제 발전량과 가까울수록 정확도가 높은 것으로 판별
6. 평가 산식은 아래와 같음
$$\sum_d\sum_{h=1}^{24}\sum_{n\in{10,17}} \left( 0.45 \frac{\left\vert \frac{U_{d,h}^n+L_{d,h}^n}{2}-G_{d,h} \right\vert}{C} + 0.45 \frac{ \left( U_{d,h}^n-L_{d,h}^n \right)}{C} + 0.1 \frac{G_{d,h}I \left\lbrace L_{d,h} > G_{d,h}\ or\ U_{d,h} < G_{d,h} \right\rbrace}{C} \right)$$
$C$ : 태양광 발전소 용량 (MW) <br>
$G_{d,h}$ : 발전소 d일의 h 시간대 실제 발전량 <br>
$L_{d,h}^n$ : 전날 n시에 입력한 d일의 h 시간대 발전량 예측 구간의 하계 (Lower Bound) 값 <br>
$U_{d,h}^n$ : 전날 n시에 입력한 d일의 h 시간대 발전량 예측 구간의 상계 (Upper Bound) 값 $\left( U_{d,h}^n > L_{d,h}^n \right)$ <br>
$I\left\lbrace A \right\rbrace$ : A가 참이면 1, 거짓이면 0인 지시함수 (Indicator Function)

## 제안 방법
- 다변량 모델과 시계열 모델을 hybrid 하여 $y^{''} = f(y^{'}t)$를 사용하여 문제를 해결하고자 제안
- 자세한 내용은 [발표 자료](Duck_Curve_한국공학대학교.pdf) 참고 바람

## 코드 실행
- `Process` 폴더 내 필요한 `.ipynb` 파일을 실행하면 됩니다. `Data Processing.ipynb` 파일은 api로 가져온 데이터를 전처리 하기 위한 파일이며 해당 부분은 대회 종료 후 코드를 삭제하여 일부분만 정리되어 있습니다.
- 디렉토리 구성 :
~~~
    - Data Processing.ipynb         # 데이터 전처리
    - EDA.ipynb                     # EDA 및 시각화
    - ML.ipynb                      # 모델링
    - api_sample.py                 # 데이터 취득 및 입찰 API
    - functions.py                  # 사용자 정의 모듈
~~~

## 느낀점
이번 대회에서 사전 참여 기간을 통해 모델을 만들고 error값을 확인해 봤어야 했는데 이 기간을 활용 못 하고 대회 전날 부터 밤을 새워 전처리 부터 모델링까지 해야 했어서 매우 아쉽다.(이래서 1~2일차에 error값이 높게 나왔다...)<br>
Boosting 계열 ML모델에 Moving Average를 결합하니 생각지도 못하게 오차가 줄어 들었고, Physics 모델과도 hybrid를 할 수 있으면 좀 더 정확한 예측이 가능하지 않을까 싶다.<br>
전처리 과정에서 시공간(Spatio-Temporal)을 활용하여 기후 유사도를 Clustering 한다면 좀 더 유의미한 결과를 얻을 수 있지 않았을까? 이에 대해서는 이번에 알게된 Spatio-Temporal Analysis에 대한 공부가 좀 필요할 것 같다.<br>
경진대회 진행하면서 계속 정확도를 높이려고 하루도 빠짐 없이 밤을 새웠는데 세상에 강자는 많다고 다른 팀들도 열심히 참여하는 것이 보였다. 매년 주제가 조금씩 바뀌는 것 같지만 2023년에도 OIBC CHALLENGE가 열린다면 한번 더 도전해 볼 것이다.

## 문의
코드 및 발표자료에 대해 궁금한 점이 있으실 경우 lhk6565@naver.com으로 문의해주시면 답변드리겠습니다.:blush:<br>
데이터에 대한 저작권은 대회 주관사인 [POSTECH 오픈이노베이션 빅데이터센터 (OIBC)](http://oibc.postech.ac.kr/)에 있으므로 해당 주관사로 문의 부탁드립니다.