# 带带弟弟 OCR
from ddddocr import DdddOcr

ocr = DdddOcr(show_ad=False, old=True)

#  第一个验证截图保存：verification_code_1.png
with open("./images/captcha.jpg", 'rb') as f:
    image = f.read()
res = ocr.classification(image)
print(res)
