from PIL import Image
import numpy as np

# Função para converter imagem colorida para níveis de cinza
def converter_para_cinza(imagem):
    return imagem.convert('L')

# Função para binarizar a imagem (preto e branco)
def binarizar_imagem(imagem_cinza, limite=128):
    # Converta a imagem para um array numpy
    array_imagem = np.array(imagem_cinza)
    
    # Aplique o limiar para binarizar
    array_binarizada = (array_imagem > limite) * 255
    
    # Converta o array de volta para uma imagem
    imagem_binarizada = Image.fromarray(np.uint8(array_binarizada))
    return imagem_binarizada

# Carregar a imagem
imagem_colorida = Image.open('C:/Users/junio/Downloads/bing-panda-600x600.jpg')

# Converter para níveis de cinza
imagem_cinza = converter_para_cinza(imagem_colorida)
imagem_cinza.show()  # Mostrar a imagem em tons de cinza

# Binarizar a imagem
imagem_binarizada = binarizar_imagem(imagem_cinza, limite=128)
imagem_binarizada.show()  # Mostrar a imagem binarizada (preto e branco)

# Salvar as imagens processadas, se necessário
imagem_cinza.save('imagem_cinza.jpg')
imagem_binarizada.save('imagem_binarizada.jpg')
