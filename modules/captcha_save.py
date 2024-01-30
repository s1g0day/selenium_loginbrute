import os

def captcha_save_main(res, VerifyCode):
    captcha_file = VerifyCode + '.png'
    # 删除图片
    # os.remove(VerifyCode + '.png')

    # 获取文件名
    file_name = os.path.basename(captcha_file)
    # print("文件名:", file_name)

    # 获取文件路径 /output/VerifyCode/captcha
    dir_path = os.path.dirname(captcha_file)
    # print("目录路径:", dir_path)
    
    # 重命名图片
    if res:
        newfile_name = dir_path + "/" + res + '_' + file_name + '.png'
        os.rename(VerifyCode + '.png', newfile_name)