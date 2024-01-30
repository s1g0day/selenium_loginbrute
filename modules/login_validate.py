'''
验证登录的几种方式
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# demo
# def demo():
#    # 只说明主要代码
#     if "ss" == "ss":
#         print("验证码不正确")
#         return "验证码不正确"
#     elif "ss" == "ss":
#         print("登录失败")
#         return "登录失败"
#     else:
#         print("登录异常")
#         return "登录异常"

# 
def res_json(data):
   
   # 只说明主要代码
    if "验证码错误" in data:
        print("验证码不正确")
        return "验证码不正确"
    elif "密码错误" in data:
        print("登录失败")
        return "登录失败"
    else:
        print("登录异常")
        return "登录异常"
    
# 通过判断返回源代码长度确认是否登录成功
def Source_code_length(browser):
    # 获取页面源代码
    source = browser.page_source
    
    '''
    先计算计算各个状态下的页面源代码的长度，然后修改相应的代码长度 8553 8554
    '''
    # alert_text = str(len(source))
    if len(source) == 8553:
        print("验证码不正确")
        return "验证码不正确"
    elif len(source) == 8554:
        print("登录失败")
        return "登录失败"
    else:
        print("无法通过源代码的长度判断：", len(source))
        return "无法通过源代码的长度判断"


# 通过定位提示信息确认是否登录成功
def Location_prompt_information(browser):
    # 使用XPath定位元素并提取文本
    element = browser.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[6]/table/tbody/tr/td[2]')
    text = element.text
    if "无效的用户信息" in text:
        print("登录失败")
        return "登录失败"
    elif "验证码不正确" in text:
        print("验证码不正确")
        return "验证码不正确"
    else:
        print("登录异常")
        return "登录异常"

# 弹窗处理
def pop_ups(browser):
    # 如果登录后存在alert弹窗，则开启自动按下键盘的 ENTER 键
    # 检测是否存在弹窗，如果存在则关闭
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    # print('------------获取alert对话框的内容------------')
    alert_text = browser.switch_to.alert.text
    # print('------------打印警告对话框内容------------')
    # print ('data: ',alert_text)
    browser.switch_to.alert.dismiss()
    # print("关闭弹窗")
    return alert_text