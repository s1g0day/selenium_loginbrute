#!/usr/bin/env python
# coding=utf-8
import time
import random
import requests
from requests.exceptions import ConnectionError
from common.hander_random import requests_headers

headers = requests_headers()

def req_get(url, data=None, header=None):
    time.sleep(random.random()*5)
    try:
        if header:
            headers.update(header)
        # 发送请求的代码
        response = requests.get(url=url, headers=headers, data=data, verify=False, allow_redirects=False, timeout=(4,20))
        response.encoding = response.apparent_encoding # apparent_encoding比"utf-8"错误率更低
        
        # 检查响应状态码
        if response.status_code == 200:
            # 处理成功响应的逻辑
            print('请求成功')
            return response
        else:
            # 处理其他响应状态码的逻辑
            print('请求失败，状态码：', response.status_code)
        
    except ConnectionError as e:
        # 处理连接错误的逻辑
        print('连接错误:', e)

    except Exception as e:
        # 处理其他异常的逻辑
        print('发生了其他异常:', e)
def req_post(url, data=None, header=None):
    try:
        if header:
            headers.update(header)
        response = requests.post(url=url, headers=headers, data=data, verify=False, allow_redirects=False, timeout=(4,20))
        response.encoding = response.apparent_encoding # apparent_encoding比"utf-8"错误率更低

        # 检查响应状态码
        if response.status_code == 200:
            # 处理成功响应的逻辑
            print('请求成功')
            return response
        else:
            # 处理其他响应状态码的逻辑
            print('请求失败，状态码：', response.status_code)
    except ConnectionError as e:
        # 处理连接错误的逻辑
        print('连接错误:', e)
    except Exception as e:
        # 处理其他异常的逻辑
        print('发生了其他异常:', e)

