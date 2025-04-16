#Cálculo das células pertecentes a cálculos escondidos 
from soilcalc.services.factor_correction import calculate_factor
import math


#AC19(MO) - Para batelada Testemunha (Mesma para a batelada do Branco)
def calculaMo(valorMO):
    if valorMO == None:
        return None
    
    try:
        valorMO = float(valorMO)
        resultado = (43.5 - 9.5 * math.log(valorMO)) * 1.8
        return resultado
    
    except ValueError:
        return None



#AD18(P) - Batelada Branco
def calculaP_branco(bateladaP_branco, testemunha, valor_referencia):
    
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = ((bateladaP_branco * factor * 50 * 10) / (25))
        return resultado
    except:
        return None


#AD19(P) - Para Batelada Testemunha
def calculaP(bateladaP_branco,batelada_valor, testemunha, valor_referencia):
    
    factor = calculate_factor(testemunha, valor_referencia)
    if batelada_valor == None:
        return None
    try:
        resultado = (((batelada_valor - bateladaP_branco) * factor * 50 * 10) / (25))
        return resultado
    except:
        return None
    


#AE18(K) - Batelada Branco
def calculaK_branco(bateladaK_branco, testemunha, valor_referencia):
    
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = ((bateladaK_branco * factor * (50/5)) * (20))
        return resultado
    except:
        return None



#AE19(K) - Para Batelada Testemunha
def calculaK(bateladaK_branco, batelada_valor, testemunha, valor_referencia):
    
    factor = calculate_factor(testemunha, valor_referencia)
    if batelada_valor == None:
        return None
    try:
        resultado = (((batelada_valor - bateladaK_branco) * factor * (50/5)) * (20))
        return resultado
    except:
        return None
    
    
    
#AF18(Na) - Para Batelada Branco    
def calculaNa_branco(bateladaNa_branco, testemunha, valor_referencia):
    
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = (((bateladaNa_branco * factor)(50*5))/230)
        return resultado
    except:
        return None
    
    
#AF18(Na) - Para Batelada Testemunha    
def calculaNa(bateladaNa_branco, batelada_valor, testemunha, valor_referencia):
    
    factor = calculate_factor(testemunha, valor_referencia)
    if batelada_valor == None:
        return None
    try:
        resultado = ((((batelada_valor - bateladaNa_branco) * factor)*(50*5))/230)
        return resultado
    except:
        return None
   
    
#AG18(Ca) - Para Batelada Branco
def calculaCa_branco(bateladaCa_branco):    
    try:
        resultado = ((bateladaCa_branco * (50*10))/(5*1*200))
        return resultado
    except:
        return None



#AG19(Ca) - Para Batelada Testemunha
def calculaCa(bateladaCa_branco, batelada_valor ):    
    try:
        resultado = (((batelada_valor - bateladaCa_branco) * (50*10))/(5*1*200))
        return resultado
    except ValueError:
        return None
    



#AH18(Mg) - Para Batelada Branco
def calculaMg_branco(bateladaMg_branco):    
    try:
        resultado = ((bateladaMg_branco * (50*10))/(5*1*120))
        return resultado
    except:
        return None
    
    
    
    
#AH19(Mg) - Para Batelada Testemunha
def calculaMg(bateladaMg_branco, batelada_valor):    
    try:
        resultado = (((batelada_valor - bateladaMg_branco) * (50*10))/(5*1*120))
        return resultado
    except:
        return None




#AI18(Al) - Para Batelada Branco
def calculaAl_branco(bateladaAl_branco):    
    try:
        resultado = ((bateladaAl_branco * (0.025*50*100))/(25*5))
        return resultado
    except:
        return None
  
  
    
    
#AI19(Al) - Para Batelada Testemunha
def calculaAl(bateladaAl_branco, batelada_valor):    
    try:
        resultado = (((batelada_valor - bateladaAl_branco) * (0.025*50*100))/(25*5))
        return resultado
    except:
        return None
   
   
    
    
#NÃO EXISTE BATELADA BRANCO PARA H+Al

#AJ19(H+Al) - Para Batelada Testemunha
def calculaHAl(batelada_valor):    
    try:
        resultado = 2.73**(8.062906 - 1.111044*batelada_valor)
        return resultado
    except:
        return None
    
    
    
#AK18(B) - Para Batelada Branco
def calculaB_branco(bateladaB_branco,testemunha, valor_referencia):
    
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = ((bateladaB_branco * factor * 20 * 6)/(10 * 4))
        return resultado
    except:
        return None



