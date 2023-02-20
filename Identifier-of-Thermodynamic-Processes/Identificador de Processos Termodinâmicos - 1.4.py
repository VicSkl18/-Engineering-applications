#===================================================================================================#
'''
Versão 1.4
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

#==============================================BIBLIOTECA============================================#


from numpy import log as ln 
import plotly.express as pl



#===========================FUNÇÃO 0: IDENTIFICAR SE O USUÁRIO TEM OU NÃO VALOR DE GAMA===========================#
def valor_gama():
    x = str(input('Você tem o valor de gama [S/N]? ')).strip().upper()
    
    while x not in 'SsNn':
        print("Responda apenas com 'S' par sim ou 'N' para não!!!")
        x = str(input('Você tem o valor de gama [S/N]? '))

    if x == 'S':
        n = 0
        return n

    elif x == 'N':   
        n = 1 
        return n

#===========================FUNÇÃO 1: ENTRADA DE VALORES(COM O VALOR DE GAMA)===========================#

def entrada_de_valores_com_gama():
    
#ENTRADA DE VALORES

    print('='*60)
    g = float(input("γ = "))
    pi   = float(input("Insira o valor da pressão inicial: "))
    pf   = float(input("Insira o valor da pressão final: "))
    vi   = float(input("Insira o valor do volume inicial: ")) 
    vf   = float(input("Insira o valor do volume final: "))
    print('='*60)

#RETORNO DOS VALORES CALCULADOS

    trabalho, calor, energia = identifica_processo(g, pi, pf, vi, vf)

    print("W = {:.3f}J".format(trabalho))
    print("Q = {:.3f}J".format(calor))
    print("ΔEi = {:.3f}J".format(energia))
    print('='*60)

#GRÁFICO

    dd_x = [vi, vf]
    dd_y = [pi, pf]

    img = pl.line(x = dd_x, y = dd_y, title = "DIAGRAMA PxV", height = 400, width = 400, line_shape = 'spline')
    img.show()

#VERIFICA SE O USUÁRIO QUER OU NÃO CONTINUAR USANDO A CALCULADORA

    resposta = calcular_novamente()
    return resposta

#===========================FUNÇÃO 2: IDENTIFICAÇÃO DOS PROCESSOS (COM O VALOR DE GAMA)===========================#

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
                 

    #IDENTIFICAÇÃO: ISOCÓRICO

            if Vi == Vf:

                    print("Processo termodinâmico: Isocórico") 
                    W = 0
                    Q = cv * (Pf - Pi) * Vf
                    Ei = Q
                    

   #IDENTIFICAÇÃO: ISOBÁRICO

            elif Pi == Pf:
                
                    Pt = Pf
                    print("Processo termodinâmico: Isobárico") 
                    W = Pt * Vt 
                    Q = cp * W
                    Ei = cv * Pt * Vt 

#ANÁLISE: ISOTÉRMICO OU ADIABÁTICO?

            E_adi, Erro_isot = erro_percentual(P1, P2, Pi, Vi, Pf, Vf)
            
            if (Pi * Vi <= Pf * Vf) or (Pi * Vi >= Pf * Vf) or (P1 <= P2) or (P1 >= P2):

               if E_adi <= 10 or Erro_isot <= 10: 
               
                                    
                #ERRO PERCENTUAL: RESULTADOS
                  print("ADIABÁTICO: PERCENTUAL DE ERRO PiVi^γ = PfVf^γ: {:.5f}%".format(E_adi))
                  print("ISOTÉRMICO: PERCENTUAL DE ERRO Pi.Vi = Pf.Vf: {:.5f}%".format(Erro_isot))
                  print()
                  print("Com  base nesses dados qual é o processo?")
                  print()
                  resp1 = isotermico_ou_adiabatico() 

                  if resp1 == '1':

                    #IDENTIFICAÇÃO: ADIABÁTICO

                        print("Processo termodinâmico: Adiabático")
                        W = (((Pi * Vi) - (Pf * Vf)) / (gama - 1))
                        Q = 0
                        Ei = -W
                 
                  if resp1 == '2':             
                                
                    #IDENTIFICAÇÃO: ISOTÉRMICO

                        print("Processo termodinâmico: Isotérmico")     
                        W = Pf * Vf * ln((Vf / Vi))
                        Q = W
                        Ei = 0

     
            return W, Q, Ei          

#===========================FUNÇÃO 3: ENTRADA DE VALORES(SEM O VALOR DE GAMA)===========================#

    #EM DESENVOLVIMENTO
'''
def entrada_de_valores_sem_gama():
    
    print('='*60)
    pi   = float(input("Insira o valor da pressão inicial: "))
    pf   = float(input("Insira o valor da pressão final: "))
    vi   = float(input("Insira o valor do volume inicial: ")) 
    vf   = float(input("Insira o valor do volume final: "))
    print('='*60)

    P = (pi/pf)
    V = (vf/vi)

    gama = ln(P) / ln(V)

    print("γ = {:.2f}".format(gama))

    #RETORNO DOS VALORES CALCULADOS

    trabalho, calor, energia = identifica_processo(gama, pi, pf, vi, vf)

    print("W = {:.3f}J".format(trabalho))
    print("Q = {:.3f}J".format(calor))
    print("ΔEi = {:.3f}J".format(energia))
    print('='*60)

    #VERIFICA SE O USUÁRIO QUER OU NÃO CONTINUAR USANDO A CALCULADORA

    resposta = calcular_novamente()
    return resposta
