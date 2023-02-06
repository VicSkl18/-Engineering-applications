'''
 Através desse algoritmo é possível calcular os coeficientes de anisotropia de uma chapa metálica a 0°, 45° e 90°
em relação a direção de laminação, além disso também são calculados o os coeficientes de anisotropia normal e planar médio.
 Ademais, há também uma função que permite o usuário saber automaticamente a classificação de uma estampagem baseando-se
no gráfico do ensaio Erichsen inserindo apenas as medidas de espessura da chapa metálica e a profundidade do copo estampado em
milímetros.

Autor do código: Victor da Silva Teixeira
e-mail: unieviteixeira@fei.edu.br

Desenvolvido para a disciplina: Propriedades mecânicas dos materiais 
Professor da disciplina: Julio Cesar Dutra

Centro Universitário da FEI
'''
#================================================================================
#                                   Bibliotecas:
#================================================================================

from numpy import log as ln 
import numpy as np


#================================================================================
#                                   Seleção de ensaio:
#================================================================================

def selecao():

  print("="*80)
  print("ANISOTROPIA E ESTAMPABILIDADE".center(80))
  print("="*80)
  print("")
  print("[1] Anisotropia\n[2] Estampabilidade")
  print("")
  print("="*80)
  x = str(input("Qual você deseja? "))
  print("="*80)

  if x == '1':
    anisotropia()

  elif x == '2':
    estampabilidade()

  else:
    print("Insira apenas '1' ou '2'!!!")
    selecao()

#================================================================================
#                                   Anisotropia:
#================================================================================

def anisotropia():

  #Definindo as variáveis de entrada e declarando-as como globais
  global Li_0, Lf_0, wi_0, wf_0, Li_45, Lf_45, wi_45, wf_45, Li_90, Lf_90, wi_90, wf_90

  try:
    Li_0 = float(input("Comprimento incial [li] em 0°: " ))
    Lf_0 = float(input("Comprimento  [lf] em 0°: "))
    wi_0= float(input("Largura inicial [Wi] em 0°: "))
    wf_0 = float(input("Largura final [Wf] em 0°: "))
    print("")
    Li_45 = float(input("Comprimento incial [li] em 45°: " ))
    Lf_45 = float(input("Comprimento  [lf] em 45°: "))
    wi_45= float(input("Largura inicial [Wi] em 45°: "))
    wf_45 = float(input("Largura final [Wf] em 45°: "))
    print("")
    Li_90 = float(input("Comprimento incial [li] em 90°: " ))
    Lf_90 = float(input("Comprimento final [lf] em 90°: "))
    wi_90= float(input("Largura inicial [Wi] em 90°: "))
    wf_90 = float(input("Largura final [Wf] em 90°: "))
  
  except Exception as  erro:

    print('='*80)
    print("Um dos valores inseridos não é um número ou não é válido,\nnão será possível realizar os cálculos.\nInsira os valores novamente!")
    print('='*80)
    anisotropia()
  
  lista = [Li_0, Lf_0, wi_0, wf_0, Li_45, Lf_45, wi_45, wf_45, Li_90, Lf_90, wi_90, wf_90] #Lista que será usada para verificar se os valores de entrada são negativos 
  
  for i in lista:
    if i == 0:
      print('='*80)
      print("Um dos valores inseridos não é um número ou não é válido,\nnão será possível realizar os cálculos.\nInsira os valores novamente!")
      print('='*80)
      anisotropia()

  #Abstração das equações de anisotropia
  r_0 = ln(wf_0/wi_0)/ln((Li_0*wi_0)/(Lf_0*wf_0))        #Equação 1
  r_45 = ln(wf_45/wi_45)/ln((Li_45*wi_45)/(Lf_45*wf_45))
  r_90 = ln(wf_90/wi_90)/ln((Li_90*wi_90)/(Lf_90*wf_90))

  r = (r_0 + (2*r_45) + r_90)/4 #Equação 2

  Δr = (r_0 - (2*r_45) + r_90)/2 #Equação 3

  #Retrono dos resultados
  print('='*80)
  print("COEFICIENTES DE ANISOTROPIA".center(80))
  print('='*80)
  print("r_0° = {:.3f}\nr_45° = {:.3f}\nr_90° = {:.3f}".format(r_0, r_45, r_90))
  print('='*80)
  print("Anisotropia normal médio [r] = {:.3f}\nAnisotropia planar médio [Δr] = {:.3f}".format(r, Δr))
  print('='*80)
  
  #Chama a função que permite ao usuário decidir se quer voltar ao menu ou encerrar o programa 
  opcoes()

