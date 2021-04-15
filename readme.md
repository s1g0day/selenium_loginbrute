# 环境

~~~
python3.7
chrome
windows
~~~

# 安装配置

1.安装python模块

~~~
pip3 install -r requirements.txt
~~~

2.下载chromedriver并移动到python/script目录下

> ps: 默认已经设置好python的环境变量

3.设置selenium的`xpath`和`id`路径，注释中已说明

4.在dic目录下导入username.txt和password.txt文件

5.运行

~~~
python3 selenium_loginbrute.py
~~~



# 参考

[selenium 弹出框的处理 switch_to.alert 三种类型](https://blog.csdn.net/chang995196962/article/details/89641100)

[Python之Selenium+Chromedriver爆破登录](https://www.yuque.com/corgi/yfbm4o/grormk)

[keybd_event模拟键盘输入](https://blog.csdn.net/qq_29360495/article/details/53006082)

[python+selenium+百度OCR 验证码识别登录](https://blog.csdn.net/weapon_host/article/details/104574073)



# 更新历史

## selenium_loginbrute 0.3 (2021-04-15)

### 新增功能

- 修改二维码识别的API，调用第三方打码平台图鉴

- 添加简单的进度提示，同步更新百度API的代码

- 新增历史代码备份目录

- 重命名文件

  ~~~
  # 调用百度文字识图API的代码
  selenium_loginbrute(baidu).py
  
  # 调用第三方平台API的代码
  selenium_loginbrute(Coding).py
  ~~~

### 新想法

- 尝试实现代码多线程
- 尝试解决代码运行后不能操作电脑的问题

## selenium_loginbrute 0.2 (2021-04-14)

### 新增功能

- 添加循环功能，实现脚本自动爆破
- 添加日志功能，实现将除账号密码不正确的弹窗信息写入日志

### 新想法

- 尝试调用第三方打码平台API，提高二维码识别正确率

## login_test 0.1 (2021-04-14)

### 新增功能

- 通过python的selenium实现一次性登录功能的测试
- 调用百度文字识图api

### 新想法

- 尝试完成循环爆破代码
