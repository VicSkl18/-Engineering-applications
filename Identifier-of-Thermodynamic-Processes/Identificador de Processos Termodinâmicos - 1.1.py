'''
Versão 1.1
Autor: Victor S. Teixeira
LinkedIn: https://www.linkedin.com/in/victor-s-teixeira-022a5717b
e-mail: unieviteixeira@fei.edu.br
'''


from numpy import log as ln
print("="*60)
print('''Ao inserir valores de pressão e volume 
digite-os em notação cientifífica!!!

Exemplo: Para 5.0x10^5 inserir 5.0e5
         Para 3.4x10^-3 inserir 3.4e-3''')

#Entrada de valores
print('='*60)
Pi = float(input("Insira o valor da pressão inicial (x10^5 Pa): "))
Pf = float(input("Insira o valor da pressão final (x10^5 Pa): "))
Vi = float(input("Insira o valor do volume inicial (x10^-3 m³): ")) 
Vf = float(input("Insira o valor do volume final (x10^-3 m³): "))
print('='*60)

#Variáveis auxiliares para os processos isobárico
Pt = Pf - Pi
Vt = Vf - Vi 

#Variáveis auxiliares para identificação do processo adiabático
P1 = Pi * (Vi ** 1.67)
P1 = round(P1, 3)
P2 = Pf * (Vf ** 1.67)
P2 = round(P2, 3)


#Identificando se é um processo isotérmico
if Pi * Vi == Pf * Vf or Pi * Vi <= Pf * Vf or Pi * Vi >= Pf * Vf  :
    if Pi * Vi <= Pf * Vf and ((100 * ((Pf * Vf) - (Pi * Vi)))/(Pf * Vf)) < 1:
        print("Processo termodinâmico: Isotérmico")     
        W = Pf * Vf * ln((Vf / Vi))
        Ei = 0
        print("W = {:.2f}J".format(W))
        print("Q = {:.2f}J".format(W))
        print("ΔEi =", Ei, "J")
        print('='*60)

    elif Pi * Vi >= Pf * Vf and ((100 * ((Pi * Vi) - (Pf * Vf)))/(Pi * Vi)) < 1:
        print("Processo termodinâmico: Isotérmico")     
        W = Pf * Vf * ln((Vf / Vi))
        Ei = 0
        print("W = {:.2f}J".format(W))
        print("Q = {:.2f}J".format(W))
        print("ΔEi =", Ei, "J")
        print('='*60)

    elif Pi * Vi == Pf * Vf:
        print("Processo termodinâmico: Isotérmico")     
        W = Pf * Vf * ln((Vf / Vi))
        Ei = 0
        print("W = {:.2f}J".format(W))
        print("Q = {:.2f}J".format(W))
        print("ΔEi =", Ei, "J")
        print('='*60)

#Identificando o processo adiabático
if P1 == P2 or P1 <= P2 or P1 >= P2:
    if P1 <= P2 and ((((100 *((P2 - P1))) / P2 )) < 1) and ((((100 *((P2 - P1))) / P2 )) > 0):
        print("Processo termodinâmico: Adiabático")
        W = (1/0.67) * ((Pi * Vi) - (Pf * Vf))
        Ei = -W
        print("W = {:.2f}J".format(W))
        print("Q =", 0, "J")
        print("ΔEi = {:.2f}J".format(Ei))
        print('='*60)

    elif P1 >= P2 and ((((100 *((P1 - P2))) / P1 )) < 1) and ((((100 *((P1 - P2))) / P1 )) > 0):
        print("Processo termodinâmico: Adiabático")
        W = ((Pi * Vi) - (Pf * Vf)) / 0.67
        Ei = -W
        print("W = {:.2f}J".format(W))
        print("Q =", 0, "J")
        print("ΔEi = {:.2f}J".format(Ei))
        print('='*60)
        
    elif P1 == P2:
        print("Processo termodinâmico: Adiabático")
        W = ((Pi * Vi) - (Pf * Vf)) / 0.67
        Ei = -W
        print("W = {:.2f}J".format(W))
        print("Q =", 0, "J")
        print("ΔEi = {:.2f}J".format(Ei))
        print('='*60)

#Identificando se é um processo isocórico
if Vi == Vf:

        print("Processo termodinâmico: Isocórico") 
        Q = (3/2) * (Pf - Pi) * Vf
        print("W = ", 0, "J")
        print("Q = {:.3f}J".format(Q))
        print("ΔEi = {:.3f}J".format(Q))
        print('='*60)

#Identificando se é um processo isobárico
if Pi == Pf:
    
        Pt = Pf
        print("Processo termodinâmico: Isobárico") 
        W = Pt * Vt 
        Q = (5/2) * W
        Ei = (3/2) * Pt * Vt 
        print("W = ", W, "J")
        print("Q =", Q, "J")
        print("ΔEi =", Ei, "J")
        print('='*60)
