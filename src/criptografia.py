from random import randint
from time import time
import numpy as np
from matplotlib import pyplot as plt
import cv2



#======================== INPUT IMAGE ========================
def input_img(image_name: str):
  # Retorna as dimencoes da imagem e um objeto que é a sua imagem(img)
  image = cv2.imread(image_name)
  print("Dimensões da imagem: " + str(image.shape))
  altura, largura, canais = image.shape
  print(f'Largura: {largura}')
  print(f'Altura: {altura}')
  print(f'Canais de cores: {canais}')
  return image, altura, largura, canais



#======================== SHOW IMAGE ========================
def show_image(image):
  # Mostra Uma imagem
  plt.figure(figsize = (6, 6))
  plt.imshow(image)
  plt.show()



#======================== IMAGE BUILDER ========================
def image_builder(altura: int, largura: int, canais: int, intarray: list):
  # Retorna uma imagem com o conteudo intarray
  return np.ndarray(shape=(altura, largura, canais), dtype=int, buffer=np.array(list(intarray)))




#======================== CRIPTOGRAFAR IMAGEM ========================
def criptografar(image, altura: int, largura: int, canais: int, operacao: str):
  # ^ XOR
  # & AND
  # | OR
  t = time()
  op = {
      'AND': lambda a, b : a & b,
      'OR' : lambda a, b : a | b,
      'XOR': lambda a, b : a ^ b
  }
  ENC = []
  PWD = []
  for y in range(0, altura):
    for x in range(0, largura):
      for z in range(canais):
        mini_chave = randint(0,255)
        PWD.append(mini_chave)
        ENC.append(op[operacao](int(image[y][x][z]), mini_chave))
  
  print('Tempo de criptografia:', time() - t, 'sec')
  
  return ENC
