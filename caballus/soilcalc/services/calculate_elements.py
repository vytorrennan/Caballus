#Cálculo das células pertecentes a cálculos escondidos 
import math


#AC19(MO) - Para batelada Testemunha (Mesma para a batelada do Branco)
def calculate_mo(valorMO):
    if valorMO == None:
        return None
    
    try:
        valorMO = float(valorMO)
        resultado = (43.5 - 9.5 * math.log(valorMO)) * 1.8
        return resultado
    
    except ValueError:
        return None



#AD18(P) - Batelada Branco
def calculaP_branco(bateladaP_branco,fatorP_branco):
    try:
        resultado = ((bateladaP_branco * fatorP_branco * 50 * 10) / (25))
        return resultado
    except:
        return None

#AD19(P) - Para Batelada Testemunha
def calculate_P(fatorP_branco, bateladaP_branco,batelada_valor):
    if batelada_valor == None:
        return None
    try:
        resultado = (((batelada_valor - bateladaP_branco) * fatorP_branco * 50 * 10) / (25))
        return resultado
    except:
        return None
    

#AE18(K) - Batelada Branco
def calculaK_branco(bateladaK_branco,fatorK_branco):
    try:
        resultado = ((bateladaK_branco * fatorK_branco * (50/5)) * (20))
        return resultado
    except:
        return None


#AE19(K) - Para Batelada Testemunha
def calculate_P(fatorK_branco, bateladaK_branco,batelada_valor):
    if batelada_valor == None:
        return None
    try:
        resultado = (((batelada_valor - bateladaK_branco) * fatorK_branco * (50/5)) * (20))
        return resultado
    except:
        return None