from PySide6.QtWidgets import *
from formulario import *    
from PySide6 import *
import sys

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
        self.ui.btnLimpiarA.clicked.connect(self.limpiar_matrices_A)
        self.ui.btnLimpiarOM.clicked.connect(self.limpiar_matrices_OM)
        self.ui.btnLimpiarEQ.clicked.connect(self.limpiar_EQ)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MetodosNumericos() 
    myapp.show()
    sys.exit(app.exec())