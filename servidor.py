#! /usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui, uic

class servidorInterfaz(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.updateTable())
        self.timer.start(250)
        # Set up the user interface from Designer.
        self.ui = uic.loadUi("servidor.ui")
        self.ui.tableWidget.horizontalHeader().hide()
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.setRowCount(20)
        self.ui.tableWidget.setColumnCount(20)
        ###self.ui.connect(self.ui.tableWidget, QtCore.SIGNAL(QtCore.keyPressEvent()), self, SLOT(self.keyPressEvent()))
        self.ui.spin_filas.valueChanged.connect(lambda: self.resizeTable())
        self.ui.spin_colum.valueChanged.connect(lambda: self.resizeTable())
        self.ui.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.spin_espera.valueChanged.connect(lambda: self.esperaAct())
        self.ui.iniciar_juego.setCheckable(True)
        self.ui.terminar_juego.setVisible(False)
        self.ui.iniciar_juego.clicked.connect(lambda: self.ini_juego())
        self.ui.terminar_juego.clicked.connect(lambda: self.ter_juego())
        self.ui.show()

    def resizeTable(self):
    	self.ui.tableWidget.setRowCount(self.ui.spin_filas.value())
    	self.ui.tableWidget.setColumnCount(self.ui.spin_colum.value())

    def esperaAct(self):
    	self.timer.start(self.ui.spin_espera.value())

    def updateTable(self):
    	if (self.ui.iniciar_juego.isChecked()):
    		#aqui va la actualizacion de la tabla
    		print "hola"


    def ini_juego(self):
    	if (self.ui.iniciar_juego.isChecked()):
    		self.ui.iniciar_juego.setText("Pausar Juego")
    		self.ui.terminar_juego.setVisible(True)
    		#aqui va la inicializacion de snake
    	else:
    		self.ui.iniciar_juego.setText("Iniciar Juego")

    def ter_juego(self):
    	if (self.ui.iniciar_juego.isChecked()):
    		self.ui.terminar_juego.setVisible(False)
    		self.ui.iniciar_juego.setCheckable(False)
    		self.ui.iniciar_juego.setCheckable(True)
    		self.ui.iniciar_juego.setText("Iniciar Juego")
    	self.ui.terminar_juego.setVisible(False)
    	#aqui va el reinicio de la tabla del juego


	def keyPressEvent(self, event):
	    key = event.key()
	    print(key)
	    if key == QtCore.Qt.Key_Left:
	        print('Left Arrow Pressed')
	    elif key == QtCore.Qt.Key_Up:
	    	print('Up Arrow Pressed')
	    elif key == QtCore.Qt.Key_Right:
	    	print('Right Arrow Pressed')
	    elif key == QtCore.Qt-Key_Down:
    		print('Down Arrow Pressed')

app = QtGui.QApplication(sys.argv)
window = servidorInterfaz()
sys.exit(app.exec_())