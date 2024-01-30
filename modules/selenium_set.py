from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def selenium_main(config):
    options = webdriver.ChromeOptions()
    options.use_chromium = True
    options.add_argument("–incognito") # 隐身模式（无痕模式）
    if config['headless']==True:
        options.add_argument('--headless') # 无界模式
    if config['url'].startswith("https://"):
        options.add_argument('--ignore-certificate-errors') # 设置Chrome忽略网站证书错误
        # print("自动设置Chrome忽略网站证书")
    # options.add_argument("blink-settings=imagesEnabled=false") # 不加载图片
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    options.binary_location = config["CHROMEPATH"]
    s = Service(config["DRIVERPATH"])
    browser = webdriver.Chrome(options=options, service=s)
    browser.implicitly_wait(15)

    return browser
