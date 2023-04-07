import os
from PIL import Image

# def in_file(filename):
#     return os.path.abspath(filename)   # Retorna o caminho completo do arquivo em questao

# def out_file(filename):
#     return os.path.abspath(filename)  # Retorna o caminho completo do arquivo em questao
# ------------------------------------------------>

'''
  Modo convencional
   - Não considera uma media ponderada, portanto
      Não é possível realizar uma transformação 
        com qualidade
'''
def grayscale(colored):
    w, h = colored.size    # Tupla que entrega a largura e altura da imagem
    img = Image.new("RGB", (w,h))

    for col in range(w):
        for lin in range(h):
            pxl = colored.getpixel((col,lin))  # Pegando cada pixel
            luminance = (pxl[0] + pxl[1] + pxl[2]) // 3    # Pegando a quantidade de luminancia do pixel, com base na media dos tres valores RGB
            img.putpixel((col, lin), (luminance, luminance, luminance))
    return img

'''
  Modo real
   - É feito uma média ponderada na imagem
     em razão do seguinte:
       (1) Verde possui mais preferência, logo perde MENOS intensidade de cor
       (2) Vermelho vem em seguida, perdendo pouco MAIS intensidade
       (3) Azul por ultimo, perdendo MUITA INTENSIDADE DE COR

        ----> Ela da maior peso para o verde
'''
def true_grayscale(colored):
    w, h = colored.size    # Tupla que entrega a largura e altura da imagem
    img = Image.new("RGB", (w,h))

    for col in range(w):
        for lin in range(h):
            pxl = colored.getpixel((col,lin))  # Pegando cada pixel
            luminance = int( 0.3 * pxl[0] + 0.59 * pxl[1] + 0.11 * pxl[2]) // 3    # Pegando a quantidade de luminancia do pixel, com base na media ponderada supracitada no comentario acima.
            img.putpixel((col, lin), (luminance, luminance, luminance))
    return img
# ---------------------------------------------------------------------------------------------------------------------------------------------------
def black_white(infile, outfile):
    baloes = Image.open(infile)
    pb_baloes = true_grayscale(baloes)
    pb_baloes.save(outfile)


def main():
    from sys import argv
    if len(argv) == 1:
        file = input('Qual o arquivo? R = ')
    else:
        file = argv[1]

    black_white(file, 'resultado.jpg')

if __name__ == '__main__':
    main()