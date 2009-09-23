# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import codecs

class SongParser():

  def __init__(self, ruta_archivo):
    self.ruta_archivo = ruta_archivo
    self.parrafos = []

  def crear_parrafos(self):
	archivo = codecs.open(self.ruta_archivo, 'r', 'utf-8')
	parrafo = ''
	for linea in archivo.readlines():
	  if not linea.strip() == '':
		parrafo = parrafo + linea
	  else:
		if not parrafo == '':
		  self.parrafos.append(unicode(parrafo.strip()))
		  parrafo = ''
	return self.parrafos

if __name__ == "__main__":
  s = SongParser("songs/De tal manera.txt")
  for i in s.crear_parrafos():
	print 'PARRAFO'
	print i
  
