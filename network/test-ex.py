import requests
import re
import json
from lxml import etree
import pandas as pd

# 设置请求头，包括 Cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Cookie': 'csrftoken=p2nGcExA1h6cDnxrbFUJarOEMqUXgMvr; sessionid=fe917783ec656d43f65cdf868c6ba1f9; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjEyMTE4MzUxMDIiLCJncm91cHMiOlsyMl0sImlhdCI6MTY5NTM4MTYzMywiZXhwIjoxNjk1NDY4MDMzfQ.xqHziZ2Ks1zN7El8xtRN1cjRyuRDFMwnCA8cdWZScXk; webvpn_username=21211835102%7C1695381633%7Cb2cc51842a5409a20279a9438bc5451683f35bb8'
}

def getPosition(url,filename):
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html_text=res.text
    tree = etree.HTML(html_text)

    result = []

    # 假设每个表格行都是一个学生的信息
    for row in tree.xpath('//table[@class="table table-hover"]/tbody/tr'):
        student = {
            "排名": row.xpath('./td[1]/text()')[0],
            "用户名": row.xpath('./td[2]/a/text()')[0],
            "姓名": row.xpath('./td[3]/text()')[0],
            "班级": row.xpath('./td[4]/a/text()')[0],
            "解题": row.xpath('./td[5]/a/font/text()')[0],
            "状态": row.xpath('./td[6]/a/text()')[0],
            "正确率": row.xpath('./td[7]/text()')[0],
            "代码行": row.xpath('./td[8]/text()')[0],
        }
        result.append(student)
        with open(filename+'.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        
    
        

if __name__ == '__main__':
    # 请求目标网页
    url = [
    'https://10-132-246-246.webvpn.wzu.edu.cn/courseuser/course/114/userlist/',
    'https://10-132-246-246.webvpn.wzu.edu.cn/courseuser/course/114/userlist/?grade=608',
    'https://10-132-246-246.webvpn.wzu.edu.cn/courseuser/course/114/userlist/?grade=609'
    ]
    filename=['总排名','23网工1','23网工2']
    for i in range(len(filename)):
        
        getPosition(url[i], filename[i])

    