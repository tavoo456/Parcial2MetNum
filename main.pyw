from PySide6.QtWidgets import *
from formulario import *    
from PySide6 import *
import sys

class MetodosNumericos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.btnCalcularBiseccion.clicked.connect(self.biseccion)
        self.ui.btnSuma.clicked.connect(self.sumarMatriz)
        self.ui.btnResta.clicked.connect(self.restarMatriz)
        self.ui.btnMultiplicar.clicked.connect(self.multiplicarMatriz)
        self.ui.btnMatrizInversa.clicked.connect(self.determinante)
        self.ui.btnMatrizInversa.clicked.connect(self.matrizInversa)
        self.center()
    
    #Esta función centra el form en la pantalla
    def center(self):
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        size = self.geometry()
        
        x = (screen_rect.width() - size.width()) / 2
        y = (screen_rect.height() - size.height()) / 2
        
        self.move(x, y)
    
    def InicializarMatriz(self, lista):
        for i in range(3):
            for j in range(3):
                lista.append([0]*3)
    
    def sumarMatriz(self):
        a = []
        b = []
        c = []
        self.InicializarMatriz(a)
        self.InicializarMatriz(b)
        self.InicializarMatriz(c)
        
        for i in range(3):
            for j in range(3):
                a[i][j] = float(getattr(self.ui, f'AA{i}{j}').text())
                b[i][j] = float(getattr(self.ui, f'AB{i}{j}').text())
        
        # a[0][0] = float(self.ui.AA00.text())
        # a[0][1] = float(self.ui.AA01.text())
        # a[0][2] = float(self.ui.AA02.text())
        # a[1][0] = float(self.ui.AA10.text())
        # a[1][1] = float(self.ui.AA11.text())
        # a[1][2] = float(self.ui.AA12.text())
        # a[2][0] = float(self.ui.AA20.text())
        # a[2][1] = float(self.ui.AA21.text())
        # a[2][2] = float(self.ui.AA22.text())
        # for i in range(3):
        #     for j in range(3):
        #         a[i][j] = float(self.ui.AA00.text())
        
        for i in range(3):
            for j in range(3):
                c[i][j] = a[i][j] + b[i][j]
                getattr(self.ui, f'RS{i}{j}').setText(str(c[i][j]))
            
        
        for i in range(3):
            print('[', end=' ')
            for j in range(3):
                print(a[i][j], end='  ')
            print(']')
            print(' ')
        
        for i in range(3):
            print('[', end=' ')
            for j in range(3):
                print(b[i][j], end='  ')
            print(']')
            print(' ')
    
    def restarMatriz(self):
        a = []
        b = []
        c = []
        self.InicializarMatriz(a)
        self.InicializarMatriz(b)
        self.InicializarMatriz(c)
        
        validar = True
        
        for i in range(3):
            for j in range(3):
                a_txt = getattr(self.ui, f'AA{i}{j}').text().strip()
                b_txt = getattr(self.ui, f'AB{i}{j}').text().strip()
                if not a_txt or not b_txt:
                    self.Advertencia()
                    return  
                a[i][j] = float(a_txt)
                b[i][j] = float(b_txt)
        
        if(validar):
            for i in range(3):
                for j in range(3):
                    c[i][j] = a[i][j] + (-1) * b[i][j]
                    getattr(self.ui, f'RR{i}{j}').setText(str(c[i][j]))
    
    def Advertencia(self):
        dialogo = QMessageBox()
        dialogo.setIcon(QMessageBox.Warning)
        dialogo.setWindowTitle("Advertencia")
        dialogo.setText("Complete todos los campos")
        dialogo.setStandardButtons(QMessageBox.Ok)
        dialogo.exec() 

    
    def multiplicarMatriz(self):
        a = []
        b = []
        c = []
        self.InicializarMatriz(a)
        self.InicializarMatriz(b)
        self.InicializarMatriz(c)
        
        for i in range(3):
            for j in range(3):
                a[i][j] = float(getattr(self.ui, f'AA{i}{j}').text())
                b[i][j] = float(getattr(self.ui, f'AB{i}{j}').text())
        
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    c[i][j] += a[i][k] * b[k][j]
                    getattr(self.ui, f'RM{i}{j}').setText(str(c[i][j]))
    
    #Funciones Para Calcular Matriz Inversa
    #Determinante
    def determinante(self):
        a = []
        self.InicializarMatriz(a)
        
        for i in range(3):
            for j in range(3):
                a[i][j] = float(getattr(self.ui, f'AO{i}{j}').text())
        
        diagonales_principales = (
        a[0][0] * a[1][1] * a[2][2] +
        a[1][0] * a[2][1] * a[0][2] +
        a[2][0] * a[0][1] * a[1][2]
        )
        
        # Diagonales secundarias
        diagonales_secundarias = (
        a[0][2] * a[1][1] * a[2][0] +
        a[1][2] * a[2][1] * a[0][0] +
        a[2][2] * a[0][1] * a[1][0]
        )
        
        det = diagonales_principales -  diagonales_secundarias
        print(det)
        return det
    
    def matrizInversa(self):
        a = []
        aC = []
        aCT = []
        mI = []
        self.InicializarMatriz(a)
        self.InicializarMatriz(aC)
        self.InicializarMatriz(aCT)
        self.InicializarMatriz(mI)
        
        det = self.determinante()
        
        for i in range(3):
            for j in range(3):
                a[i][j] = float(getattr(self.ui, f'AO{i}{j}').text())
        
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
                mI[i][j] = aCT[i][j] / det
        
        for i in range(3):
            print('[', end=' ')
            for j in range(3):
                print(aC[i][j], end='  ')
            print(']')
            print(' ')
        
        for i in range(3):
            print('[', end=' ')
            for j in range(3):
                print(aCT[i][j], end='  ')
            print(']')
            print(' ')
        
        for i in range(3):
            print('[', end=' ')
            for j in range(3):
                print(mI[i][j], end='  ')
            print(']')
            print(' ')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MetodosNumericos() 
    myapp.show()
    sys.exit(app.exec())