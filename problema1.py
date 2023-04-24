'''
Un banco necesita controlar el acceso a cuentas bancarias y para ello desea hacer un programa de prueba en Java que permita lanzar procesos que ingresen y retiren dinero a la vez y comprobar así si el resultado final es el esperado.

Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100 euros, 50 o 20. También se pueden tener procesos que retiran 100, 50 o 20 euros euros. Se desean tener los siguientes procesos:

40 procesos que ingresan 100

20 procesos que ingresan 50

60 que ingresen 20.

De la misma manera se desean lo siguientes procesos que retiran cantidades.

40 procesos que retiran 100

20 procesos que retiran 50

60 que retiran 20.

Se desea comprobar que tras la ejecución la cuenta tiene exactamente 100 euros, que era la cantidad de la que se disponía al principio.
'''
from multiprocessing import Pool
import time

class Cuenta():
    def __init__(self):
        self.dinero = 100
       
        
    def ingresar(self, dato):
        self.dinero = self.dinero + dato
        
    
    def retirar(self, cantidad):
        self.dinero = self.dinero - cantidad
        

def cliente(proc, dinero, func):
    pool = Pool(processes=proc)  
    pool.map(func, dinero)
    pool.close()
    
    time.sleep(2)  

if __name__ == '__main__':
    d1 = 100
    d2 = 50
    d3 = 20
    c = Cuenta()
    cliente(40, d1, c.ingresar)
    cliente(20, d2, c.ingresar)
    cliente(60, d3, c.ingresar)
    cliente(40, d1, c.retirar)
    cliente(20, d2, c.retirar)
    cliente(60, d3, c.retirar)
    print(f'El dinero total es {c.dinero}')