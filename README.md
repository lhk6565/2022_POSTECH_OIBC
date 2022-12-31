# 2022_POSTECH_OIBC

<p align='center'>
    <img src='poster.jfif' width='250' height='350'>
</p>

[2022 POSTECH OIBC CHALLENGE 태양광 발전량 예측 경진대회](https://o.solarkim.com/cmpt2022)에서 장려상 (7등 / 63팀)을 받은 Duck Cureve팀의 발표 자료입니다.

## 대회 소개
- 기술로 전력 시장을 개방하는 H Energy와 POSTECH 오픈이노베이션 빅데이터 센터(OIBC), 산업 인공지능 프로그램이 함께 미래 전력 시장을 이끌어갈 인재를 발굴, 지원하기 위해 대학 및 대학원생 대상으로 제4회 OIBC CHALLENGE를 주최
- 타 지역 태양광 발전소들의 발전량 데이터를 활용하여 신규 설치된 광명시 태양광 발전소의 다음 날 24시간 동안의 매시간 발전량 구간 예측

## 대회 미션
- "타 지역 태양광 발전소들의 발전량 데이터를 활용하여 신규 설치된 광명시 태양광 발전소의 다음날 24시간 동안의 매시간 발전량 구간 예측"

## 대회 규칙
1. 대회 기간 동안의 광명시 태양광 발전소의 시간 별 발전량을 전날 10시와 17시 각각 총 두 번 API를 통해 매일 입력
2. 예측된 발전량의 범위를 구간(상계값 및 하계값)으로 입력
3. 입력한 태양광 발전량 예측값은 변경할 수 있으며, 최종 입력된 값을 기준으로 평가
4. 전날 10시, 17시 예측된 발전량과 실제 발전량의 차이를 비교하여 평가
5. 구간 예측의 정확도는 실제 발전량이 구간 내에 포함되면서 예측 범위가 좁고 구간 평균이 실제 발전량과 가까울수록 정확도가 높은 것으로 판별
6. 평가 산식은 아래와 같음
$$\sum_d\sum_{h=1}^{24}\sum_{n\in{10,17}} \left( 0.45 \frac{\left\vert \frac{U_{d,h}^n+L_{d,h}^n}{2}-G_{d,h} \right\vert}{C} + 0.45 \frac{ \left( U_{d,h}^n-L_{d,h}^n \right)}{C} + 0.1 \frac{G_{d,h}I \left\{ L_{d,h} > G_{d,h} \;or\; U_{d,h} < G_{d,h} \right\}}{C} \right)$$
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
