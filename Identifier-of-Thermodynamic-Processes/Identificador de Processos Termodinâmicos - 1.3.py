#===================================================================================================#
'''
Versão 1.3
Autor: Victor S. Teixeira
LinkedIn: https://www.linkedin.com/in/victor-s-teixeira-022a5717b
e-mail: unieviteixeira@fei.edu.br

Sobre: 
Esse programa identifica qual processo termodinâmico ocorreu através dos dados 
de pressão e volume iniciais e finais e calcula os valores de trabalho(W), calor envolvido(Q)
e variação de energia interna(ΔEi).
Obs.: Essa é a atualização da versão 1.1 do programa. Agora é possível trabalhar com gases ideiais monoatômicos, diatômicos e poliatômicos.

Quaisquer dúvidas entre em contato com o desenvolvedor.
'''
#===================================================================================================#


#===========================BIBLIOTECA===========================#

from numpy import log as ln 


#===========================FUNÇÃO 1: IDENTIFICAÇÃO DOS PROCESSOS===========================#

def identifica_processo(gama, Pi, Pf, Vi, Vf):

    #VARIÁVEIS AUXILIARES: ISOBÁRICO

            Pt = Pf - Pi
            Vt = Vf - Vi 

    #VARIÁVEIS AUXILIARES: ADIABÁICO

            P1 = Pi * (Vi ** gama)
            P1 = round(P1, 3)
            P2 = Pf * (Vf ** gama)
            P2 = round(P2, 3)

    #CONDIÇÃO PARA DIFERENCIAR OS VALORES DE CP E CV COM BASE NO TIPO DE GÁS

            if gama == 1.67 or gama == 1.4 or gama == 1.33:
                if gama == 1.67:
                    cv = (3/2)
                    cp = (5/2)

                elif gama == 1.4:
                    cv = (5/2)
                    cp = (7/2)

                elif gama == 1.33:
                    cv = 3
                    cp = 4      
    
    #IDENTIFICAÇÃO: ISOTÉRMICO

            if Pi * Vi == Pf * Vf or Pi * Vi <= Pf * Vf or Pi * Vi >= Pf * Vf:

                if Pi * Vi <= Pf * Vf and ((100 * ((Pf * Vf) - (Pi * Vi)))/(Pf * Vf)) < 1:
                    print("Processo termodinâmico: Isotérmico")     
                    W = Pf * Vf * ln((Vf / Vi))
                    Q = W
                    Ei = 0
                    
                    

                elif Pi * Vi >= Pf * Vf and ((100 * ((Pi * Vi) - (Pf * Vf)))/(Pi * Vi)) < 1:
                    print("Processo termodinâmico: Isotérmico")     
                    W = Pf * Vf * ln((Vf / Vi))
                    Q = W
                    Ei = 0
                   
                    

                elif Pi * Vi == Pf * Vf:
                    print("Processo termodinâmico: Isotérmico")     
                    W = Pf * Vf * ln((Vf / Vi))
                    Q = W
                    Ei = 0
                    
                

    #IDENTIFICAÇÃO: ADIABÁTICO

            if P1 == P2 or P1 <= P2 or P1 >= P2:
                if P1 <= P2 and ((((100 *((P2 - P1))) / P2 )) < 1) and ((((100 *((P2 - P1))) / P2 )) > 0):
                    print("Processo termodinâmico: Adiabático")
                    W = (((Pi * Vi) - (Pf * Vf)) / (gama - 1))
                    Q = 0
                    Ei = -W
                    
                    

                elif P1 >= P2 and ((((100 *((P1 - P2))) / P1 )) < 1) and ((((100 *((P1 - P2))) / P1 )) > 0):
                    print("Processo termodinâmico: Adiabático")
                    W = (((Pi * Vi) - (Pf * Vf)) / (gama - 1))
                    Q = 0
                    Ei = -W
                    
                    
                elif P1 == P2:
                    print("Processo termodinâmico: Adiabático")
                    W = (((Pi * Vi) - (Pf * Vf)) / (gama - 1))
                    Q = 0
                    Ei = -W
                    
    
    #IDENTIFICAÇÃO: ISOCÓRICO

            if Vi == Vf:

                    print("Processo termodinâmico: Isocórico") 
                    W = 0
                    Q = cv * (Pf - Pi) * Vf
                    Ei = Q
                    

   #IDENTIFICAÇÃO: ISOBÁRICO

            if Pi == Pf:
                
                    Pt = Pf
                    print("Processo termodinâmico: Isobárico") 
                    W = Pt * Vt 
                    Q = cp * W
                    Ei = cv * Pt * Vt 

            return W, Q, Ei          


#===========================FUNÇÃO 2: VERIFICA SE O USUÁRIO QUER CONINUAR CALCULANDO===========================#

def calcular_novamente():
   print('''
[1] Fazer outro cálculo
[2] Encerrar calculadora
            ''') 
   print('='*60)
   RESP = str(input("Qual opção deseja ? "))

   while RESP not in ['1', '2']: 
        print("INSIRA APENAS '1' OU '2' !!!")
        RESP = input("Qual opção deseja ? ")
        
   return RESP         


#===========================PROGRAMA PRINCIPAL: LAÇO DE REPETIÇÃO===========================#

while True:

#INFORMAÇÕES

    print("="*60)
    print("\033[1m CÁLCULO E IDENTIFICAÇÃO DE PROCESSOS TERMODINÂMICOS \033[0m".center(65))
    print("="*60)
    print("\033[1;31mInserir os valores de pressão e\nvolume em notação científica!!!\033[0m")
    print("Exemplo:\nPara \033[1;32m5.0x10^5\033[0m inserir \033[1;32m5.0e5\033[0m\nPara \033[1;32m3.4x10^-3\033[0m inserir \033[1;32m3.4e-3\033[0m")
    print("="*60)
    print("Constante γ:")
    print("Monoatômico = 1.67\nDiatômico   = 1.4\nPoliatômico = 1.33")

#ENTRADA DE VALORES

    print('='*60)
    g = float(input("γ = "))
    pi   = float(input("Insira o valor da pressão inicial (x10^5 Pa): "))
    pf   = float(input("Insira o valor da pressão final (x10^5 Pa): "))
    vi   = float(input("Insira o valor do volume inicial (x10^-3 m³): ")) 
    vf   = float(input("Insira o valor do volume final (x10^-3 m³): "))
    print('='*60)

#RETORNO DOS VALORES CALCULADOS

    trabalho, calor, energia = identifica_processo(g, pi, pf, vi, vf)

    print("W = {:.3f}J".format(trabalho))
    print("Q = {:.3f}J".format(calor))
    print("ΔEi = {:.3f}J".format(energia))
    print('='*60)

#VERIFICA SE O USUÁRIO QUER OU NÃO CONTINUAR USANDO A CALCULADORA

    resposta = calcular_novamente()

    if resposta == '1':
        print('')

    elif resposta == '2':
        print('='*60)
        print("CALCULADORA ENCERRADA!!!")
        print('='*60)
        break    