'''

#===========================FUNÇÃO 4: VERIFICA SE O USUÁRIO QUER CONINUAR CALCULANDO===========================#

def calcular_novamente():

   print('''
[1] Fazer outro cálculo
[2] Encerrar calculadora
            ''') 
   print('='*60)

   RESP = str(input("Qual opção deseja? "))

   while RESP not in ['1', '2']: 

        print("INSIRA APENAS '1' OU '2' !!!")
        RESP = input("Qual opção deseja? ")
        
   return RESP         
#===========================FUNÇÃO 5: VERIFICA SE O USUÁRIO SELECIONOU O ISOTÉRMICO OU ADIABÁTICO===========================#
def isotermico_ou_adiabatico():
    
    print('''
[1] Adiabáico
[2] Isotérmico
            ''') 
    print('='*60)

    RESP = str(input("Qual opção deseja? "))

    print('='*60)

    while RESP not in ['1', '2']: 

        print("INSIRA APENAS '1' OU '2' !!!")
        RESP = input("Qual opção deseja? ")
        print('='*60)

    return RESP         

#===========================FUNÇÃO 6: CALCULA O PERCENTUAL DE ERRO PARA ISOTÉRMICO E ADIABÁTICO===========================#

def erro_percentual(p1, p2, PI, VI, PF, VF):

    #PERCENUAL DE ERRO: ADIABÁTICO
    
    if p1 >  p2:

        maior1 = p1 
        menor1 = p2
    
    elif p1 < p2:

        maior1 = p2  
        menor1 = p1  

    else:

        maior1 = p1
        menor1 = p2     

    Erro1 = (100 *((maior1 - menor1))) / maior1

    #PERCENTUAL DE ERRO: ISOTÉRMICO
    
    PV1 = PI * VI
    PV2 = PF * VF
    
    if  PV1 > PV2:

        maior2 = PV1
        menor2 = PV2
    
    elif  PV1 < PV2:

        maior2 = PV2
        menor2 = PV1
   
    else:

        maior2 = PV1
        menor2 = PV2

    Erro2 = (100 *((maior2 - menor2))) / maior2

    return Erro1, Erro2


#===========================PROGRAMA PRINCIPAL: LAÇO DE REPETIÇÃO===========================#

while True:

#INFORMAÇÕES

    print("="*60)
    print("\033[1m CÁLCULO E IDENTIFICAÇÃO DE PROCESSOS TERMODINÂMICOS \033[0m".center(65))
    print("="*60)
    print("\033[1;31mEm algumas situações é melhor inserir os\nvalores de pressão e volume em notação científica!!!\033[0m")
    print("Exemplo:\nPara \033[1;32m5.0x10^5 Pa\033[0m inserir \033[1;32m5.0e5\033[0m\nPara \033[1;32m3.4x10^-3 m³\033[0m inserir \033[1;32m3.4e-3\033[0m")
    print("="*60)
    print("Constante γ:")
    print("Monoatômico = 1.67\nDiatômico   = 1.4\nPoliatômico = 1.33")
    print("="*60)

    vg = valor_gama()

    if vg == 0:
        r_f1 = entrada_de_valores_com_gama()
        
        if r_f1 == '1':
            print('')

        elif r_f1 == '2':
            print('='*60)
            print("CALCULADORA ENCERRADA!!!")
            print('='*60)
            break

'''
    if vg == 1:
        r_f2 = entrada_de_valores_sem_gama()
'''
