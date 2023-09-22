# coding=gbk
# -*- coding:uft-8 -*-
# 豆瓣TOP250

import requests  # 导入第三方库
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


def collect(p):  # 采集函数
    url = f'https://movie.douban.com/top250?start={p}&filter='
    headers = {  # 设置请求头
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.106Safari/537.36'
    }
    page = requests.get(url=url, headers=headers).content.decode('utf-8')  # 采集页面数据
    soup = BeautifulSoup(page, 'html.parser')  # 实例化soup
    ls = soup.find_all('div', class_='item')
    for li in ls:
        dic = {  # 将数据用bs4解析为字典
            '排名': eval(li.select('.pic > em')[0].string),
            '名称': li.select('.info > .hd > a > .title')[0].string,
            '评分': eval(li.select('.info > .bd > .star > .rating_num')[0].string)
        }
        print(dic)
        resLs.append(dic)  # 将字典加入列表


def main():  # 主函数
    for i in range(10):
        collect(i * 25)  # 抓取数据
        sleep(0.2)
    df = pd.DataFrame(resLs)  # 转列表为dataframe
    path = pd.ExcelWriter('豆瓣TOP250.xlsx')
    df.to_excel(path, encoding='utf-8', index=False)
    path.save()  # 保存数据


def draw():  # 绘制折线图
    nameLs = [i['名称'] for i in resLs[:10]]  # 提取名称
    commentLs = [i['评分'] for i in resLs[:10]]  # 提取评分
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
    plt.figure(figsize=(10, 10))  # 设置画布大小
    plt.xticks(rotation='-45', fontsize=9)
    plt.plot(nameLs, commentLs, color='blue', markersize=10, marker='o', linestyle='--')  # 绘图
    plt.xlabel('名称')
    plt.ylabel('评分')
    plt.title('名称评分折线图')
    plt.savefig('豆瓣TOP250.png')  # 保存图片
    print('绘图完成!')
    plt.show()
    plt.clf()


if __name__ == '__main__':
    resLs = []  # 初始化列表
    main()  # 执行主函数
    draw()  # 绘图