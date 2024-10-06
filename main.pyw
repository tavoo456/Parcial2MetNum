from PySide6.QtWidgets import *
from formulario import *    
from PySide6 import *
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
class MetodosNumericos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSuma.clicked.connect(self.sumar_matriz)
        self.ui.btnResta.clicked.connect(self.restar_matriz)
        self.ui.btnMultiplicar.clicked.connect(self.multiplicar_matriz)
        self.ui.btnMatrizInversa.clicked.connect(self.determinante)
        self.ui.btnMatrizInversa.clicked.connect(self.matriz_inversa)
        self.ui.btnSistemaDeEcuaciones.clicked.connect(self.sistema_ecuaciones)
        self.ui.btnIngresarN.clicked.connect(self.actualizar_tabla)
        self.ui.btnCalcularRegresion.clicked.connect(self.regresion_lineal)
        self.ui.btnLimpiarA.clicked.connect(self.limpiar_matrices_A)
        self.ui.btnLimpiarOM.clicked.connect(self.limpiar_matrices_OM)
        self.ui.btnLimpiarEQ.clicked.connect(self.limpiar_EQ)
        self.ui.btnLimpiarRegresion.clicked.connect(self.limpiar_regresion)
        self.center()
    
    #Esta función centra el form en la pantalla
    def center(self):
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        size = self.geometry()
        
        x = (screen_rect.width() - size.width()) / 2
        y = (screen_rect.height() - size.height()) / 2
        
        self.move(x, y)
    
    def inicializar_matriz(self, lista):
        for i in range(3):
            for j in range(3):
                lista.append([0]*3)
    
    def actualizar_tabla(self):
        numeroFilas = int(self.ui.txtN.text())
        self.ui.twIngresoDeDatos.setRowCount(numeroFilas)
        
        for fila in range(numeroFilas):
            for columna in range(2):
                self.ui.twIngresoDeDatos.setItem(fila, columna, QTableWidgetItem(""))
    
    def advertencia(self, msg):
        dialogo = QMessageBox()
        dialogo.setIcon(QMessageBox.Warning)
        dialogo.setWindowTitle("Advertencia")
        dialogo.setText(msg)
        dialogo.setStandardButtons(QMessageBox.Ok)
        dialogo.exec()
    
    def limpiar_matrices_A(self):
        for i in range(3):
            for j in range(3):
                getattr(self.ui, f'AA{i}{j}').setText("")
                getattr(self.ui, f'AB{i}{j}').setText("")
                getattr(self.ui, f'RS{i}{j}').setText("")
                getattr(self.ui, f'RR{i}{j}').setText("")
                getattr(self.ui, f'RM{i}{j}').setText("")
    
    def limpiar_matrices_OM(self):
        for i in range(3):
            for j in range(3):
                getattr(self.ui, f'AO{i}{j}').setText("")
                getattr(self.ui, f'RI{i}{j}').setText("")
    
    def limpiar_EQ(self):
        for i in range(3):
            getattr(self.ui, f'XEQ{i + 1}').setText("")
            getattr(self.ui, f'YEQ{i + 1}').setText("")
            getattr(self.ui, f'ZEQ{i + 1}').setText("")
            getattr(self.ui, f'IEQ{i + 1}').setText("")
        
        self.ui.lblX.setText("x = ")
        self.ui.lblY.setText("y = ")
        self.ui.lblZ.setText("z = ")
    
    def limpiar_regresion(self):
        self.ui.lblFormula.setText("y = ")
        self.ui.txtN.setText("")
        self.ui.lwRegresion.clear()
        self.ui.twIngresoDeDatos.setRowCount(0)
        self.ui.twRegresion.setRowCount(0)
    
    def sumar_matriz(self):
        a = []
        b = []
        c = []
        self.inicializar_matriz(a)
        self.inicializar_matriz(b)
        self.inicializar_matriz(c)
        
        
        for i in range(3):
            for j in range(3):
                a_txt = getattr(self.ui, f'AA{i}{j}').text().strip()
                b_txt = getattr(self.ui, f'AB{i}{j}').text().strip()
                
                if not a_txt or not b_txt:
                    self.advertencia("Campos vacíos, ingrese los datos correctamente")
                    return
                
                try:
                    a[i][j] = float(a_txt)
                    b[i][j] = float(b_txt)
                except Exception:
                    self.advertencia("Las matrices solo aceptan valores numéricos")
                    return
        
        for i in range(3):
            for j in range(3):
                c[i][j] = a[i][j] + b[i][j]
                getattr(self.ui, f'RS{i}{j}').setText(str(c[i][j]))
    
    def restar_matriz(self):
        a = []
        b = []
        c = []
        self.inicializar_matriz(a)
        self.inicializar_matriz(b)
        self.inicializar_matriz(c)
        
        
        for i in range(3):
            for j in range(3):
                a_txt = getattr(self.ui, f'AA{i}{j}').text().strip()
                b_txt = getattr(self.ui, f'AB{i}{j}').text().strip()
                
                if not a_txt or not b_txt:
                    self.advertencia("Campos vacíos, ingrese los datos correctamente")
                    return  
                
                try:
                    a[i][j] = float(a_txt)
                    b[i][j] = float(b_txt)
                except Exception:
                    self.advertencia("Las matrices solo aceptan valores numéricos")
                    return
        
        for i in range(3):
            for j in range(3):
                c[i][j] = a[i][j] + (-1) * b[i][j]
                getattr(self.ui, f'RR{i}{j}').setText(str(c[i][j]))
    
    def multiplicar_matriz(self):
        a = []
        b = []
        c = []
        self.inicializar_matriz(a)
        self.inicializar_matriz(b)
        self.inicializar_matriz(c)
        
        for i in range(3):
            for j in range(3):
                a_txt = getattr(self.ui, f'AA{i}{j}').text().strip()
                b_txt = getattr(self.ui, f'AB{i}{j}').text().strip()
                
                if not a_txt or not b_txt:
                    self.advertencia("Campos vacíos, ingrese los datos correctamente")
                    return  
                
                try:
                    a[i][j] = float(a_txt)
                    b[i][j] = float(b_txt)
                except Exception:
                    self.advertencia("Las matrices solo aceptan valores numéricos")
                    return
                
        
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    c[i][j] += a[i][k] * b[k][j]
                    getattr(self.ui, f'RM{i}{j}').setText(str(c[i][j]))
    
    #Funciones Para Calcular Matriz Inversa
    def determinante(self):
        a = []
        self.inicializar_matriz(a)
        
        for i in range(3):
            for j in range(3):
                a_txt = getattr(self.ui, f'AO{i}{j}').text().strip()
                
                if not a_txt:
                    return
                
                try:
                    a[i][j] = float(a_txt)
                except Exception:
                    self.advertencia("Las matrices solo aceptan valores numéricos")
                    return
        
        diagonales_principales = (
        a[0][0] * a[1][1] * a[2][2] +
        a[1][0] * a[2][1] * a[0][2] +
        a[2][0] * a[0][1] * a[1][2]
        )
        
        diagonales_secundarias = (
        a[0][2] * a[1][1] * a[2][0] +
        a[1][2] * a[2][1] * a[0][0] +
        a[2][2] * a[0][1] * a[1][0]
        )
        
        det = diagonales_principales -  diagonales_secundarias
        return det
    
    def matriz_inversa(self):
        a = []
        aC = []
        aCT = []
        mI = []
        self.inicializar_matriz(a)
        self.inicializar_matriz(aC)
        self.inicializar_matriz(aCT)
        self.inicializar_matriz(mI)
        
        for i in range(3):
            for j in range(3):
                a_txt = getattr(self.ui, f'AO{i}{j}').text().strip()
                
                if not a_txt:
                    self.advertencia("Campos vacíos, ingrese los datos correctamente")
                    return
                
                try:
                    a[i][j] = float(a_txt)
                except Exception:
                    self.advertencia("Las matrices solo aceptan valores numéricos")
                    return
        
        det = self.determinante()
        
        aC[0][0] = (a[1][1] * a[2][2]) - (a[2][1] * a[1][2])
        aC[0][1] = -((a[1][0] * a[2][2]) - (a[2][0] * a[1][2]))
        aC[0][2] = (a[1][0] * a[2][1]) - (a[2][0] * a[1][1])
        aC[1][0] = -((a[0][1] * a[2][2]) - (a[0][2] * a[2][1]))
        aC[1][1] = (a[0][0] * a[2][2]) - (a[2][0] * a[0][2])
        aC[1][2] = -((a[0][0] * a[2][1]) - (a[0][1] * a[2][0]))
        aC[2][0] = (a[0][1] * a[1][2]) - (a[1][1] * a[0][2])
        aC[2][1] = -((a[0][0] * a[1][2]) - (a[1][0] * a[0][2]))
        aC[2][2] = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
        
        for i in range(3):
            for j in range(3):
                aCT[i][j] = aC[j][i]
        
        for i in range(3):
            for j in range(3):
                mI[i][j] = round(aCT[i][j] / det, 2)
        
        for i in range(3):
            for j in range(3):
                getattr(self.ui, f'RI{i}{j}').setText(str(mI[i][j]))
    
    def sistema_ecuaciones(self):
        a = []
        aC = []
        aCT = []
        aI = [] 
        b = []
        c = []       
        self.inicializar_matriz(a)
        self.inicializar_matriz(aC)
        self.inicializar_matriz(aCT)
        self.inicializar_matriz(aI)
        
        for i in range(3):
            b.append([0]*3)
            c.append([0]*3)
        
        for i in range(3):
            X_txt = getattr(self.ui, f'XEQ{i + 1}').text().strip()
            Y_txt = getattr(self.ui, f'YEQ{i + 1}').text().strip()
            Z_txt = getattr(self.ui, f'ZEQ{i + 1}').text().strip()
            I_txt = getattr(self.ui, f'IEQ{i + 1}').text().strip()            
            
            if not X_txt or not Y_txt or not Z_txt:
                self.advertencia("Campos vacíos, ingrese los datos correctamente")
                return
            
            try:
                a[i][0] = float(X_txt)
                a[i][1] = float(Y_txt)
                a[i][2] = float(Z_txt)      
                c[i][0] = float(I_txt)
            except Exception:
                self.advertencia("En un sistema de ecuaciones lineales solo se aceptan valores numéricos")
                return
        
        diagonales_principales = (
        a[0][0] * a[1][1] * a[2][2] +
        a[1][0] * a[2][1] * a[0][2] +
        a[2][0] * a[0][1] * a[1][2]
        )
        
        diagonales_secundarias = (
        a[0][2] * a[1][1] * a[2][0] +
        a[1][2] * a[2][1] * a[0][0] +
        a[2][2] * a[0][1] * a[1][0]
        )
        
        det = diagonales_principales -  diagonales_secundarias
        
        aC[0][0] = (a[1][1] * a[2][2]) - (a[2][1] * a[1][2])
        aC[0][1] = -((a[1][0] * a[2][2]) - (a[2][0] * a[1][2]))
        aC[0][2] = (a[1][0] * a[2][1]) - (a[2][0] * a[1][1])
        aC[1][0] = -((a[0][1] * a[2][2]) - (a[0][2] * a[2][1]))
        aC[1][1] = (a[0][0] * a[2][2]) - (a[2][0] * a[0][2])
        aC[1][2] = -((a[0][0] * a[2][1]) - (a[0][1] * a[2][0]))
        aC[2][0] = (a[0][1] * a[1][2]) - (a[1][1] * a[0][2])
        aC[2][1] = -((a[0][0] * a[1][2]) - (a[1][0] * a[0][2]))
        aC[2][2] = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
        
        for i in range(3):
            for j in range(3):
                aCT[i][j] = aC[j][i]
        
        for i in range(3):
            for j in range(3):
                aI[i][j] = round(aCT[i][j] / det, 2)
        
        b[0][0] = round(aI[0][0] * c[0][0] + aI[0][1] * c[1][0] + aI[0][2] * c[2][0], 2)
        b[1][0] = round(aI[1][0] * c[0][0] + aI[1][1] * c[1][0] + aI[1][2] * c[2][0], 2)
        b[2][0] = round(aI[2][0] * c[0][0] + aI[2][1] * c[1][0] + aI[2][2] * c[2][0], 2)
        
        self.ui.lblX.setText("x = " + str(b[0][0]))
        self.ui.lblY.setText("y = " + str(b[1][0]))
        self.ui.lblZ.setText("z = " + str(b[2][0]))

    def regresion_lineal(self):
        self.ui.lblFormula.setText("y = ")
        self.ui.lwRegresion.clear()
        self.ui.twRegresion.setRowCount(0)
        
        x = []
        y = []
        media_x = [] 
        media_y = []
        media_x_cuadrado = []
        media_y_cuadrado = []
        multiplicacion_media = []
        x_cuadrado = []
        multiplicacion_xy = []
        n = self.ui.twIngresoDeDatos.rowCount()
        
        for i in range(n):
            x.append([0])
            y.append([0])
            media_x.append([0])
            media_y.append([0])
            media_x_cuadrado.append([0])
            media_y_cuadrado.append([0])
            multiplicacion_media.append([0])
            x_cuadrado.append([0])
            multiplicacion_xy.append([0])
        
        for fila in range(n):
            X_txt = self.ui.twIngresoDeDatos.item(fila, 0)
            Y_txt = self.ui.twIngresoDeDatos.item(fila, 1)
                
            if not X_txt.text() or not Y_txt.text():
                self.advertencia("Campos vacíos, ingrese los datos correctamente")
                return
            
            try:
                x[fila] = float(X_txt.text())
                y[fila] = float(Y_txt.text())
            except Exception:
                self.advertencia("Solo se aceptan valores numéricos, ingrese los datos correctamente")
                return
        
        suma_x = round(sum(x), 2)
        suma_y = round(sum(y), 2)
        promedio_x = round(suma_x / n, 2)
        promedio_y = round(suma_y / n, 2)
        
        for i in range(n):
            media_x[i] = round(x[i] - promedio_x, 2)
            media_y[i] = round(y[i] - promedio_y, 2)
            
            media_x_cuadrado[i] = round(media_x[i] ** 2, 2)
            media_y_cuadrado[i] = round(media_y[i] ** 2, 2)
            
            multiplicacion_media[i] = round(media_x[i] * media_y[i],2)
        
        suma_media_x_cuadrado = round(sum(media_x_cuadrado) ,2)
        suma_media_y_cuadrado = round(sum(media_y_cuadrado), 2)
        suma_multiplicacion_media = round(sum(multiplicacion_media), 2)
        
        desviacion_estandar_x = round(math.sqrt(suma_media_x_cuadrado / n), 2)
        desviacion_estandar_y = round(math.sqrt(suma_media_y_cuadrado / n), 2)
        covarianza = round(suma_multiplicacion_media / n, 2)
        r = round(covarianza / (desviacion_estandar_x * desviacion_estandar_y), 2)
        
        if r>0:
            for i in range(n):
                x_cuadrado[i] = x[i] ** 2
                multiplicacion_xy[i] = round(x[i] * y[i], 2)
            
            suma_x_cuadrado = sum(x_cuadrado)
            suma_multiplicacion_xy = round(sum(multiplicacion_xy), 2)
            
            a = round(((n * suma_multiplicacion_xy) - (suma_x * suma_y)) / ((n * suma_x_cuadrado) - (suma_x ** 2)), 2)
            b = round(promedio_y - a * promedio_x, 2)
            
            self.ui.twRegresion.setColumnCount(9)
            self.ui.twRegresion.setHorizontalHeaderLabels(["X", "Y", "x - x̅", "y - y̅", "(x - x̅)²", "(y - y̅)²", "(x - x̅)(y - y̅)", "x²", "x*y"])
            self.ui.twRegresion.setRowCount(n)
            
            for i in range(n):
                self.ui.twRegresion.setItem(i, 0, QTableWidgetItem(str(x[i])))
                self.ui.twRegresion.setItem(i, 1, QTableWidgetItem(str(y[i])))
                self.ui.twRegresion.setItem(i, 2, QTableWidgetItem(str(media_x[i])))
                self.ui.twRegresion.setItem(i, 3, QTableWidgetItem(str(media_y[i])))
                self.ui.twRegresion.setItem(i, 4, QTableWidgetItem(str(media_x_cuadrado[i])))
                self.ui.twRegresion.setItem(i, 5, QTableWidgetItem(str(media_y_cuadrado[i])))
                self.ui.twRegresion.setItem(i, 6, QTableWidgetItem(str(multiplicacion_media[i])))
                self.ui.twRegresion.setItem(i, 7, QTableWidgetItem(str(x_cuadrado[i])))
                self.ui.twRegresion.setItem(i, 8, QTableWidgetItem(str(multiplicacion_xy[i])))
            
            self.ui.lwRegresion.addItem("∑x = " + str(suma_x))
            self.ui.lwRegresion.addItem("∑y = " + str(suma_y))
            self.ui.lwRegresion.addItem("x̅ = " + str(promedio_x))
            self.ui.lwRegresion.addItem("y̅ = " + str(promedio_y))
            self.ui.lwRegresion.addItem("∑(x - x̅)² = " + str(suma_media_x_cuadrado))
            self.ui.lwRegresion.addItem("∑(y - y̅)² = " + str(suma_media_y_cuadrado))
            self.ui.lwRegresion.addItem("∑(x - x̅)(y - y̅) = " + str(suma_multiplicacion_media))
            self.ui.lwRegresion.addItem("")
            self.ui.lwRegresion.addItem("Sx = " + str(desviacion_estandar_x))
            self.ui.lwRegresion.addItem("Sy = " + str(desviacion_estandar_y))
            self.ui.lwRegresion.addItem("Sxy = " + str(covarianza))
            self.ui.lwRegresion.addItem("r = " + str(r) + ", HAY correlación lineal")
            self.ui.lwRegresion.addItem("")
            self.ui.lwRegresion.addItem("∑x² = " + str(suma_x_cuadrado))
            self.ui.lwRegresion.addItem("∑x*y = " + str(suma_multiplicacion_xy))
            
            self.ui.lblFormula.setText("Fórmula: y = " + str(a) + "*x + (" + str(b) + ")")
            
            x_recta = np.linspace(min(x), max(x), 100)
            y_recta = a * x_recta + b
            
            plt.plot(x_recta, y_recta, color = 'red', label = f'Recta de regresión: y = {a}x + {b}')
            
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Puntos y recta de regresión')
            
            plt.legend()            
            plt.show() 
        else:
            self.ui.twRegresion.setColumnCount(7)
            self.ui.twRegresion.setHorizontalHeaderLabels(["X", "Y", "x - x̅", "y - y̅", "(x - x̅)²", "(y - y̅)²", "(x - x̅)(y - y̅)"])
            self.ui.twRegresion.setRowCount(n)
            
            for i in range(n):
                self.ui.twRegresion.setItem(i, 0, QTableWidgetItem(str(x[i])))
                self.ui.twRegresion.setItem(i, 1, QTableWidgetItem(str(y[i])))
                self.ui.twRegresion.setItem(i, 2, QTableWidgetItem(str(media_x[i])))
                self.ui.twRegresion.setItem(i, 3, QTableWidgetItem(str(media_y[i])))
                self.ui.twRegresion.setItem(i, 4, QTableWidgetItem(str(media_x_cuadrado[i])))
                self.ui.twRegresion.setItem(i, 5, QTableWidgetItem(str(media_y_cuadrado[i])))
                self.ui.twRegresion.setItem(i, 6, QTableWidgetItem(str(multiplicacion_media[i])))
            
            self.ui.lwRegresion.addItem("∑x = " + str(suma_x))
            self.ui.lwRegresion.addItem("∑y = " + str(suma_y))
            self.ui.lwRegresion.addItem("x̅ = " + str(promedio_x))
            self.ui.lwRegresion.addItem("y̅ = " + str(promedio_y))
            self.ui.lwRegresion.addItem("∑(x - x̅)² = " + str(suma_media_x_cuadrado))
            self.ui.lwRegresion.addItem("∑(y - y̅)² = " + str(suma_media_y_cuadrado))
            self.ui.lwRegresion.addItem("∑(x - x̅)(y - y̅) = " + str(suma_multiplicacion_media))
            self.ui.lwRegresion.addItem("")
            self.ui.lwRegresion.addItem("Sx = " + str(desviacion_estandar_x))
            self.ui.lwRegresion.addItem("Sy = " + str(desviacion_estandar_y))
            self.ui.lwRegresion.addItem("Sxy = " + str(covarianza))
            self.ui.lwRegresion.addItem("r = " + str(r) + ", NO hay correlación lineal")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MetodosNumericos() 
    myapp.show()
    sys.exit(app.exec())