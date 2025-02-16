def organizador_aritmetico(problemas, mostrar_respostas=False):
    #1 - Limitar quantidade de problemas

    if len(problemas) > 5:
        return 'Erro: Muitos problemas, limite é 5.'

    #Operadores devem ser apenas '+' ou '-'
    operadores = []

    for problema in problemas:
        
        operador = problema.split()
        operadores.append(operador[1])

    for operador in operadores:
        if operador in ['*','/']:
            return "Erro: Operador deve ser '+' or '-'."
    #numeros so podem ter digitos
    numeros = []

    for problema in problemas:
        
        problema = problema.split()
        numeros.append(problema[0])
        numeros.append(problema[2])

    for numero in numeros:
        if not numero.isdigit():
            return 'Erro: Apenas digitos são permitidos.'

    #Numeros so podem no maximo 4 digitos

    for numero in numeros:
        if len(numero) > 4:
           return 'Erro: São permitidos no máximo 4 digitos.'

    #mostrar a operação
    resposta = []
    linha_sup = ''
    linha_inf = ''
    linha_resposta = ''
    dashes = ''

    for problema in problemas:
        operation = problema.split()
        conta = ''.join(operation)    
        resultado = eval(conta)
        resposta.append(resultado)
    

    
    for i in range (0, len(numeros), 2):
        operador = operadores[i // 2]
        space = max(len(numeros[i]), len(numeros[i + 1])) + 2
        linha_sup += numeros[i].rjust(space)
        linha_inf +=  operador + numeros[i + 1].rjust(space - 1)
        
        dashes += '-' * space
        # espaço entre as operações
        if i != len(numeros) - 2:
            linha_sup += ' ' * 4
            linha_inf += ' ' * 4
            dashes += ' ' * 4

    for i in range(len(resposta)):
        space = max(len(numeros[i * 2]), len(numeros[i * 2 + 1])) + 2
        linha_resposta += str(resposta[i]).rjust(space)

        if i != len(resposta) - 1:
            linha_resposta += ' ' * 4
  
    if mostrar_respostas:
        resposta_final = '\n'.join((linha_sup,linha_inf,dashes,linha_resposta))
    else:
        resposta_final = '\n'.join((linha_sup,linha_inf,dashes))

    return resposta_final
print(f'\n{organizador_aritmetico(["3801 - 2", "123 + 49"], True)}')



