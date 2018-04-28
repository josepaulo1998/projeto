class tabuleiro():
    
    def __init__(self):
        self.token = None
        self.jogo = [[[] for i in range(3)] for i in range(3)]
        self.linha = None
        self.coluna = None

    def linha1(self):
        self.coluna = input("Qual a posição nessa linha, A, B ou C:") 
        if self.coluna == "A": 
            self.jogo[0][0].append(self.token)
            if self.token in self.jogo:
                print("teste") 
        elif self.coluna == "B":
            self.jogo[0][1].append(self.token) #
        elif self.coluna == "C":
            self.jogo[0][2].append(self.token)
        else:
            print("teste")
        
        for listas in self.jogo:
            print()
            for elementos in listas:
                print(elementos, end="")
       
        
    def linha2(self):
        self.coluna = input("Qual a posição nessa linha, A, B ou C:")
       
        if self.coluna == "A":
            self.jogo[1][0].append("X") 
        elif self.coluna == "B":
            self.jogo[1][1].append("X")
        elif self.coluna == "C":
            self.jogo[1][2].append("X") 
        
       
        for listas in self.jogo:          
            print()
            for elementos in listas:
                print(elementos, end="")
                      

    def linha3(self):
        self.coluna = input("Qual a posição nessa linha, A, B ou C:")
        
        if self.coluna == "A":
            self.jogo[2][0].append("X")
        elif self.coluna == "B":
            self.jogo[2][1].append("X")
        elif self.coluna == "C":
            self.jogo[2][2].append("X")
        
        
        for listas in self.jogo:
            print()
            for elementos in listas:
                print(elementos, end="")
        

    

jogada = tabuleiro()
jogada.token = input("token:")
while True:
    jogada.linha = int(input("Qual a linha em que queres jogar 1, 2, 3:"))
    

    if jogada.linha == 1:
        jogada.linha1()
    elif jogada.linha == 2:
        jogada.linha2()
    elif jogada.linha == 3:
        jogada.linha3()