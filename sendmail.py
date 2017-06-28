#!/usr/bin/env python3
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
import urllib.request as http
import requests


sender = 'changwen11@163.com'
receiver = 'changwen11@163.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'changwen11@163.com'
password = 'changwen1987'

msg = MIMEText('<html><h1>你好</h1> 有房源了 -> http://zzfws.bjjs.gov.cn/enroll/home.jsp</html>', 'html', 'utf-8')

msg['Subject'] = subject


def sending():
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


# content = http.urlopen('http://zzfws.bjjs.gov.cn/enroll/home.jsp').read()
# print(str(content))
# html = http.urlopen('http://zzfws.bjjs.gov.cn/enroll/home.jsp').read()
# print(str(html))
# if "img_dailog_enrollnone.jpg" in str(content):
#     print(str(content))

# post_param = {'action':'','start':'0','limit':'1'}
# return_data = requests.get('http://zzfws.bjjs.gov.cn/enroll/home.jsp',data =post_param, verify = False)
# print (return_data.text)


#### auto

from selenium import webdriver
from time import sleep

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(r'/home/tcs/Documents/chrome/chromedriver')
# 用get打开百度页面
driver.get('http://zzfws.bjjs.gov.cn/enroll/home.jsp')





