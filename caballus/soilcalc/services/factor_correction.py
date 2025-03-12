#service/factor_correction


def calculate_factor(testemunha, valor_referencia):
#Fator de correção (leitura da testemunha/valor de referência #é um valor de entrada#) 
#Vai virar o fator de correção que multiplicará todos os valores de leitura da respectiva leitura
    factor = testemunha/valor_referencia
    return factor


