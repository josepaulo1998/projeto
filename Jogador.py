class jogador():
    
    def __init__(self): 
        
        self.nome = None
        self.token = None
        #self.token1 = "X"
        #self.token2 = "O"
    #EXIXTIU UM EXERCICIO NUMA FICHA QUE FIZEMOS ISTO PROCURA XD
    def tokens(self):
        while True: #Ciclo para não deixa o utilizador colocar qualquer outro caracter sem ser o pretendido
            self.token = input("Qual o token que deseja usar [X]:[O]:")
            if self.token == self.token.upper():#Se o self.token  não for == a maiusculas 
                if self.token == "O" or self.token == "X":
                    return self.token
                    break # para acabar com o ciclo
            else: 
                print("Introduza apenas maiusculas para o programa entender") # < faz este pint

print("Dados do Jogador 1") 
jogador1 = jogador()
jogador1.nome = input("Qual é o seu nome:")
jogador1.tokens() 
 

print("Dados do jogador 2:")
jogador2 = jogador()
jogador2.nome = input("Nome do jogador 2:")
if jogador1.token == "O":
    jogador2.token = "X"
else:
    jogador2.token = "O" 

print("O jogador {} escolheu [{}], {} vais ter de ficar com o [{}]".format(jogador1.nome, jogador1.token, jogador2.nome, jogador2.token))

















'''
print("jogador1:{}".format(jogador1.nome)) #ver maneira de aparecer os dois juntos
print("jogador1:{}".format(jogador2.nome)) #ver maneira de aparecer os dois juntos
'''