#================================================================================
#                                   Estampabilidade:
#================================================================================

def estampabilidade():
  #Definindo as variáveis de entrada e declarando-as como globais
  global t, d

  try:
    t = float(input("Insira a espessura da chapa [mm]: "))
    d = float(input("Insira a profundidade do copo [mm]: "))

    if t < 0 or d < 0:
        print('='*80)
        print("Um dos valores inseridos não é um número ou não é valido,\nnão será possível realizar os cálculos.\nInsira os valores novamente!")
        print('='*80)
        estampabilidade()
  
  except Exception as  erro:
    print('='*80)
    print("Um dos valores inseridos não é um número ou não é valido,\nnão será possível realizar os cálculos.\nInsira os valores novamente!")
    print('='*80)
    estampabilidade()

  #Abstração da análise do gráfico 
  QC_X = [0.501, 0.519, 0.535, 0.552, 0.568, 0.584, 0.6, 0.616, 0.632, 0.649, 0.665, 0.681, 0.697, 0.709, 0.716, 0.726, 0.734,
          0.742, 0.75, 0.761, 0.778, 0.786, 0.798, 0.811, 0.819, 0.829, 0.835, 0.847, 0.864, 0.88, 0.895, 0.913, 0.924, 0.932, 
          0.945, 0.958, 0.978, 0.993, 1.009, 1.021, 1.029, 1.04, 1.057, 1.076, 1.089, 1.102, 1.11, 1.122, 1.138, 1.156, 1.167, 
          1.188, 1.203, 1.223, 1.241, 1.254, 1.276, 1.289, 1.304, 1.316, 1.324, 1.337, 1.353, 1.366, 1.383, 1.397, 1.422, 1.436, 
          1.453, 1.466, 1.49, 1.505, 1.519, 1.535, 1.548, 1.565, 1.581, 1.596, 1.612, 1.62, 1.636, 1.652, 1.666, 1.683, 1.697, 1.715, 
          1.733, 1.749, 1.766, 1.778, 1.796, 1.812, 1.828, 1.844, 1.863, 1.877, 1.894, 1.907, 1.925, 1.94, 1.954, 1.972, 1.984, 1.992, 2]
  
  ArrQc = np.array(QC_X)
    
  QC_Y = [8.189,8.249,8.307,8.364,8.422,8.48,8.538,8.595,8.653,8.718,8.775,8.833,8.891,8.93,8.952,8.988,9.006,9.042,9.06,9.1,
          9.154,9.175,9.215,9.255,9.273,9.309,9.327,9.366,9.417,9.467,9.511,9.561,9.597,9.615,9.655,9.691,9.745,9.788,9.831,9.867,
          9.886,9.918,9.961,10.008,10.044,10.077,10.095,10.127,10.17,10.213,10.246,10.296,10.336,10.379,10.423,10.455,10.505,10.538,
          10.574,10.603,10.621,10.653,10.689,10.718,10.751,10.783,10.826,10.859,10.898,10.934,10.978,11.014,11.042,11.079,11.107,11.14,
          11.169,11.201,11.23,11.244,11.273,11.302,11.334,11.363,11.388,11.421,11.453,11.482,11.511,11.54,11.572,11.601,11.63,11.659,11.684,
          11.716,11.749,11.778,11.81,11.843,11.871,11.908,11.936,11.954,11.936]
  
  EM_X = [0.51,0.529,0.554,0.578,0.602,0.627,0.653,0.679,0.705,0.734,0.76,0.787,0.813,0.826,0.856,0.885,0.919,0.952,0.978,1.072,
          1.109,1.143,1.18,1.221,1.264,1.306,1.348,1.393,1.44,1.479,1.517,1.565,1.606,1.651,1.699,1.739,1.787,1.83,1.868,1.905]
  
  ArrEm = np.array(EM_X)

  EM_Y = [8.736,8.833,8.917,8.992,9.073,9.148,9.23,9.309,9.388,9.475,9.545,9.621,9.697,9.762,9.811,9.89,9.975,10.062,10.127,10.353,
          10.436,10.516,10.602,10.689,10.775,10.869,10.97,11.067,11.169,11.251,11.329,11.426,11.5,11.569,11.646,11.705,11.777,11.847,11.908,11.989] 
  
  EP_X = [0.507,0.525,0.546,0.581,0.616,0.654,0.694,0.723,0.75,0.782,0.816,0.853,0.89,0.929,0.964,0.996,1.034,1.065,1.128,1.164,1.205,1.242,1.271,
          1.313,1.358,1.401,1.446,1.49,1.534,1.574,1.614,1.657,1.701,1.744,1.776]
  
  ArrEp = np.array(EP_X)

  EP_Y = [9.105,9.201,9.28,9.379,9.487,9.575,9.681,9.789,9.886,9.969,10.051,10.136,10.245,10.324,10.404,10.492,10.558,10.642,10.78,10.847,10.931,
          11.008,11.094,11.212,11.299,11.367,11.441,11.516,11.584,11.678,11.765,11.821,11.866,11.932,11.972]


  v = busca_EEP(ArrEp, EP_Y, t, d)

  if v == 2:
    print('='*80)
    print("Essa é uma estampagem extra profunda (EEP).")
    print('='*80)
  
  else:
    v = busca_EP(ArrEm, EM_Y, ArrEp, EP_Y, t, d)
    if v == 2:
     print('='*80)
     print("Essa é uma estampagem profunda (EP).")
     print('='*80)
    
    else:
      v = busca_EM(ArrQc, QC_Y, ArrEm, EM_Y, t, d)
      if v == 2:
        print('='*80)
        print("Essa é uma estampagem média (EM).")
        print('='*80)
      
      else:
         v = busca_QC(ArrQc, QC_Y, t, d)
         if v == 2:
           print('='*80)
           print("Essa é uma estampagem de qualidade comercial (QC).")
           print('='*80)
        
         else:
           print('='*80)
           print("Os valores obtidos em seu ensaio não condizem nenhum com tipo de classificação")
           print('='*80)

  #Chama a função que permite ao usuário decidir se quer voltar ao menu ou encerrar o programa

    opcoes()

