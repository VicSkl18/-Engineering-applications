import numpy as np


def fluido():
    print('='*85)
    print("CALCULADORA DE EMPUXO".center(85))
    print('='*85)
    print("DADOS DO FLUIDO".center(85))
    print('='*85)

    try:
        g = float(input("Qual o peso específico específico do fluído? ɣ (N/m³) = "))

    except Exception as error:
        print("="*85)
        print("O valor inserido não é válido,\nnão será possível realizar os cálculos.\nInsira o valor novamente!")
        print("="*85)
        fluido()

    corpo(g)


def corpo(G):
    print('='*85)
    print("DADOS DO CORPO".center(85))
    print('='*85)
    print('''O corpo é cilindrico, piramidal, cônico ou paralelepípedo? 

 [1] Cilindrico
 [2] Piramidal
 [3] Cônico
 [4] Paralelepípedo
''')

    print('='*85)
    opt = int(input("Qual você deseja? "))

    while opt not in [1, 2, 3, 4]:
        print('='*85)
        print("Responda apenas com as funções apresentadas!")
        print("="*85)
        opt = int(input("Qual você deseja? "))

    if opt == 1:
        cld(G)

    elif opt == 2:
        pmd(G)

    elif opt == 3:
        cnc(G)

    elif opt == 4:
        plp(G)


def cld(g):

    print('='*85)

    try:
        h = float(input("Qual a altura do corpo? h (m) = "))
        d = float(input("Qual o diâmetro da base do corpo? Ø (m) = "))

    except Exception as error:
        print("="*85)
        print("Um dos valores inseridos não é válido,\nnão será possível realizar os cálculos.\nInsira os valores novamente!")
        print("="*85)
        cld(g)

    vl = ((np.pi*d**2)/4)*h
    e = g * vl
    print("="*85)
    print("Empuxo (E) = {:.3f}N".format(e))
    print("="*85)

    calcular_novamente()


def pmd(g):

    print('='*85)

    try:
        h = float(input("Qual a altura do corpo? h (m) = "))
        a = float(input("Qual a área da base do corpo? a (m²) = "))

    except Exception as error:
        print("="*85)
        print("Um dos valores inseridos não é válido,\nnão será possível realizar os cálculos.\nInsira os valores novamente!")
        print("="*85)
        pmd(g)

    vl = (a*h)/3
    e = g * vl
    print("="*85)
    print("Empuxo (E) = {:.3f}N".format(e))
    print("="*85)

    calcular_novamente()


def cnc(g):

    print('='*85)

    try:
        h = float(input("Qual a altura do corpo? h (m) = "))
        d = float(input("Qual o diâmetro da base do corpo? a (m²) = "))

    except Exception as error:
        print("="*85)
        print("Um dos valores inseridos não é válido,\nnão será possível realizar os cálculos.\nInsira os valores novamente!")
        print("="*85)
        pmd(g)

    vl = ((np.pi*(d/2)**2)*h)/3
    e = g * vl
    print("="*85)
    print("Empuxo (E) = {:.3f}N".format(e))
    print("="*85)

    calcular_novamente()


def plp(g):

    print('='*85)

    try:
        h = float(input("Qual a altura do corpo? h (m) = "))
        a = float(input("Qual a área da base do corpo? a (m²) = "))

    except Exception as error:
        print("="*85)
        print("Um dos valores inseridos não é válido,\nnão será possível realizar os cálculos.\nInsira os valores novamente!")
        print("="*85)
        pmd(g)

    vl = (a*h)/3
    e = g * vl
    print("="*85)
    print("Empuxo (E) = {:.3f}N".format(e))
    print("="*85)

    calcular_novamente()


def calcular_novamente():

    print('''
[1] Calcular novamente
[2] Encerrar programa
            ''')
    print("="*85)

    RESP = str(input("Qual opção deseja? "))

    while RESP not in ['1', '2']:

        print("Insira apenas '1' OU '2' !!!")
        RESP = input("Qual opção deseja? ")

    if RESP == '1':
        print("="*85)
        fluido()

    elif RESP == '2':
        print("="*85)
        print("CALCULADORA ENCERRADA")
        print("="*85)


fluido()
