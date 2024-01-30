
import random
import string
import hashlib
from PIL import Image
from selenium.webdriver.common.by import By


# 验证码的获取
def picture_main(url, browser, captcha_update_xpath):
    browser.get(url)
    browser.implicitly_wait(10)
    browser.save_screenshot('output/VerifyCode/pic/pic.png')
    # 点击更换验证码
    code_element = browser.find_element(By.XPATH, captcha_update_xpath)
    # print("验证码的坐标为：", code_element.location)
    # print("验证码的大小为：", code_element.size)
    left = code_element.location['x']#x点的坐标
    top = code_element.location['y']#y点的坐标
    right = code_element.size['width']+left#上面右边点的坐标
    height = code_element.size['height']+top#下面右边点的坐标
    image = Image.open('output/VerifyCode/pic/pic.png')

    # 生成随机字符串作为输入
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # 使用SHA256哈希算法生成哈希值
    hash_value = hashlib.sha256(random_string.encode()).hexdigest()
    VerifyCode = 'output/VerifyCode/captcha/'+hash_value
    code_image = image.crop((left, top, right, height))
    code_image.save(VerifyCode + '.png')#截取的验证码图片保存为新的文件
    

    return VerifyCode