#================================================================================
#                                   Busca EPP:
#================================================================================

def busca_EEP(x, y, T, D):
  df_arr = np.absolute(x - T) 
  index = df_arr.argmin()
  n = 0

  if D > y[index] and D <= 12:
    n += 2
  
  return n

#================================================================================
#                                   Busca EP:
#================================================================================

def busca_EP(x1, y1, x2, y2, T, D):
  df_arr1 = np.absolute(x1 - T) 
  index1 = df_arr1.argmin()    
  df_arr2 = np.absolute(x2 - T)  
  index2 = df_arr2.argmin()
  n = 0

  if D > y1[index1]:
    n += 1
  if D < y2[index2]:    
    n += 1
  
  return n

#================================================================================
#                                   Busca EM:
#================================================================================

def busca_EM(x1, y1, x2, y2, T, D):
  df_arr1 = np.absolute(x1 - T)
  index1 = df_arr1.argmin()
  df_arr2 = np.absolute(x2 - T)
  index2 = df_arr2.argmin()
  n = 0
  
  if D > y1[index1]:
    n += 1
  if D < y2[index2]:    
    n += 1
  
  return n
  
#================================================================================
#                                   Busca QC:
#================================================================================

def busca_QC(x, y, T, D):
  df_arr = np.absolute(x - T) 
  index = df_arr.argmin()
  n = 0

  if D < y[index] and D >= 8:
    n += 2
  
  return n

#================================================================================
#               Opções: Calcular novamente ou encerrar o programa?
#================================================================================

def opcoes():
  print("[1] Menu\n[2] Encerrar o programa")
  print("="*80)
  x = str(input("Qual você deseja? "))

  if x == '1': 
    selecao()
  
  elif x == '2':
    print("="*80)
    print("PROGRAMA ENCERRADO".center(80))
    print("="*80)

  else:
    print("="*80)
    print("Insira apenas '1' ou '2'!!!")
    print("="*80)
    opcoes()

#================================================================================
#                                       Início:
#================================================================================

selecao()
