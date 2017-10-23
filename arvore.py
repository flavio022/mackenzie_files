class ArvoreBinBusca:
    class __No:
        def __init__(self,e):
            self.item = e
            self.pai = None
            self.direita = None
            self.esquerda = None

        def getItem(self):
             return self.item
        def getPai(self):
            return self.pai
        def getDireita(self):
            return self.direita
        def getEsquerda(self):
            return self.esquerda
        def setItem(self,e):
            self.item = e
        def setPai(self,e):
            self.pai = e
        def setEsquerda(self,e):
            self.esquerda = e
        def setDireita(self,e):
            self.direita = e
    
    def __init__(self):
        self.raiz = None
        return self.raiz == None
    def __setRaiz(self,n):
        self.raiz = e
    def __getRaiz(self):
        return self.raiz
    #Busca um elemento em uma arvore
    def busca(self,elem):
        resp = ArvoreBinBusca.__buscaElem(self.__getRaiz(),elem)
    
    @staticmethod
    def __buscaElem(n,elem):
        if n == None:
            return None
        elif elem == n.getItem():
            return n
        elif elem <= n.getItem():
            return ArvoreBinBusca.__buscaElem(n.getEsquerda(),elem)
        else:
            return ArvoreBinBusca.__buscaElem(n.getDireita(),elem)
   
    def consultaMenorValor(self):
        if self.eVazia():
            return None
        else:
            aux = self.__getRaiz()
            while aux.getEsquerda() !=None:
                aux = aux.getEsqueda()
            return aux.getItem()
   
    def ConsultaMenorRecursivo(self):
        if self.eVazia():
            return None
        else:
            return ArvoreBinBusca.__menorRecursivo(self.__getRaiz())
    @staticmethod
    def __menorRecursivo(n):
        if n.getEsquerda() == None
            return n.getItem()
        else:
            return ArvoreBinBusca.__menorRecursivo(n.getEsquerda())
    
    def consultaSoma_emOrdem(self):
        return ArvoreBinBusca.__somaEmOrdem(self.__getRaiz())

    @staticmethod
    def __somaEmOrdem(n):
        if n == None:
            return 0
        else:
            return ArvoreBinBusca.__somaEmOrdem(n.getEsquerda())+n.getItem()+ArvoreBinBusca.__somaEmOrdem(n.getDireita())