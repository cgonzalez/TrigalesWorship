# -*- coding: utf-8 -*-
import glob
import codecs

class ColectionParser():

  def __init__(self, ruta):
    self.ruta = ruta
    self.indice = {}

  def crear_indice(self):
    lista_archivos = glob.glob(self.ruta)
    for nombre_archivo in lista_archivos:
      archivo = codecs.open(nombre_archivo, 'r', 'utf-8')
      titulo = archivo.readline().strip()  # La primera línea se toma como título
      self.indice[titulo] = nombre_archivo
    return self.indice

if __name__ == "__main__":
  c = ColectionParser("songs/*.txt")
  indice = c.crear_indice()
  print indice
  