from PIL import Image
import numpy as np
import os

def triangle(l, m = False):
    MOD = (255,10,200)  # RGB
    WHITE = (0xff,0xff,0xff)
    BLACK = (0,0,0)

    img = Image.new("RGB", (l,l), (255,255,255))
    for n in range(l):
        for x in range(l):
            if n < x:
                img.putpixel((n,x), BLACK)
            elif not m:
                img.putpixel((n,x), MOD)
            else:
                img.putpixel((n,x), WHITE)

    return img

def franca(height):
    width = 3 * height // 2

    BLUE = (0, 85, 164)
    WHITE = (255,255,255)
    RED = (239, 65, 53)

    img = Image.new("RGB", (width, height), WHITE)  # PINTAR TUDO DE BRANCO PRIMEIRAMENTE

    offset = width//3
    for x in range(offset):
        for y in range(offset * 2):
            img.putpixel((x,y), BLUE)
            img.putpixel((x + (2 * offset), y), RED)   # 2 * offset  PULA 2 FAIXAS PARA DESENHAR O VERMELHO NA TERCEIRA
    
    return img

def cript():
    msg = ''.join([str(hex(ord(x)))[2:] for x in 'MENSAGEM_SECRETA'])

    img = Image.new("RGB", (400,400), (0,0,0))  # Max_Msg_len = 106.100 = (400 x 400) / 15
    for x in range(len(msg)/2):
        img.putpixel((0,))


if __name__ == '__main__':
    tri = triangle(800)
    franca = franca(800)
    tri.show()
    franca.show()

    ss = np.array((t))
    print(ss)