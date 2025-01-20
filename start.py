# Inspirado no artigo: https://www.dio.me/articles/reducao-de-dimensionalidade-em-imagens-usando-python

import sys
from PIL import Image

def converter_para_cinza(imagem):
    largura, altura = imagem.size
    imagem_cinza = Image.new("L", (largura, altura))

    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem.getpixel((x, y))
            valor_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_cinza.putpixel((x, y), valor_cinza)

    return imagem_cinza

def binarizar_imagem(imagem_cinza, limiar=127):
    largura, altura = imagem_cinza.size
    imagem_binaria = Image.new("1", (largura, altura))

    for y in range(altura):
        for x in range(largura):
            valor_cinza = imagem_cinza.getpixel((x, y))
            valor_binario = 1 if valor_cinza > limiar else 0
            imagem_binaria.putpixel((x, y), valor_binario)

    return imagem_binaria

def main():
    if len(sys.argv) != 2:
        print('Uso correto: python start.py "caminho_da_imagem"')
        sys.exit(1)

    caminho_imagem = sys.argv[1]
    
    try:
        imagem_original = Image.open(caminho_imagem)
    except FileNotFoundError:
        print(f"Imagem no caminho {caminho_imagem} não encontrada.")
        sys.exit(1)

    imagem_cinza = converter_para_cinza(imagem_original)
    imagem_binaria = binarizar_imagem(imagem_cinza)

    imagem_original.show()
    imagem_cinza.show()
    imagem_binaria.show()

if __name__ == "__main__":
    main()
