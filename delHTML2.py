# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup

# 打开HTML文件进行读取
with open('que.txt', 'r', encoding='utf-8') as file:
    file_contents = file.read()

# 创建Beautiful Soup对象来解析文本
soup = BeautifulSoup(file_contents, 'html.parser')

# 使用类名选择器查找所有问题块
question_blocks = soup.find_all("div", class_='questionItem___q6Hgu')

# 创建一个新的文本文件来存储问题、答案和图片链接
with open('result.txt', 'w', encoding='utf-8') as output_file:
    for question_block in question_blocks:
        # 提取问题文本
        question_text = question_block.text.strip()
        output_file.write("问题: {}\n".format(question_text))
        
        # 提取答案选项文本
        answer_elements = question_block.select('label.ant-radio-wrapper')
        for answer_element in answer_elements:
            option = answer_element.select('span.font16')[0].text.strip()
            text = answer_element.select('div.renderHtml___UerV1')[0].text.strip()
            output_file.write("选项: {}\n答案: {}\n".format(option, text))

        # 提取图片链接
        image_elements = question_block.select('img')
        for i, image_element in enumerate(image_elements):
            image_url = image_element['src']
            # 下载图片并保存到本地文件夹
            response = requests.get(image_url)
            if response.status_code == 200:
                image_filename = 'image_{}.png'.format(i)
                with open(image_filename, 'wb') as image_file:
                    image_file.write(response.content)
                output_file.write("图片链接: {}\n".format(image_url))
                output_file.write("图片文件: {}\n".format(image_filename))
        
        # 写入空行来分隔不同的问题
        output_file.write("\n")
