# coding=gbk
# -*- coding:uft-8 -*-
# 教务系统模拟登陆

import requests
import re
import execjs


def collect():
    url = 'http://124.160.64.163/jwglxt/xtgl/login_slogin.html'
    headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'}
    res = requests.get(url=url, headers=headers)
    JSESSIONID = res.headers['Set-Cookie'].split(';')[0].split('=')[1]
    print(f'JSESSIONID: {JSESSIONID}')
    ex = 'name="csrftoken" value="(.*?)"'
    csrftoken = re.compile(ex).findall(res.text)[0]
    print(f'csrftoken: {csrftoken}')

    url = 'http://124.160.64.163/jwglxt/xtgl/login_logoutAccount.html'
    headers['Cookie'] = 'JSESSIONID=' + JSESSIONID
    requests.post(url=url, headers=headers)

    url = 'http://124.160.64.163/jwglxt/xtgl/login_getPublicKey.html'
    res = requests.get(url=url, headers=headers).json()
    modulus = res['modulus']
    exponent = res['exponent']
    print(f'modulus: {modulus}')
    print(f'exponent: {exponent}')
    ctx = execjs.compile(open('教务系统模拟登陆.js', encoding='utf-8').read())
    mm = ctx.call('encrypt', modulus, exponent, password)
    print(f'mm: {mm}')

    url = 'http://124.160.64.163/jwglxt/xtgl/login_slogin.html'
    data = {
        'csrftoken': csrftoken,
        'language': 'zh_CN',
        'yhm': username,
        'mm': mm
    }
    res = requests.post(url=url, headers=headers, data=data, allow_redirects=False)
    JSESSIONID = res.headers['Set-Cookie'].split('JSESSIONID=')[1].split(';')[0]
    print(f'JSESSIONID: {JSESSIONID}')


if __name__ == '__main__':
    username = '1610070111'
    password = '341278608d'
    collect()