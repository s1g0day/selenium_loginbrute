import os
from urllib import parse

# 判断是否保存验证码
def captcha_save_main(log_file, res, VerifyCode, config):
    captcha_file = VerifyCode + '.png'

    # 获取文件名
    file_name = os.path.basename(captcha_file)
    # print("文件名:", file_name)

    # 获取文件路径 /output/VerifyCode/captcha
    dir_path = os.path.dirname(captcha_file)
    # print("目录路径:", dir_path)

    if log_file != "login_failed":
        os.remove(VerifyCode + '.png')  # 删除验证码识别错误的图片
    else:
        parsed_url = parse.urlparse(config['url'])
        hostname = parsed_url.hostname

        if hostname:
            Host = hostname
            # print(f"主机名: {Host}")
        else:
            Host = parsed_url.netloc
            # print(f"IP地址: {Host}")

        # 创建文件夹路径
        folder_path = os.path.join("output/VerifyCode/captcha", Host)
        folder_path = folder_path.replace("\\", "\\\\")
        # 检查文件夹是否存在，如果不存在则创建
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        newfile_name = dir_path + '/' + Host + '/' + res + '_' + file_name
        # 重命名图片: l路径 + 验证码_随机hash.png
        os.rename(captcha_file, newfile_name)

# 写入文件
def save_log(log_file, log_alert, log_user, log_passwd, res, VerifyCode, config):
    with open("output/log/" + log_file + ".log", "a") as file_object:
        file_object.write('user: ' + log_user + ', passwd: ' + log_passwd + ', data: ' + log_alert + '\n')
    captcha_save_main(log_file, res, VerifyCode, config)


def alertlog_main(config, log_alert, log_user, log_passwd, res, VerifyCode):
    if log_alert:

        # 验证码错误
        if log_alert in config['captcha_error']:
            save_log("captcha_error", log_alert, log_user, log_passwd, res, VerifyCode, config)
        # 登录失败
        elif log_alert in config['login_failed']:
            save_log("login_failed", log_alert, log_user, log_passwd, res, VerifyCode, config)
        # # 登录成功
        # elif log_alert in config['captcha_error']:
        #     save_log("captcha_error", log_alert, log_user, log_passwd, res, VerifyCode, config)
        # 其他
        else:
            save_log("error", log_alert, log_user, log_passwd, res, VerifyCode, config)
    else:
        save_log("error", log_alert, log_user, log_passwd, res, VerifyCode, config)