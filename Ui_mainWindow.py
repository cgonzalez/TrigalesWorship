# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/christian/Documentos/Proyectos/TrigalesWorship/mainWindow.ui'
#
# Created: Sun Aug 23 00:57:28 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 622)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lnColeccion = QtGui.QLineEdit(self.tab)
        self.lnColeccion.setObjectName("lnColeccion")
        self.horizontalLayout_3.addWidget(self.lnColeccion)
        self.btnBuscar = QtGui.QPushButton(self.tab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/edit-find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setObjectName("btnBuscar")
        self.horizontalLayout_3.addWidget(self.btnBuscar)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.listColeccion = QtGui.QListWidget(self.tab)
        self.listColeccion.setDragEnabled(True)
        self.listColeccion.setDragDropOverwriteMode(False)
        self.listColeccion.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.listColeccion.setAlternatingRowColors(False)
        self.listColeccion.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listColeccion.setObjectName("listColeccion")
        self.verticalLayout_8.addWidget(self.listColeccion)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnNuevo = QtGui.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        self.btnNuevo.setObjectName("btnNuevo")
        self.horizontalLayout_2.addWidget(self.btnNuevo)
        self.btnEditar = QtGui.QPushButton(self.tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditar.setIcon(icon2)
        self.btnEditar.setObjectName("btnEditar")
        self.horizontalLayout_2.addWidget(self.btnEditar)
        self.btnAgregar = QtGui.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/list-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregar.setIcon(icon3)
        self.btnAgregar.setObjectName("btnAgregar")
        self.horizontalLayout_2.addWidget(self.btnAgregar)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listLista = QtGui.QListWidget(self.groupBox_2)
        self.listLista.setAcceptDrops(True)
        self.listLista.setDragEnabled(True)
        self.listLista.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.listLista.setAlternatingRowColors(False)
        self.listLista.setMovement(QtGui.QListView.Free)
        self.listLista.setObjectName("listLista")
        self.verticalLayout_2.addWidget(self.listLista)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnSubir = QtGui.QPushButton(self.groupBox_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/arrow-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSubir.setIcon(icon4)
        self.btnSubir.setObjectName("btnSubir")
        self.horizontalLayout_4.addWidget(self.btnSubir)
        self.btnBajar = QtGui.QPushButton(self.groupBox_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/arrow-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBajar.setIcon(icon5)
        self.btnBajar.setObjectName("btnBajar")
        self.horizontalLayout_4.addWidget(self.btnBajar)
        self.btnQuitar = QtGui.QPushButton(self.groupBox_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnQuitar.setIcon(icon6)
        self.btnQuitar.setObjectName("btnQuitar")
        self.horizontalLayout_4.addWidget(self.btnQuitar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.listControles = QtGui.QListWidget(self.groupBox_5)
        self.listControles.setAutoFillBackground(False)
        self.listControles.setAlternatingRowColors(False)
        self.listControles.setSpacing(5)
        self.listControles.setViewMode(QtGui.QListView.ListMode)
        self.listControles.setSelectionRectVisible(False)
        self.listControles.setObjectName("listControles")
        self.verticalLayout_5.addWidget(self.listControles)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnInicio = QtGui.QPushButton(self.groupBox_5)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/go-first-view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInicio.setIcon(icon7)
        self.btnInicio.setObjectName("btnInicio")
        self.horizontalLayout_6.addWidget(self.btnInicio)
        self.btnAnterior = QtGui.QPushButton(self.groupBox_5)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/go-previous-view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAnterior.setIcon(icon8)
        self.btnAnterior.setObjectName("btnAnterior")
        self.horizontalLayout_6.addWidget(self.btnAnterior)
        self.btnSiguiente = QtGui.QPushButton(self.groupBox_5)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/go-next-view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSiguiente.setIcon(icon9)
        self.btnSiguiente.setObjectName("btnSiguiente")
        self.horizontalLayout_6.addWidget(self.btnSiguiente)
        self.btnFin = QtGui.QPushButton(self.groupBox_5)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/go-last-view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFin.setIcon(icon10)
        self.btnFin.setObjectName("btnFin")
        self.horizontalLayout_6.addWidget(self.btnFin)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnFontType = QtGui.QToolButton(self.groupBox_3)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/application-x-font-ttf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFontType.setIcon(icon11)
        self.btnFontType.setObjectName("btnFontType")
        self.horizontalLayout_7.addWidget(self.btnFontType)
        self.btnFontColor = QtGui.QToolButton(self.groupBox_3)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/format-text-color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFontColor.setIcon(icon12)
        self.btnFontColor.setObjectName("btnFontColor")
        self.horizontalLayout_7.addWidget(self.btnFontColor)
        self.btnBGColor = QtGui.QToolButton(self.groupBox_3)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/fill-color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBGColor.setIcon(icon13)
        self.btnBGColor.setObjectName("btnBGColor")
        self.horizontalLayout_7.addWidget(self.btnBGColor)
        self.btnBGImage = QtGui.QToolButton(self.groupBox_3)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/insert-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBGImage.setIcon(icon14)
        self.btnBGImage.setObjectName("btnBGImage")
        self.horizontalLayout_7.addWidget(self.btnBGImage)
        spacerItem = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gvVistaPrevia = QtGui.QGraphicsView(self.groupBox_3)
        self.gvVistaPrevia.setMinimumSize(QtCore.QSize(266, 200))
        self.gvVistaPrevia.setMaximumSize(QtCore.QSize(266, 200))
        self.gvVistaPrevia.setObjectName("gvVistaPrevia")
        self.horizontalLayout.addWidget(self.gvVistaPrevia)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.btnComenzar = QtGui.QPushButton(self.groupBox_3)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/media-playback-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnComenzar.setIcon(icon15)
        self.btnComenzar.setCheckable(True)
        self.btnComenzar.setObjectName("btnComenzar")
        self.verticalLayout_4.addWidget(self.btnComenzar)
        self.btnSoloImagen = QtGui.QPushButton(self.groupBox_3)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/imagegallery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSoloImagen.setIcon(icon16)
        self.btnSoloImagen.setCheckable(True)
        self.btnSoloImagen.setObjectName("btnSoloImagen")
        self.verticalLayout_4.addWidget(self.btnSoloImagen)
        self.btnPantallaBlanca = QtGui.QPushButton(self.groupBox_3)
        self.btnPantallaBlanca.setCheckable(True)
        self.btnPantallaBlanca.setObjectName("btnPantallaBlanca")
        self.verticalLayout_4.addWidget(self.btnPantallaBlanca)
        self.btnPantallaNegra = QtGui.QPushButton(self.groupBox_3)
        self.btnPantallaNegra.setCheckable(True)
        self.btnPantallaNegra.setObjectName("btnPantallaNegra")
        self.verticalLayout_4.addWidget(self.btnPantallaNegra)
        self.btnDetener = QtGui.QPushButton(self.groupBox_3)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/media-playback-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDetener.setIcon(icon17)
        self.btnDetener.setCheckable(True)
        self.btnDetener.setObjectName("btnDetener")
        self.verticalLayout_4.addWidget(self.btnDetener)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 24))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEditar = QtGui.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuVer = QtGui.QMenu(self.menubar)
        self.menuVer.setObjectName("menuVer")
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBuscar.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo.setText(QtGui.QApplication.translate("MainWindow", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEditar.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAgregar.setText(QtGui.QApplication.translate("MainWindow", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Canciones", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Biblia", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Lista de reproducción", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSubir.setText(QtGui.QApplication.translate("MainWindow", "Subir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBajar.setText(QtGui.QApplication.translate("MainWindow", "Bajar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnQuitar.setText(QtGui.QApplication.translate("MainWindow", "Quitar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Controles", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInicio.setText(QtGui.QApplication.translate("MainWindow", "Inicio", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAnterior.setText(QtGui.QApplication.translate("MainWindow", "Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSiguiente.setText(QtGui.QApplication.translate("MainWindow", "Siguiente", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFin.setText(QtGui.QApplication.translate("MainWindow", "Fin", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Vista previa", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFontType.setText(QtGui.QApplication.translate("MainWindow", "Tipo de letra", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFontColor.setText(QtGui.QApplication.translate("MainWindow", "Color de letra", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBGColor.setText(QtGui.QApplication.translate("MainWindow", "Fondo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBGImage.setText(QtGui.QApplication.translate("MainWindow", "Imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnComenzar.setText(QtGui.QApplication.translate("MainWindow", "Comenzar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSoloImagen.setText(QtGui.QApplication.translate("MainWindow", "Sólo imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPantallaBlanca.setText(QtGui.QApplication.translate("MainWindow", "Pantalla negra", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPantallaNegra.setText(QtGui.QApplication.translate("MainWindow", "Pantalla blanca", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDetener.setText(QtGui.QApplication.translate("MainWindow", "Detener", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEditar.setTitle(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVer.setTitle(QtGui.QApplication.translate("MainWindow", "Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

