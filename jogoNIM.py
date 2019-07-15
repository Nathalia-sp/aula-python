def partida():
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    print()
    if (n>=m and n%(m+1)!=0):
        print("Computador começa!")
        print()
        computador_escolhe_jogada(n,m)
    else:
        print("Você começa!")
        print()
        usuario_escolhe_jogada(n,m)

def computador_escolhe_jogada(n,m):
    opcao=1
    n=n-opcao
    if (n!=0 and n%(m+1)!=0 and (n+1)%m!=0 or n+1==m):
        if(n+1>=m):
            opcao=m
        else:
            opcao=n+1
        n=n+1-opcao
        if (opcao==1):
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou",opcao,"peças.")
        if (n!=0):
            print("Agora restam",n,"peças no tabuleiro.")
            usuario_escolhe_jogada(n,m)
        else:
            print ("Fim do jogo! O computador ganhou!")
    else:
        print("O computador tirou uma peça.")
        if (n!=0):
            print("Agora restam",n,"peças no tabuleiro.")
            print()
            usuario_escolhe_jogada(n,m)
        else:
            print("Fim do jogo! O computador ganhou!")
                
                
    


def usuario_escolhe_jogada(n,m):
    opcao_usuario=int(input("Quantas peças você vai tirar? "))
    while(opcao_usuario>m):
        print()
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        opcao_usuario=int(input("Quantas peças você vai tirar? "))
    if (opcao_usuario==1):
        print()
        print( "Você tirou uma peça.")
    else:
        print("Você tirou",opcao_usuario,"peças.")
    n=n-opcao_usuario
    if (n==1):
        print("Agora resta apenas uma peça no tabuleiro.")
    else:
        print("Agora restam",n,"peças no tabuleiro.")
        print()
    computador_escolhe_jogada(n,m)


def campeonato():
    num_partida=0
    while (num_partida!=3):
        num_partida=num_partida +1
        print("**** Rodada ",num_partida, "****")
        partida()
        print()
    print("Placar: Você 0 X 3 Computador")



def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    escolha = int(input("1 - para jogar uma partida isolada ou 2 para jogar um campeonato "))
    if (escolha==1):
        print()
        print("Você escolheu uma partida isolada!")
        print()
        partida()
    else:
        print()
        print("Você escolheu um campeonato!")
        print()
        campeonato()
                
                
    
    
    
    
    
        
    
                
    
            
            
        
    
        
        
