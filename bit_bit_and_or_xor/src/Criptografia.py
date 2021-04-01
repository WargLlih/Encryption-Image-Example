from random import randint
from time import time
import numpy as np
from matplotlib import pyplot as plt
import cv2
from random import choices, sample



#======================== INPUT IMAGE ========================
def input_img(image_name: str):
  # Retorna as dimencoes da imagem e um objeto que é a sua imagem(img)
  img = cv2.imread(image_name)
  print("Dimensões da imagem: " + str(img.shape))
  altura, largura, canais = img.shape
  print(f'Largura: {largura}')
  print(f'Altura: {altura}')
  print(f'Canais de cores: {canais}')
  return img, altura, largura, canais



#======================== SHOW IMAGE ========================
def show_image(image):
  # Mostra Uma imagem
  #image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  plt.imshow(image)
  plt.show()



#======================== IMAGE BUILDER ========================
def image_builder(altura: int, largura: int, intarray: list):
  # Retorna uma imagem com o conteudo intarray
  return np.ndarray(shape=(altura, largura, 3), dtype=int, buffer=np.array(list(intarray)))



#======================== PASSWORD GENERATOR ========================
def passwd_gen(tamanho: int, valores: tuple):
  #tamanho -> tamnaho da lista
  #valores -> valores possiveis ex: de 0 ate 255 (0, 255)
  v = range(valores[0], valores[1])
  return choices(v, k=tamanho)



#======================== CRIPTOGRAFAR IMAGEM ========================
def criptografar(image, altura: int, largura: int, password: list):
  # ^ XOR
  # & AND
  # | OR
  countpwd = 0
  ENC = []
  for y in range(0, altura):
    for x in range(0, largura):
      for z in range(len(image[y][x])):
        ENC.append(int(image[y][x][z]) ^ password[countpwd%len(password)])
        countpwd+=1
  
  return ENC



#======================== MAIN ========================
def main():
  image_name = input('Nome da imagem com extensão: ') # entrando com a imagem

  a = time() # Timer starts here!

  image, altura, largura, _ = input_img(image_name) # carregando a imagem e pegando suas dimensões
  show_image(image) # mostrando a imagem
  
  PWD = passwd_gen(2**256, (0, 256))
  ENC = criptografar(image, altura, largura, PWD)
  new_image = image_builder(altura, largura, ENC)

  print(f'tempo: {time()- a}') # Timer ends here!
  show_image(new_image)



if __name__ == "__main__":
  main()
