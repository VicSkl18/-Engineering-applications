#Versão 1.0


from numpy import log as ln

#Entrada de valores
print('='*60)
Pi = float(input("Insira o valor da pressão inicial (x10^5 Pa): "))
Pf = float(input("Insira o valor da pressão final (x10^5 Pa): "))
Vi = float(input("Insira o valor do volume inicial (x10^-3 m³): "))
Vf = float(input("Insira o valor do volume final (x10^-3 m³): "))
print('='*60)

#Variáveis auxiliares
Pt = Pf - Pi
Vt = Vf - Vi 

#Variáveis auxiliares para identificação do processo adiabático
P1 = ((Pi *(10**5)) * ((Vi * (10 ** -3)) ** 1.67))
P1 = round(P1)
P2 = ((Pf *(10**5)) * ((Vf * (10 ** -3)) ** 1.67))
P2 = round(P2)
print(P1)
print(P2)

#Identificando se é um processo isobárico
if Pt == Pf or Pt == -Pi or Pt == 0:
    if Pt == - Pi:
        Pt = Pi
        print("Esse é um processo isobárico!") 
        W = (Pt * (10**5)) * (Vt * (10 ** -3))
        Q = (5/2) * (Pt * (10**5))
        Ei = (3/2) * (Pt * (10**5)) * (Vt * (10 ** -3))
        print("W = ", W)
        print("Q =", Q)
        print("ΔEi =", Ei)
        print('='*60)

    else:
        Pt = Pf
        print("Esse é um processo isobárico!") 
        W = (Pt * (10**5)) * (Vt * (10 ** -3))
        Q = (5/2) * (Pt * (10**5)) * (Vt * (10 ** -3))
        Ei = (3/2) * (Pt * (10**5)) * (Vt * (10 ** -3))
        print("W = ", W, "J")
        print("Q =", Q, "J")
        print("ΔEi =", Ei, "J")
        print('='*60)

#Identificando se é um processo isotérmico
elif Pi * Vi == Pf * Vf:
    print("Esse é um processo isotérmico!")     
    W = ((Pf * (10**5)) * (Vf * (10 ** -3))) * ln((Vf * (10 ** -3)) / (Vi * (10 ** -3)))
    Ei = 0
    print("W = {:.2f}J".format(W))
    print("Q = {:.2f}J".format(W))
    print("ΔEi =", Ei, "J")
    print('='*60)

#Identificando se é um processo isocórico
elif Vt == Vf or Vt == -Vi or Vt == 0:
    if Vt == - Vi:
        Vt = Vi
        print("Esse é um processo isocórico!") 
        Q = (3/2) * ((Pf - Pi) * (10 ** 5)) * Vt
        print("W = ", 0, "J")
        print("Q = {:.2f}J".format(Q))
        print("ΔEi = {:.2f}J".format(Q))
        print('='*60)

    else:
        Vt = Vf
        print("Esse é um processo isocórico!") 
        Q = (3/2) * ((Pf - Pi) * (10 ** 5)) * (Vt *(10 ** -3))
        print("W = ", 0, "J")
        print("Q = {:.2f}J".format(Q))
        print("ΔEi = {:.2f}J".format(Q))
        print('='*60)

#Identificando o processo adiabático
elif P1 == P2:
    print("Esse é um processo adiabático!")
    W = (1/0.67) * (((Pi *(10 ** 5)) * (Vi *(10 ** -3))) - ((Pf *(10 ** 5)) * (Vf *(10 ** -3))))
    Ei = -W
    print("W = {:.2f}J".format(W))
    print("Q =", 0, "J")
    print("ΔEi = {:.2f}J".format(Ei))
    print('='*60)
