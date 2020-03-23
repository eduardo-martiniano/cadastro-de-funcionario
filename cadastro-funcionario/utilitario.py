def valida_salario(salario):
    if salario.isalpha():
        return False
    else:
        return True

def custo_setorial(x):
    total =sum(x)
    return total


def calculo_salario(salario):
    salario_bruto = float(salario)
    inss = 0
    if salario_bruto <= 1693.72:
        inss = salario_bruto * 0.08
    elif salario_bruto > 1693.72 and salario_bruto <= 2822.90:
        inss = salario_bruto * 0.09
    elif salario_bruto > 2822.90 and salario_bruto <= 5645.80:
        inss = salario_bruto * 0.11
    elif salario_bruto > 5645.80:
        inss = 621.04
    irrf = 0
    if salario_bruto < 1903.98:
        irrf = 0
    elif salario_bruto > 1903.98 and salario_bruto < 2826.66:
        irrf = salario_bruto * 0.075
    elif salario_bruto >= 2826.66 and salario_bruto < 3751.06:
        irrf = salario_bruto * 0.15
    elif salario_bruto >= 3751.06 and salario_bruto < 4664.69:
        irrf = salario_bruto * 0.225
    elif salario_bruto >= 4664.69:
        irrf = salario_bruto * 0.275
    salario_liquido = salario_bruto - (irrf + inss)
    return inss, irrf, salario_liquido


def armazenar(matricula,nome,email,telefone,celular,endereco,numero,bairro,cidade,uf,complemento,cargo,salario,inss,irrf,salario_liquido):

    arquivo = open("teste.txt", "a")
    arquivo.write("\nMATRICULA: " + matricula)
    arquivo.write("\nNOME: " + nome)
    arquivo.write("\nEMAIL: " + email)
    arquivo.write("\nTELEFONE: " + telefone)
    arquivo.write("\nCELULAR: " + celular)
    arquivo.write("\nENDEREÇO: " + endereco)
    arquivo.write("\nNUMERO: " + numero)
    arquivo.write("\nBAIRRO: " + bairro)
    arquivo.write("\nCIDADE: " + cidade)
    arquivo.write("\nUF: " + uf)
    arquivo.write("\nCOMPLEMEMTO: " + complemento)
    arquivo.write("\nCARGO: " + cargo)
    arquivo.write("\nSALARIO: " + str(salario))
    arquivo.write("\nINSS: " + inss)
    arquivo.write("\nIRRF: " + irrf)
    arquivo.write("\nSALARIO LIQUIDO: " + salario_liquido)
    arquivo.close()


def exibir():
    arquivo = open("teste.txt", "r")
    texto = arquivo.read()
    print(texto)
    arquivo.close()