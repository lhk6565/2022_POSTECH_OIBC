'''OIBC 입찰평가 샘플코드.

>>> python eval_bid_sample.py

- 거래일 전날 10시와 17시, 2회에 걸쳐 거래일의 발전량 예측치를 제출
- 값이 작을수록 우수한 것으로 평가
- 예측 구간의 평균값을 기준으로 한 예측 오차, 예측 구간의 범위, 실제 발전량이 예측 구간에 포함 여부를 평가 산식에 반영
'''
from typing import List

TOTAL_CAPACITY = 472.39
ONE_HOUR_SEC = 3600
BID_ROUNDS = (1, 2)


def get_bids(bid_round: int):
    '''It returns bids of a round.'''
    # yapf: disable
    if bid_round == 1:
        return [{'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 7.245, 'lower':	6.555 },
                {'upper': 7.455, 'lower':	6.745 },
                {'upper': 189, 'lower':	171 },
                {'upper': 211.68, 'lower':	191.55 },
                {'upper': 116.119, 'lower':	105.061 },
                {'upper': 107.835, 'lower':	97.565 },
                {'upper': 82.583, 'lower':	74.719 },
                {'upper': 80.745, 'lower':	73.055 },
                {'upper': 29.82, 'lower':	26.98 },
                {'upper': 28.35, 'lower':	25.65 },
                {'upper': 8.715, 'lower':	7.885 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },]
    if bid_round == 2:
        return [{'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 6.9, 'lower':	6.9 },
                {'upper': 7.19, 'lower':	7.19 },
                {'upper': 180, 'lower':	180 },
                {'upper': 201.6, 'lower':	201.6 },
                {'upper': 110.59, 'lower':	110.59 },
                {'upper': 102.7, 'lower':	102.7 },
                {'upper': 78.65, 'lower':	78.65 },
                {'upper': 76.9, 'lower':	76.9 },
                {'upper': 28.4, 'lower':	28.4 },
                {'upper': 27, 'lower':	27 },
                {'upper': 8.3, 'lower':	8.3 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },
                {'upper': 0, 'lower':	0 },]
    return [{'upper': 0, 'lower': 0}]*24 
    # yapf: enable


def get_gens() -> List[float]:
    '''It returns pv power generations of a group.'''
    # yapf: disable
    return [0, 0, 0, 0, 0, 0, 0, 8.2, 25.1, 50.1, 124.7, 184.4, 
        294.9, 293.3, 221.8, 144.9, 41.5, 3.8, 0, 0, 0, 0, 0, 0]
    # yapf: enable


if __name__ == '__main__':
    gens = get_gens()
    sum_value: float = 0
    for idx, gen in enumerate(gens):
        util_errs = []
        for bid_round in BID_ROUNDS:
            bids = get_bids(bid_round)
            bid = bids[idx]
            real_gen = gens[idx]

            value = (
                (
                    0.45
                    * abs((bid['upper'] + bid['lower']) / 2 - real_gen)
                    / TOTAL_CAPACITY
                )
                + (0.45 * (bid['upper'] - bid['lower']) / (TOTAL_CAPACITY))
                + (
                    (
                        0.1
                        * (
                            real_gen
                            * (
                                1
                                if bid['lower'] > real_gen
                                or bid['upper'] < real_gen
                                else 0
                            )
                        )
                    )
                    / TOTAL_CAPACITY
                )
            )

            print(
                f'Idx({idx}), Round({bid_round}) | '
                f'Evaluation value: {value} (%) / '
                f'Bid: {bid} (kWh) / '
                f'Gen: {gen} (kWh)'
            )
            sum_value += value

    print(f'Total Evaluation value: {sum_value} (KRW)')
