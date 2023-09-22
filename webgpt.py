# coding=utf-8

import os
import pytest
import time
import json
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 以下为启动Chrome，并打开调试端口、新建配置文件的命令行。按需修改和调用
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\Public\ChromeData"

# 打印日志
def log(str=""):
  print("[%s] %s" % (datetime.datetime.now(), str))

class ChatGPT(object):
  # 初始化，连接开了本地端口调试的Chrome浏览器
  def init(self, port):
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:%d" % port)
    log("尝试在端口 %d 上连接浏览器" % port)
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
    # 该对象在生命周期内已收回复数
    self.reply_cnt = 0
    # self.reply_cnt的备份。重新生成时会用到，便于回溯。
    self.reply_cnt_old = 0

  # 关闭
  def close(self):
    self.driver.quit()

  # 打开ChatGPT网页。
  # 参数：
  # 1.delay:等待网页加载的秒数
  # 2.refresh:设为True，则强制Chrome重新载入网页。但会频繁触发CloudFlare。
  #    设为False，则什么都不做。但需要事先将浏览器开好。我是将ChatGPT设成了首页
  def open(self, delay=3, refresh=False):
    self.reply_cnt = 0
    self.reply_cnt_old = 0
    log("打开ChatGPT网页中...")
    if refresh:
      self.driver.get("https://chat.openai.com")
    time.sleep(delay)
    log("完成")

  # 向ChatGPT发送文本。delay为每个步骤间延迟的秒数。
  def send(self, str="你好", delay=0.25):
    self.reply_cnt_old = self.reply_cnt
    # 点击文本框
    txtbox = self.driver.find_element(By.CSS_SELECTOR, ".m-0")
    txtbox.click()
    time.sleep(delay)
    # 输入文本，需处理换行
    log("发送内容:"+repr(str))
    txtlines = str.split('\n')
    for txt in txtlines:
      txtbox.send_keys(txt)
      time.sleep(delay)
      txtbox.send_keys(Keys.SHIFT, Keys.ENTER)
      time.sleep(delay)
    # 发送
    txtbox.send_keys(Keys.ENTER)
    time.sleep(delay)

  # 重新生成
  def regenerate(self):
    self.reply_cnt = self.reply_cnt_old
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

  # 获取最近一条回复。
  # timeout为超时秒数
  def getLastReply(self, timeout = 90):
    log("等待回复中...")
    time_cnt = 0
    reply_str = ""
    # 判断ChatGPT是否正忙
    while self.driver.find_elements(By.CSS_SELECTOR, ".result-streaming") != []:

      if time_cnt >= timeout:
        reply_str += "【超过时间阈值%d秒" % timeout
        elemList = self.getReplyList()
        if len(elemList) <= self.reply_cnt:
          reply_str += "，未收到任何有效回复】"
          return reply_str, False
        else:
          reply_str += "，以下是收到的部分回复】\n"
          break

      time.sleep(1)
      time_cnt = time_cnt + 1

    elemList = self.getReplyList()
    if len(elemList) <= self.reply_cnt:
      return "【发生不可描述错误，未收到任何有效回复】", False

    for i in range (self.reply_cnt, len(elemList)):
      reply_str += elemList[i].text
      reply_str += "\n"

    log(reply_str)
    self.reply_cnt = len(elemList)
    return reply_str, True

  # 获取ChatGPT回复列表
  def getReplyList(self):
    return self.driver.find_elements(By.CSS_SELECTOR, ".markdown > p")

if __name__=="__main__":
  chatgpt = ChatGPT()
  chatgpt.init(9222)
  chatgpt.open()
  while True:
    str = input("=====================\n请输入内容，Ctrl+Q重开，Ctrl+R重新生成，Ctrl+C退出\n>>> ")
    if str.find(chr(17)) > -1:
      chatgpt.open(refresh=True)
    elif str.find(chr(18)) > -1:
      chatgpt.regenerate()
    else:
      chatgpt.send(str=str)
    chatgpt.getLastReply()
