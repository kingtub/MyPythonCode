import requests
import json
r'''获取优你学投首页前3个接口'''
# Base URL being accessed
url = 'http://120.79.84.67/api/'
# 登录接口
loginUrl = 'login/'
headers = {'Content-Type': 'application/json'}
# 首页学习
STUDY_LIST = "study/subject/list"
# 首页banner
BANNER_LIST = "sys/banner-list"


def login():
    params = {'loginName': '15889681345', 'password': 'aa123456'}
    resp = requests.post(url + loginUrl, data=json.dumps(params), headers=headers)
    # Decoded text returned by the request
    text = resp.text
    print(text)
    return json.loads(text)['data']['token']


def get_study_list(t):
    params = {'token': t}
    resp = requests.get(url + STUDY_LIST, params=params, headers=headers)
    text = resp.text
    print(text)


def get_banner_list(t):
    params = {'token': t, 'module': 'study'}
    resp = requests.get(url + BANNER_LIST, params=params, headers=headers)
    text = resp.text
    print(text)


token = login()
print('token=', token)
get_study_list(token)
get_banner_list(token)


