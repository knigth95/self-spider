# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

# 打开文件进行读取
with open('que.txt', 'r', encoding='utf-8') as file:
    file_contents = file.read()

# 创建Beautiful Soup对象来解析文本
soup = BeautifulSoup(file_contents, 'html.parser')

# 使用类名选择器查找所有问题块
question_blocks = soup.find_all("div", class_='questionItem___q6Hgu')

# 创建一个新的文本文件来存储问题和答案
with open('answer.txt', 'w', encoding='utf-8') as output_file:
    for question_block in question_blocks:
        # 提取问题文本
        question_text = question_block.text.strip()
        output_file.write("问题: {}\n".format(question_text))
        
        # 提取答案选项文本
        answer_elements = question_block.select('label.ant-radio-wrapper')
        for answer_element in answer_elements:
            option = answer_element.select('span.font16')[0].text.strip()
            text = answer_element.select('div.renderHtml___UerV1')[0].text.strip()
        
        # 写入空行来分隔不同的问题
        output_file.write("\n")
