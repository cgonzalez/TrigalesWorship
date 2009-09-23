# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.text = self.tr("CARGANDO...")
        self.font = QFont("Helvetica", 44)
        self.view = QGraphicsView()
        controlsLayout = QGridLayout()
        layout = QHBoxLayout()
        layout.addWidget(self.view, 1)
        self.setLayout(layout)
        self.createScene()
        self.setWindowTitle(self.tr("Text Effects"))
        self.setText("Hola mundo")
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        print size
        self.resize(screen.width(),  screen.height())
#        self.setFont("Helvetica", 55)


    def createScene(self):
        scene = QGraphicsScene()
        pic = QPixmap('fondo.jpg')
        self.view.setScene(scene)
        scene.addText(QString("<b>Hola mundo\nlinea 2\nlinea 3</b>"))
        #scene.addPixmap(pic)
        self.scene = scene
        self.view.update()

    def setText(self, text):
        self.text = QString(text)
        self.createScene()
    
    def setFont(self, font):
        self.font = QFont(font)
        self.createScene()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
