# coding=gbk
# -*- coding:uft-8 -*-
# 考研星球

import requests
import pandas as pd


def collect():
    resLs = []
    url = 'https://zxjk.jkkaoyan.com//index.php/api/study.school/lists?is_hot=0&province_id=0&screen_list=%5B%5D&is_advanced=0&token=&app_id=10001'
    headers = {'User-Agent': ua}
    res = requests.get(url=url, headers=headers).json()
    for li in res['data']:
        schoolId = li['school_id']
        url = f'https://zxjk.jkkaoyan.com//index.php/api//study.school/detail?school_id={schoolId}&token=&app_id=10001'
        res = requests.get(url=url, headers=headers).json()
        dic = {
            'ID': schoolId,
            '名称': res['data']['name'],
            '介绍': res['data']['intro'],
            'logo': res['data']['logo']
        }
        for item in res['data']['custom_field']:
            item = res['data']['custom_field'][item]
            dic[item['name']] = item['image'] if item['image_id'] else item['content']
        try:
            dic['省份'] = res['data']['region']['province']
            dic['城市'] = res['data']['region']['city']
        except:
            dic['省份'] = ''
            dic['城市'] = ''
        print(dic)
        resLs.append(dic)
    df = pd.DataFrame(resLs)
    df.to_excel('./考研星球.xlsx', encoding='utf-8', index=False)


if __name__ == '__main__':
    ua = 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    collect()