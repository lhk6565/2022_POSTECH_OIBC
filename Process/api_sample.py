# 본 코드는 python 3.10에서 테스트 되었습니다.

import requests
import json
_API_URL = 'https://research-api.dershare.xyz'
_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJNZHNVVlNnbmhZb3h2NnllNWFoNGRaIiwiaWF0IjoxNjY4MDA2MzE1LCJleHAiOjE2Njg3ODM2MDAsInR5cGUiOiJhcGlfa2V5In0.WJr-F8Oc9xIGcjdmeOD_CdP7CA1av91ZQNXpSWeJCIg'  # https://o.solarkim.com/cmpt2022/result에서 확인할 수 있다.
_AUTH_PARAM = {'headers': {'Authorization': f'Bearer {_API_KEY}'}}


def _get(url: str):
    '''
    주어진 url의 리소스를 조회한다.

    Args:
        url (str): API url
    '''
    response = requests.get(url, **_AUTH_PARAM)
    return response.json()


def _post(url: str, data: dict|list):
    '''
    리소스 생성 데이터를 이용해서 주어진 url의 리소스를 생성한다.

    Args:
        url (str): API url
        data (dict): 리소스 생성용 데이터
    '''
    response = requests.post(url, data=json.dumps(data), **_AUTH_PARAM)
    return response.json()


def _get_pv_sites():
    '''
    태양광 발전소 목록 조회. (https://research-api.dershare.xyz/docs#operation/_get_open_proc_cmpt_pv_sites_get 참고)
    '''
    pv_sites = _get(f'{_API_URL}/open-proc/cmpt-2022/pv-sites')
    print(pv_sites)
    return pv_sites


def _get_pv_gens(mm, dd):
    '''
    태양광 발전소별 발전량 조회. 주어진 날짜의 전체 발전소별 발전량을 가져온다. (https://research-api.dershare.xyz/docs#operation/_get_open_proc_cmpt_pv_gens__date__get 참고)
    '''
    date = '2022-'+mm+'-'+dd
    pv_gens = _get(f'{_API_URL}/open-proc/cmpt-2022/pv-gens/{date}')
    print(pv_gens)
    return pv_gens

def _get_weathers(num, mm, dd):
    '''
    기상 관측 정보 조회. 주어진 날짜의 3가지 기상데이터별로 별도로 조회해야 하며, 종관기상관측 데이터도 별도로 조회가능한다.
    '''
    date = '2022-'+mm+'-'+dd

    # 기상정보 1 관측데이터 조회 (https://research-api.dershare.xyz/docs#operation/_get_open_proc_cmpt_weathers_1_observeds__date__get 참고)
    if num == 1:
        weathers_1 = _get(f'{_API_URL}/open-proc/cmpt-2022/weathers/1/observeds/{date}')
        print(len(weathers_1))
        return weathers_1

    # 기상정보 2 관측데이터 조회 (https://research-api.dershare.xyz/docs#operation/_get_open_proc_cmpt_weathers_2_observeds__date__get 참고)
    if num == 2:
        weathers_2 = _get(f'{_API_URL}/open-proc/cmpt-2022/weathers/2/observeds/{date}')
        print(len(weathers_2))
        return weathers_2

    # 기상정보 3 관측데이터 조회 (https://research-api.dershare.xyz/docs#operation/_get_open_proc_cmpt_weathers_3_observeds__date__get 참고)
    if num == 3:
        weathers_3 = _get(f'{_API_URL}/open-proc/cmpt-2022/weathers/3/observeds/{date}')
        print(len(weathers_3))
        return weathers_3


def _get_weather_forecasts(num, id, hr, mm, dd):
    '''
    기상 예측 정보 조회. 주어진 날짜의 특정 시간대에 예측된 기상 예측 정보를 조회할 수 있다. 3가지 기상데이터별로 별도로 조회해야 한다.
    '''
    wth1_id = id
    wth2_id = id
    wth3_id = id
    date = '2022-'+mm+'-'+dd
    hour = hr

    # 기상정보 1 예측데이터 조회 (https://research-api.dershare.xyz/docs#operation/_get_open_proc_cmpt_weathers_1__id__forecasts__date___hour__get 참고)
    if num == 1:
        forecasts_1 = _get(f'{_API_URL}/open-proc/cmpt-2022/weathers/1/{wth1_id}/forecasts/{date}/{hour}')
        print(len(forecasts_1))
        return forecasts_1

    # 기상정보 2 예측데이터 조회 (https://research-api.dershare.xyz/docs#operation/_get_open_proc_cmpt_weathers_2__id__forecasts__date___hour__get 참고)
    if num == 2:
        forecasts_2 = _get(f'{_API_URL}/open-proc/cmpt-2022/weathers/2/{wth2_id}/forecasts/{date}/{hour}')
        print(len(forecasts_2))
        return forecasts_2

    # 기상정보 3 예측데이터 조회 (https://research-api.dershare.xyz/docs#operation/_get_open_proc_cmpt_weathers_3__id__forecasts__date___hour__get 참고)
    if num == 3:
        forecasts_3 = _get(f'{_API_URL}/open-proc/cmpt-2022/weathers/3/{wth3_id}/forecasts/{date}/{hour}')
        print(len(forecasts_3))
        return forecasts_3


def _get_environments(mm, dd):
    '''
    광명발전소의 센서 데이터 조회. 주어진 날짜의 특정 시간대에 측정된 센서 데이터를 조회할 수 있다.
    '''
    date = '2022-'+mm+'-'+dd
    environments = _get(f'{_API_URL}/open-proc/cmpt-2022/evironments/{date}')
    print(environments)
    return environments

def _post_bids():
    '''
    집합 자원 태양광 발전량 입찰. 시간별 24개의 발전량을 입찰하며 API가 호출된 시간에 따라 입찰 대상일이 결정된다. (https://research-api.dershare.xyz/docs#operation/_post_open_proc_cmpt_bids_post 참고)
    '''
    amounts = [{'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0}, #7
    {'upper': 9.48, 'lower': 9.48}, #8
    {'upper': 46.52, 'lower': 46.52}, #9
    {'upper': 116.9, 'lower': 116.9}, #10
    {'upper': 172.58, 'lower': 172.58}, #11
    {'upper': 226.99, 'lower': 226.99}, #12
    {'upper': 245.59, 'lower': 245.59}, #1
    {'upper': 211.3, 'lower': 211.3}, #2
    {'upper': 181.29, 'lower': 181.29}, #3
    {'upper': 132.29, 'lower': 132.29}, #4
    {'upper': 28.83, 'lower': 28.83}, #5
    {'upper': 2.32, 'lower': 2.32}, #6
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0},
    {'upper': 0, 'lower': 0}]
    success = _post(f'{_API_URL}/open-proc/cmpt-2022/bids', amounts)
    print(success)


def _run():
    _get_pv_sites()
    _get_pv_gens()
    _get_weathers()
    _get_weather_forecasts()
    _get_environments()
    _post_bids()


if __name__ == '__main__':
    _run()
