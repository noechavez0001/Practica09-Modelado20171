#! /usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui, uic

class servidorInterfaz(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.timer = QtCore.QTimer()
		self.direccion = "R"
		self.snake = []
		self.timer.timeout.connect(lambda: self.updateTable())
		self.timer.start(250)
		# Set up the user interface from Designer.
		self.ui = uic.loadUi("servidor.ui")
		self.ui.tableWidget.horizontalHeader().hide()
		self.ui.tableWidget.verticalHeader().hide()
		self.ui.tableWidget.setRowCount(20)
		self.ui.tableWidget.setColumnCount(20)
		self.ui.tableWidget.keyPressEvent = self.keyPressEventTable
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

	#cambia el tamano de las filas y renglones para ajustarlos al tamano
	def resizeTable(self):
		self.ui.tableWidget.setRowCount(self.ui.spin_filas.value())
		self.ui.tableWidget.setColumnCount(self.ui.spin_colum.value())

	#modifica el tiempo que tarda en actualizarce el juego en ms
	def esperaAct(self):
		self.timer.start(self.ui.spin_espera.value())

	def updateTable(self):
		if (self.ui.iniciar_juego.isChecked()):
			#aqui va la actualizacion de la tabla
			if (self.direccion=="U"):
				x = self.snake[0]
				a = self.snake[-1]
				c = (x[0] - 1)% self.ui.spin_filas.value()
				self.snake.insert(0,[c,x[1]])
				self.ui.tableWidget.item(a[0],a[1]).setBackground(QtGui.QColor(250,250,250))
				self.ui.tableWidget.item(c,x[1]).setBackground(QtGui.QColor(100,100,150))
				del self.snake[-1]
			elif (self.direccion=="D"):
				x = self.snake[0]
				a = self.snake[-1]
				c = (x[0] + 1)% self.ui.spin_filas.value()
				self.snake.insert(0,[c,x[1]])
				self.ui.tableWidget.item(a[0],a[1]).setBackground(QtGui.QColor(250,250,250))
				self.ui.tableWidget.item(c,x[1]).setBackground(QtGui.QColor(100,100,150))
				del self.snake[-1]
			elif (self.direccion=="R"):
				x = self.snake[0]
				a = self.snake[-1]
				c = (x[1] + 1)% self.ui.spin_colum.value()
				self.snake.insert(0,[x[0], c])
				self.ui.tableWidget.item(a[0],a[1]).setBackground(QtGui.QColor(250,250,250))
				self.ui.tableWidget.item(x[0], c).setBackground(QtGui.QColor(100,100,150))
				del self.snake[-1]
			elif (self.direccion=="L"):
				x = self.snake[0]
				a = self.snake[-1]
				c = (x[1] - 1)% self.ui.spin_colum.value()
				self.snake.insert(0,[x[0],c])
				self.ui.tableWidget.item(a[0],a[1]).setBackground(QtGui.QColor(250,250,250))
				self.ui.tableWidget.item(x[0],c).setBackground(QtGui.QColor(100,100,150))
				del self.snake[-1]
			# Mensaje de que se ha perdido
			if (self.snake[0] in self.snake[1:]):
				QtGui.QMessageBox.about(self, "Info",  """Juego Terminado: \nPerdiste""")
				self.ter_juego()
			print self.snake

	def ini_juego(self):
		#aqui va la inicializacion de snake
		if (self.ui.iniciar_juego.isChecked()):
			self.snake = [[0,5],[0,4],[0,3],[0,2],[0,1],[0,0]]
			self.direccion = "R"
			for x in range(self.ui.spin_filas.value()):
				for y in range(self.ui.spin_colum.value()):
					self.ui.tableWidget.setItem(x, y, QtGui.QTableWidgetItem("", 0))
			self.ui.iniciar_juego.setText("Pausar Juego")
			self.ui.terminar_juego.setVisible(True)
			for x in range(len(self.snake)):
				a = self.snake[x]
				i = self.ui.tableWidget.itemAt(a[0],a[1])
				self.ui.tableWidget.item(a[0],a[1]).setBackground(QtGui.QColor(100,100,150))
		else:
			self.ui.iniciar_juego.setText("Iniciar Juego")


	def ter_juego(self):
		#aqui va el reinicio de la tabla del juego
		if (self.ui.iniciar_juego.isChecked()):
			self.ui.tableWidget.clear()
			self.ui.terminar_juego.setVisible(False)
			self.ui.iniciar_juego.setCheckable(False)
			self.ui.iniciar_juego.setCheckable(True)
			self.ui.iniciar_juego.setText("Iniciar Juego")
		self.ui.terminar_juego.setVisible(False)



	#enventos de presionar una tecla
	def keyPressEventTable(self, event):
		key = event.key()
		if key == QtCore.Qt.Key_Left:
			if (self.direccion != "R"):
				self.direccion = "L"
			print('Left Arrow Pressed')
		elif key == QtCore.Qt.Key_Up:
			if (self.direccion != "D"):
				self.direccion = "U"
			print('Up Arrow Pressed')
		elif key == QtCore.Qt.Key_Right:
			if (self.direccion != "L"):
				self.direccion = "R"
			print('Right Arrow Pressed')
		elif key == QtCore.Qt.Key_Down:
			if (self.direccion != "U"):
				self.direccion = "D"
			print('Down Arrow Pressed')

app = QtGui.QApplication(sys.argv)
window = servidorInterfaz()
sys.exit(app.exec_())