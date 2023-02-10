import Fd

class Fp:
    def __init__(self):
        self.F1 = Fd.Fd()
        self.F2 = Fd.Fd()
        self.F3 = Fd.Fd()
        self.F4 = Fd.Fd()
        
    def inserir (self,valor,p):
        if p == 1:
            self.F1.inserir(valor)

        elif p == 2:
            self.F2.inserir(valor)

        elif p == 3:
            self.F3.inserir(valor)

        else:
            self.F4.inserir(valor)

    def remover (self,valor):
        if p == 1:
            self.f1.remover(valor)
            
