import json
import requests
import urllib3
from common.Requests_func import req_post
from modules.login_validate import res_json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 登录网页, 根据实际需求更改
def login_request_main(user, passwd, captcha, config):
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'mediav=%7B%22eid%22%3A%221133470%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A1%2C%22_refnf%22%3A1%7D; PHPSESSID=bt6fact6fjqdk8g6679scol976; Qs_lvt_443304=1703039890%2C1706591876; mediav=%7B%22eid%22%3A%221133470%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A1%2C%22_refnf%22%3A0%7D; Qs_pv_443304=2971096022078003000%2C665822840133847900%2C2611051142910009000%2C2005282463921183700%2C2407804943288993000',
    }

    json_data = {
        'username': user,
        'password': passwd,
        'captcha': captcha,
        '_captcha_id': '',
        'redirect': '',
    }

    # 返回包格式有json、有普通、有加密

    response = req_post(config['requests_url'], data=json_data, header=headers)
    # response = requests.post(config['requests_url'],headers=headers,data=json_data,verify=False,)
    if response:
        return_text = res_json(response.text)
    else:
        return_text = ""
    return return_text, user, passwd