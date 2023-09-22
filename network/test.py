import requests
import re
import json
from lxml import etree
import pandas as pd

# 设置请求头，包括 Cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Cookie': 'srftoken=p2nGcExA1h6cDnxrbFUJarOEMqUXgMvr; sessionid=fe917783ec656d43f65cdf868c6ba1f9; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjEyMTE4MzUxMDIiLCJncm91cHMiOlsyMl0sImlhdCI6MTY5NTM2ODM1NCwiZXhwIjoxNjk1NDU0NzU0fQ.v5cqEp7ZNZfQUIDH-BMVsRg7uEptySACcwLw-eWwhkM; webvpn_username=21211835102%7C1695368354%7C6b8c471d70d3c05ead7e671a5ee6701f71282a20'
}

if __name__ == '__main__':
    # 请求目标网页
    url = 'https://10-132-246-246.webvpn.wzu.edu.cn/courseuser/course/114/userlist/'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html_text=res.text
    tree = etree.HTML(html_text)

    result = []

    # 假设每个表格行都是一个学生的信息
    for row in tree.xpath('//table[@class="table table-hover"]/tbody/tr'):
        student = {
            "rank": row.xpath('./td[1]/text()')[0],
            "username": row.xpath('./td[2]/a/text()')[0],
            "name": row.xpath('./td[3]/text()')[0],
            "class": row.xpath('./td[4]/a/text()')[0],
            "solved_problems": row.xpath('./td[5]/a/font/text()')[0],
            "status": row.xpath('./td[6]/a/text()')[0],
            "correct_rate": row.xpath('./td[7]/text()')[0],
            "line_of_code": row.xpath('./td[8]/text()')[0],
        }
        result.append(student)

    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

'''
https://source-443.webvpn.wzu.edu.cn/login?service=https:%2F%2Fwebvpn.wzu.edu.cn%2Fusers%2Fauth%2Fcas%2Fcallback%3Furl

https://10-132-246-246.webvpn.wzu.edu.cn/accounts/login/?next=/courseuser/course/114/userlist/

csrftoken=p2nGcExA1h6cDnxrbFUJarOEMqUXgMvr; sessionid=fe917783ec656d43f65cdf868c6ba1f9; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjEyMTE4MzUxMDIiLCJncm91cHMiOlsyMl0sImlhdCI6MTY5NTM2ODM1NCwiZXhwIjoxNjk1NDU0NzU0fQ.v5cqEp7ZNZfQUIDH-BMVsRg7uEptySACcwLw-eWwhkM; webvpn_username=21211835102%7C1695368354%7C6b8c471d70d3c05ead7e671a5ee6701f71282a20


'''