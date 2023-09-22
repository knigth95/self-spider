# coding=gbk
# -*- coding:uft-8 -*-
# CAS模拟登陆

import requests
import re


def collect():
    url = 'http://iids.sdyu.edu.cn/cas/login?service=http%3A%2F%2Flxl.sdyu.edu.cn%2Fcas%2Findex.php%3Fcallback%3Dhttps%3A%2F%2Flxl.sdyu.edu.cn%2Fhome%2Fweb%2Fseat%2Farea%2F1'
    headers = {
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    cookie2 = res.headers['Set-Cookie']
    print(cookie2)
    JSESSIONID1 = requests.utils.dict_from_cookiejar(res.cookies)['JSESSIONID']

    ex = '<input class="for-form" type="hidden" name="lt" value="(.*?)">'
    pa = re.compile(ex)
    lt = pa.findall(res.text)[0]
    print(lt)
    ex = '<input class="for-form"type="hidden" name="execution" value="(.*?)">'
    pa = re.compile(ex)
    execution = pa.findall(res.text)[0]
    print(execution)
    url = 'http://iids.sdyu.edu.cn/cas/login'
    headers = {
        'cookie': cookie2,
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    data = {
        'username': '',
        'password': '',
        '_eventId': 'submit',
        'lt': lt,
        'source': 'cas',
        'execution': execution
    }
    res = requests.post(url=url, headers=headers, data=data, allow_redirects=False)
    print(requests.utils.dict_from_cookiejar(res.cookies))
    cookie1 = res.headers['Set-Cookie']
    CASTGC = requests.utils.dict_from_cookiejar(res.cookies)['CASTGC']

    url = res.headers['Location']
    headers = {
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    cookie3 = res.headers['Set-Cookie']
    TENANT_TICKET = requests.utils.dict_from_cookiejar(res.cookies)['TENANT_TICKET']
    JSESSIONID = requests.utils.dict_from_cookiejar(res.cookies)['JSESSIONID']
    print(cookie3)

    url = res.headers['Location']
    headers = {
        'cookie': cookie3,
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    cookie = res.headers['Set-Cookie']
    print(cookie)

    url = res.headers['Location']
    print(url)
    headers = {
        'cookie': cookie1.split(';')[-2].split()[-1] + '; ' + cookie2.split(';')[0],
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    print(headers)
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    print(res.headers['Set-Cookie'])

    url = res.headers['Location']
    headers = {
        'cookie': cookie3,
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    print(headers)
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    CAS_TICKET = requests.utils.dict_from_cookiejar(res.cookies)['CAS_TICKET']
    LOGIN_TOKEN = requests.utils.dict_from_cookiejar(res.cookies)['LOGIN_TOKEN']

    cookie = f'JSESSIONID={JSESSIONID}; TENANT_TICKET={TENANT_TICKET}; LOGIN_TOKEN={LOGIN_TOKEN}'
    url = res.headers['Location']
    headers = {
        'cookie': cookie,
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    print(cookie)
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    print(res.headers['Location'])

    cookie = f'CASTGC={CASTGC}; JSESSIONID={JSESSIONID1}; CAS_TICKET={CAS_TICKET}'
    url = res.headers['Location']
    headers = {
        'cookie': cookie,
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    print(cookie)
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    print(res.headers['Location'])

    url = res.headers['Location']
    headers = {
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    print(res.headers['Location'])
    print(res.headers['Set-Cookie'])

    cookie = res.headers['Set-Cookie'].split(', ')[-1].split(';')[0]
    url = res.headers['Location']
    headers = {
        'cookie': cookie,
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    print(headers)
    print(res.headers['Location'])

    url = 'http://lxl.sdyu.edu.cn' + res.headers['Location']
    headers = {
        'cookie': cookie,
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    print(res.status_code)
    print(res.headers['Set-Cookie'])


if __name__ == '__main__':
    collect()