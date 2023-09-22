# coding=gbk
# -*- coding:uft-8 -*-
# 模拟登陆

import requests
import time

ts = int(time.time() * 1000)
url = f'https://zsfw.hainanu.edu.cn/f/ajax_get_csrfToken?ts={ts}'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '3',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Host': 'zsfw.hainanu.edu.cn',
    'Origin': 'https://zsfw.hainanu.edu.cn',
    'Referer': 'https://zsfw.hainanu.edu.cn/static/front/hainanu/basic/html_web/lqcx.html',
    'sec-ch-ua': '"Not;ABrand";v="99","GoogleChrome";v="91","Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.164Safari/537.36',
    'X-Requested-Time': str(ts),
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'n': '3'
}
res = requests.post(url=url, headers=headers, data=data).json()
token = res['data'].split(',')[1]
session = res['jessionid']
print(f'token: {token}')
print(f'session: {session}')

ts = int(time.time() * 1000)
url = f'https://zsfw.hainanu.edu.cn/servlet/validateCodeServlet?{ts}?ts={ts}'
headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': f'zhaosheng.hainanu.session.id={session}',
    'Host': 'zsfw.hainanu.edu.cn',
    'Referer': 'https://zsfw.hainanu.edu.cn/static/front/hainanu/basic/html_web/lqcx.html',
    'sec-ch-ua': '"Not;ABrand";v="99","GoogleChrome";v="91","Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.164Safari/537.36'
}
pict = requests.get(url=url, headers=headers).content
with open('code.jpg', 'wb') as f:
    f.write(pict)
print('Get code successfully!')

code = input('Please input code:').strip()
url = 'https://zsfw.hainanu.edu.cn/f/lqcx_jg'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '104',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': f'zhaosheng.hainanu.session.id={session}',
    'Host': 'zsfw.hainanu.edu.cn',
    'Origin': 'https://zsfw.hainanu.edu.cn',
    'Referer': 'https://zsfw.hainanu.edu.cn/static/front/hainanu/basic/html_web/lqcx.html',
    'sec-ch-ua': '"Not;ABrand";v="99","GoogleChrome";v="91","Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.164Safari/537.36'
}
data = {
    'Csrf-Token': token,
    'ksh': '21341226140177',
    'sfzh': '',
    'validateCode': code
}
page = requests.post(url=url, headers=headers, data=data).content.decode('utf-8')
with open('web.html', 'w', encoding='utf-8') as p:
    p.write(page)
print('Request html successfully!')