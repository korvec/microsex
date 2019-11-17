import sys

from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtGui import QPixmap, QColor, QFont
from PyQt5.QtCore import Qt

from FUN.CONF.HojaEstilos import stylesheet

estilo = stylesheet()
fuente = QFont("Calibri", 12)
fuente.setBold(True)

modulos = [
'Unidad Básica de Cálculo',
'Unidad Aritmética Lógica',
'Unidad Secuencial de Cálculo',
'USC con Memoria de Datos']

class PanelInicialWidget(QWidget):

    def __init__(self):
        super().__init__()

        Logo = QPixmap("IMG/LOGO_GRANDE.png")

        self.logo_inicial = QLabel(self)
        self.logo_inicial.setPixmap(Logo)
        self.logo_inicial.setAlignment(Qt.AlignCenter)

        self.boton_seleccion = QPushButton("Módulos de entrenamiento", self)    # Debe tener formato de botón
        self.boton_seleccion.clicked.connect(self.seleccion_modulos)
        self.boton_seleccion.setStyleSheet(estilo["estilo_boton_inicio"])
        self.boton_seleccion.setFont(fuente)

        self.combo_seleccion = QComboBox(self)
        self.combo_seleccion.addItems(modulos)
        self.combo_seleccion.setEnabled(False)
        self.combo_seleccion.setStyleSheet(estilo["estilo_combo_box"])
        self.combo_seleccion.setFont(fuente)

        self.boton_aceptar = QPushButton("Aceptar", self)
        self.boton_aceptar.setEnabled(False)
        self.boton_aceptar.setStyleSheet(estilo["estilo_boton_inicio"])
        self.boton_aceptar.setFont(fuente)

        self.boton_cancelar = QPushButton("Cancelar", self)
        self.boton_cancelar.setEnabled(False)
        self.boton_cancelar.setStyleSheet(estilo["estilo_boton_inicio"])
        self.boton_cancelar.setFont(fuente)
        self.boton_cancelar.clicked.connect(self.funciones_principales)

        bloque_botones_aceptar = QHBoxLayout()
        bloque_botones_aceptar.addStretch(1)
        bloque_botones_aceptar.addWidget(self.boton_aceptar)
        bloque_botones_aceptar.addWidget(self.boton_cancelar)
        bloque_botones_aceptar.addStretch(1)

        self.boton_cc = QPushButton("Computador Completo", self)               # Debe tener formato de botón
        self.boton_cc.setStyleSheet(estilo["estilo_boton_inicio"])
        self.boton_cc.setFont(fuente)

        txtDMRJ = """Por: Diego Marcelo Ramírez Jove
https://github.com/korvec/microsex
2019
"""

        # DMRJ = QLabel('Por: Diego Marcelo Ramírez Jove\n2019\n', self)
        DMRJ = QLabel(txtDMRJ,self)
        DMRJ.setAlignment(Qt.AlignCenter)

        bloque_inicial = QVBoxLayout()
        bloque_inicial.addWidget(self.logo_inicial)
        bloque_inicial.addStretch(1)
        bloque_inicial.addWidget(self.boton_seleccion)
        bloque_inicial.addWidget(self.combo_seleccion)
        bloque_inicial.addLayout(bloque_botones_aceptar)
        bloque_inicial.addWidget(self.boton_cc)
        bloque_inicial.addStretch(1)
        bloque_inicial.addWidget(DMRJ)

        self.setLayout(bloque_inicial)

    def seleccion_modulos(self):

        self.boton_seleccion.setEnabled(False)
        self.combo_seleccion.setEnabled(True)
        self.boton_cc.setEnabled(False)

        self.boton_aceptar.setEnabled(True)
        self.boton_cancelar.setEnabled(True)

    def funciones_principales(self):

        self.boton_seleccion.setEnabled(True)
        self.combo_seleccion.setEnabled(False)
        self.boton_cc.setEnabled(True)

        self.boton_aceptar.setEnabled(False)
        self.boton_cancelar.setEnabled(False)
