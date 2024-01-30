import time
from selenium.webdriver.common.by import By
from modules.login_validate import Source_code_length
from modules.login_validate import Location_prompt_information
from modules.login_validate import pop_ups

# 登录网页
def login_selenium_main(user, passwd, captcha, browser, config):
    # 找到账号框并输入账号
    browser.find_element(By.XPATH,config["username_data_xpath"]).send_keys(user)
    # 找到密码框并输入密码
    browser.find_element(By.XPATH,config["password_data_xpath"]).send_keys(passwd)
    # 找到验证码框并输入验证码
    browser.find_element(By.XPATH,config["captcha_data_xpath"]).send_keys(captcha)
    # 找到登陆按钮并点击
    browser.find_element(By.XPATH,config["button_xpath"]).click()


    print('user:',user)
    print('passwd:',passwd)

    # 登录成功跳转，有一定时间差
    time.sleep(4)
    '''
    目前已知的几种提示情况，可以根据实际情况添加验证代码:
    1.登录后通过alert弹窗的方式提示账密错误，此时可以先判断是否存在弹窗，如果存在的话则按下键盘的Enter键
    2.通过302跳转提示账密错误，这种情况还没想法
    3.直接在页面显示账密错误，这种情况可以判断返回包大小，也可以定位提示框
    '''
    return_text = Source_code_length(browser)
    # return_text = Location_prompt_information(browser)
    # return_text = pop_ups(browser)
    return_text = ""
    
    browser.quit()
    return return_text, user, passwd