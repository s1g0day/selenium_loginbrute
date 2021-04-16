'''

explain: 仅用作一次性的登录测试
author: s1g0day
time: 2021/04/14
version: '0.1'
'''

from selenium import webdriver
from PIL import Image
from aip import AipOcr
import time
import re


# 验证码的获取
def picture(url):
    browser.get(url)

    browser.save_screenshot('pic.png')
    code_element = browser.find_element_by_xpath('//*[@id="ImageCheck"]')
    # print("验证码的坐标为：", code_element.location)
    # print("验证码的大小为：", code_element.size)
    left = code_element.location['x']#x点的坐标
    top = code_element.location['y']#y点的坐标
    right = code_element.size['width']+left#上面右边点的坐标
    height = code_element.size['height']+top#下面右边点的坐标
    image = Image.open('pic.png')
    code_image = image.crop((left, top, right, height))
    code_image.save('captcha.png')#截取的验证码图片保存为新的文件

# 验证码的获取和处理
def get_captcha(url):
    # 获取验证码图片
    browser.get(url)
    png = browser.find_element_by_id('ImageCheck')
    png.screenshot('capt.png')  # 将图片截屏并保存
    # 处理验证码
    img = Image.open('capt.png')

    img = img.convert('L')  # P模式转换为L模式(灰度模式默认阈值127)
    count = 160  # 设定阈值
    table = []
    for i in range(256):
        if i < count:
            table.append(0)
        else:
            table.append(1)

    img = img.point(table, '1')
    img.save('captcha.png')  # 保存处理后的验证码
    

# 验证码的识别
def discern_captcha():
    # 识别码
    APP_ID = 'xxx'                                      #这是你产品服务的appid
    API_KEY = 'xxx'                #这是你产品服务的appkey
    SECRET_KEY = 'xxx'     #这是你产品服务的secretkey
    # 初始化对象
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 读取图片
    def get_file_content(file_path):
        with open(file_path, 'rb') as f:
            return f.read()

    image = get_file_content('captcha.png')
    # 定义参数变量
    options = {'language_type': 'ENG', }  # 识别语言类型，默认为'CHN_ENG'中英文混合
    #  调用通用文字识别
    result = client.basicGeneral(image, options)  # 高精度接口 basicAccurate
    
    for word in result['words_result']:
        captcha = (word['words'])
        
       # print('识别结果：', captcha)

        return captcha


# 登录网页
def login(captcha):
    browser.find_element_by_id('txtLoginName').send_keys('***')  # 找到账号框并输入账号
    browser.find_element_by_id('txtLoginPass').send_keys('***')  # 找到密码框并输入密码
    browser.find_element_by_id('txtVerifyCode').send_keys(captcha)  # 找到验证码框并输入验证码
    browser.find_element_by_id('btnLogin').click()  # 找到登陆按钮并点击
   
    # 登录成功跳转，有一定时间差
    time.sleep(2)
    # 获取alert对话框
    alert = browser.switch_to.alert.text
    print('------------获取警告对话框的内容------------')
    print (alert)  # 打印警告对话框内容
    # 如果登录后302弹窗，则开启自动按下键盘的 ENTER 键
    win32api.keybd_event(13, 0, 0, 0)
    
    print('程序退出')
    browser.quit()

# 点击刷新验证码
def get_file():
    browser.find_element_by_xpath('//*[@id="ImageCheck"]').click()  # 找到验证码按钮并点击

# 主函数
if __name__ == '__main__':
    
    options = webdriver.ChromeOptions()
    options.add_argument('--save-page-as-mhtml')
    browser = webdriver.Chrome(options=options)
   # chrome 全屏
   # browser.maximize_window() 
    browser.implicitly_wait(10)
    url = 'http://xxx.com/Login.php'
    time.sleep(1)
    
    #对图片做处理的函数
    #get_captcha(url)
    
    print('------------开始获取二维码图片------------')
    picture(url)
    print('------------开始识别二维码------------')
    captcha = re.findall("\d+",discern_captcha())[0]
    captcha.replace(" ", "")
    print('识别结果：', captcha)
    print('------------开始登录测试------------')
    login(captcha)