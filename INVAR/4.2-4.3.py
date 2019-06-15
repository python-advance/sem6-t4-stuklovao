# Задания 4.2-4.3

import pyqrcode
import png

def creater(content, module_color, background, file_format, scale):
    qrcode = pyqrcode.create(content)
    if file_format == 'png':
        qrcode.png('qr.png', module_color = module_color, background=background,scale=scale)
    elif file_format == 'svg':
        qrcode.svg('qr.svg', module_color = module_color, background=background,scale=scale)

result = input("Введите строку: ")
creater(result, (0,0,0), (0,0,128), file_format = 'png', scale = 6)
