#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *

from colection_parser import ColectionParser
from song_parser import SongParser

from Ui_mainWindow import Ui_MainWindow
#from salida import Salida

class MiClase(QMainWindow):
	
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.create_index("songs/*.txt")
		self.ui.gvVistaPrevia.setViewport(QGLWidget())
		self.font = QFont()
		self.text = QString("Trigales Worship")
		self.bgcolor = QColor("yellow")
		self.pic = QPixmap("fondo.jpg")
#		self.pic = self.pic.scaled(266, 200, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
		self.createScene()
#		self.mostrar_letra()
		### Conexiones
		self.connect(self.ui.btnAgregar, SIGNAL("clicked()"), self.agregar_a_la_lista)
		self.connect(self.ui.btnQuitar, SIGNAL("clicked()"), self.quitar_de_la_lista)
		self.connect(self.ui.listLista, SIGNAL("itemSelectionChanged()"), self.mostrar_letra)
#		self.connect(self.ui.fontTipoDeLetra, SIGNAL("currentFontChanged(const QFont &)"), self.setFont)
#		self.connect(self.ui.btnTipoLetra, SIGNAL("clicked()"), self.setFont)
		self.connect(self.ui.btnComenzar, SIGNAL("clicked()"), self.comenzarPresentacion)
		self.connect(self.ui.btnSiguiente,  SIGNAL("clicked()"),  self.siguiente)
		self.connect(self.ui.btnAnterior,   SIGNAL("clicked()"),  self.anterior)
		self.connect(self.ui.btnInicio, SIGNAL("clicked()"),  self.inicio)
		self.connect(self.ui.btnFin, SIGNAL("clicked()"),  self.fin)
#		self.connect(self.ui.btnColor, SIGNAL("clicked()"),  self.setColor)

	def create_index(self, ruta):
		c = ColectionParser(ruta)
		self.indice = c.crear_indice()
		for i in self.indice.keys():
		  self.ui.listColeccion.addItem(QString(i))
		self.ui.listColeccion.sortItems()

	def agregar_a_la_lista(self):
		self.ui.listLista.addItem(self.ui.listColeccion.currentItem().text())

	def quitar_de_la_lista(self):
		self.ui.listLista.takeItem(self.ui.listLista.row(self.ui.listLista.currentItem()))

	def mostrar_letra(self):
		titulo = unicode(self.ui.listColeccion.currentItem().text())
		s = SongParser(self.indice[titulo])
		parrafos = s.crear_parrafos()
		self.ui.listControles.clear()
		for parrafo in parrafos:
			self.ui.listControles.addItem(parrafo)

	def createScene(self):
		print "redibujando"
		scene = QGraphicsScene()
		self.ui.gvVistaPrevia.setScene(scene)
		#scene.addPixmap(self.pic)
		scene.setFont(self.font)
#		scene.addText(self.text, self.font)
		scene.addText(self.text)
		scene.setBackgroundBrush(self.bgcolor)
		self.scene = scene
		#self.ui.gvVistaPrevia.fitInView(scene.sceneRect());
		#self.ui.gvVistaPrevia.alignment()
		self.ui.gvVistaPrevia.update()

	def setFont(self):
#		self.font = QFont(font)
		self.font, ok = QFontDialog.getFont()
		if ok:
			self.createScene()

	def setText(self, text):
		self.text = QString(text)
		self.createScene()

	def setPic(self, pic):
		self.pic = QPixmap(pic)
		self.createScene()

	def setPic(self, color):
		self.bgcolor = QColor(color)
		self.createScene()

	def comenzarPresentacion(self):
		salida = Salida()
		salida.show()

	def siguiente(self):
		fila = self.ui.listControles.currentRow()
		if fila == -1:
			self.ui.listControles.setCurrentRow(0)
		elif fila == self.ui.listControles.count() - 1:
			print "ultima fila"
		else:
			self.ui.listControles.setCurrentRow(fila + 1)

	def anterior(self):
		fila = self.ui.listControles.currentRow()
		if fila == -1:
			self.ui.listControles.setCurrentRow(self.ui.listControles.count() - 1)
		elif fila == 0:
			print "primera fila"
		else:
			self.ui.listControles.setCurrentRow(fila - 1)

	def inicio(self):
		self.ui.listControles.setCurrentRow(0)

	def fin(self):
		self.ui.listControles.setCurrentRow(self.ui.listControles.count() - 1)

	def setColor(self):
		color = QColorDialog.getColor()
		if color.isValid():
			self.bgcolor = color
			self.createScene()

#def abrir_archivo(self):
		#dlgAbrir = QtGui.QFileDialog(self)
		#self.nombreArchivo = dlgAbrir.getOpenFileName()
		#texto = open(self.nombreArchivo, 'r').read()
		#self.ui.textEdit.setText(texto)
	#def guardar_archivo(self):
		#archivo = open(self.nombreArchivo, 'w')
		#archivo.write(self.ui.textEdit.toPlainText())
		#archivo.close()
	#def mostrar_archivo(self):
		#for i in self.archivo.readlines():
			#if(self.archivo.readlines % 2):
				#valor = str(self.ui.textEdit.text())
				#valor = i.strip().split('.')
				#self.ui.textEdit.setText(valor)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ventana = MiClase()
	ventana.show()
	sys.exit(app.exec_())
