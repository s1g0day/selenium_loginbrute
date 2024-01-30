import ddddocr

# 验证码的识别
def ddddocr_captcha_main(VerifyCode):
    
    # 初始化对象
    ocr = ddddocr.DdddOcr()
    # 读取图片
    def get_file_content(file_path):
        with open(file_path, 'rb') as f:
            return f.read()
    
    image = get_file_content(VerifyCode + '.png')
    # 读取验证码
    res = ocr.classification(image)
    if res:
        print("\n得到验证码：" + res)
        return res
    else:
        print("\n验证码识别失败")
        pass