import utilitario as ut

listaRH = []
listaCONT = []
listaTI = []
listaSEC = []
opc = 0
while opc==0:

    matricula = str(input('MATRICULA: '))
    nome = str(input('NOME: '))
    email = str(input('EMAIL: '))
    telefone = str(input('TELEFONE: '))
    celular = str(input('CELULAR: '))
    endereco = str(input('ENDEREÇO: '))
    numero = str(input('NUMERO: '))
    bairro = str(input('BAIRRO: '))
    cidade = str(input('CIDADE: '))
    uf = str(input('UF: '))
    complemento = str(input('COMPLEMENTO:'))
    if len(complemento) == 0:
        complemento = 'SEM COMPLEMENTO'
    cargo = str(input('CARGO: '))
    salario = str(input('SALÁRIO: '))
    while ut.valida_salario(salario)==False:
        print("Favor inserir o salário!")
        salario = str(input('SALÁRIO: '))
        ut.valida_salario(salario)
    setor = str(input('SETOR: \n 1 - RH\n 2 - CONTABILIDADE\n 3 - TI\n 4 - SECRETARIA'))
    if setor == "1":
        salario = float(salario)
        listaRH.append(salario)


    elif setor == "2":
        salario = float(salario)
        listaCONT.append(salario)


    elif setor == "3":
        salario = float(salario)
        listaTI.append(salario)


    elif setor == "4":
        salario = float(salario)
        listaSEC.append(salario)

    inss = str(ut.calculo_salario(salario)[0])
    irrf = str(ut.calculo_salario(salario)[1])
    salario_liquido = str(ut.calculo_salario(salario)[2])

    ut.armazenar(matricula, nome, email, telefone, celular, endereco, numero, bairro, cidade, uf, complemento, cargo,
                 salario, inss, irrf, salario_liquido)

    opcao=input("Deseja cadastrar mais funcionários? 1-Sim, 2 -Não")
    if opcao == "2":
        opc = 1
    else:
        opc = 0





mostrar = str(input('DESEJA EXIBIR [S/N]:'))
if mostrar in 'sS':
    ut.exibir()
    print("Custo setorial:", "\nRH:", ut.custo_setorial(listaRH), "\nContabilidade:", ut.custo_setorial(listaCONT), "\nTI", ut.custo_setorial(listaTI),"\nSecretaria", ut.custo_setorial(listaSEC))
else:
    print('END')