#AK19(B) - Para Batelada Testemunha
def calculaB(bateladaB_branco, batelada_valor, testemunha, valor_referencia):
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = (((batelada_valor - bateladaB_branco) * factor * 20 * 6)/(10 * 4))
        return resultado
    except:
        return None



#AL18(Cu) - Para Batelada Branco
def calculaCu_branco(bateladaCu_branco):
    try:
        resultado = (bateladaCu_branco * 10)
        return resultado
    except:
        return None

#AL19(Cu) - Para Batelada Testemunha
def calculaCu(bateladaCu_branco, batelada_valor):
    try:
        resultado = ((batelada_valor - bateladaCu_branco) * 10)
        return resultado
    except:
        return None
    
    
    
#AM18(Fe) - Para Batelada Branco
def calculaFe_branco(bateladaFe_branco):
    try:
        resultado = (bateladaFe_branco * 10)
        return resultado
    except:
        return None



#AM19(Fe) - Para Batelada Testemunha
def calculaFe(bateladaFe_branco, batelada_valor):
    try:
        resultado = ((batelada_valor - bateladaFe_branco) * 10)
        return resultado
    except:
        return None
    
    
    
#AN18(Mn) - Para Batelada Branco
def calculaMn_branco(bateladaMn_branco):
    try:
        resultado = (bateladaMn_branco * 10)
        return resultado
    except:
        return None
    
    
    
#AN19(Mn) - Para Batelada Testemunha
def calculaMn(bateladaMn_branco, batelada_valor):
    try:
        resultado = ((batelada_valor - bateladaMn_branco) * 10)
        return resultado
    except:
        return None
    
    
    
    
#AO18(Zn) - Para Batelada Branco  
def calculaZn_branco(bateladaZn_branco):
    try:
        resultado = (bateladaZn_branco * 10)
        return resultado
    except:
        return None



#AO19(Zn) - Para Batelada Testemunha
def calculaZn(bateladaZn_branco, batelada_valor):
    try:
        resultado = ((batelada_valor - bateladaZn_branco) * 10)
        return resultado
    except:
        return None
    
    
    
#AP18(S) - Para Batelada Branco
def calculaS_branco(bateladaS_branco, testemunha, valor_referencia):
    
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = (bateladaS_branco * factor * 2,5)
        return resultado
    except:
        return None
    
    
    
#AP19(S) - Para Batelada Testemunha
def calculaS(bateladaS_branco, batelada_valor, testemunha, valor_referencia):
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = ((batelada_valor - bateladaS_branco) * factor * 2,5)
        return resultado
    except:
        return None
    
    
#AQ18(Prem) - Para Batelada Branco
def calculaPrem_branco(batelada_branco, testemunha, valor_referencia):
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = batelada_branco * factor * 40
        return resultado
    except:
        return None
    
    
#AQ19(Prem) - Para Batelada Testemunha
def calculaPrem(batelada_branco, batelada_valor, testemunha, valor_referencia):
    factor = calculate_factor(testemunha, valor_referencia)
    try:
        resultado = ((batelada_valor - batelada_branco) * factor * 40)
        return resultado
    except:
        return None
    
    
#AR18(C_eletrica) - Para Batelada Branco


#AS18(Areia) - Para Batelada Branco
def calculaAreia_branco(argila, becker02, argSilte, becker01, tipo):
    if tipo == "branco":
        try:
            resultado = 100 - (calculaArgila(argila, becker02, tipo) + calculaSilte(argSilte, becker01, argila, becker02, tipo))
            return resultado
        except:
            return None
    else:
        try:
            resultado = 100 - (calculaArgila(argila, becker02, tipo) + calculaSilte(argSilte, becker01, argila, becker02, tipo))
            return resultado
        except:
            return 0
    



#AT18(Argila) - Para Batelada Branco
def calculaArgila(argila, becker02,tipo):
    if tipo == "branco":
        try:
            resultado = (argila - becker02) * 100 *20
            return resultado
        except:
            return None
    else:
        try:
            resultado = (argila - becker02) * 200
            return resultado
        except:
            return 0
    



#AU18(Silte) - Para Batelada Branco
def calculaSilte(argSilte, becker01, argila, becker02, tipo):
    if tipo == "branco":
        try:
            resultado = (((argSilte - becker01) - (argila - becker02)) * 100) * 10
            return resultado
        except:
            return None
    else:
        try:
            resultado = (((argSilte - becker01) - (argila - becker02)) * 200)
            return resultado
        except:
            return 0
    
    


