integrantes = [
    { "nome": "Rodrigo Lima Nogueira Santos", "RGM": 37031376 },
    { "nome": "Felype Reinaldo Alves de Lira", "RGM": 37273264},
    { "nome": "João Paulo dos Santos Moscardi", "RGM": 38229064},
    { "nome": "Guilherme Pereira Franco da Silva", "RGM": 37369644},
    { "nome": "Wanderson Gabriel Matos da Silva", "RGM": 37070851},
]

opcoesMenus = [
    "Converter de Decimal para Binário",
    "Converter de Decimal para Hexadecimal",
    "Converter de Decimal para Octadecimal",
    "Converter de Binário para Decimal",
    "Converter de Hexadecimal para Decimal",
    "Converter de Octadecimal para Decimal",
    "Encerrar sistema"
]

def printLine(printSpcae = False):
    print("------------------------------------------------------")

    if printSpcae:
        print()

def printIntegrantes():
    printLine()
    print("Seja bem vindo ao nosso sistema de conversão de bases!")
    printLine(True)

    printLine()
    print("Integrantes do grupo:")
    printLine()

    for integrante in integrantes:
        print(f"Nome: {integrante['nome']}, RGM: {integrante['RGM']}")

    printLine(True)

def printMenu():
    printLine()
    print("Por favor, escolha uma das opções abaixo:")
    printLine()

    for i in range(len(opcoesMenus)):
        print(f"{i + 1} - {opcoesMenus[i]}")

    printLine()

    valorEscolha = int(input("Digite a opção desejada: "))

    printLine()

    return valorEscolha

def printResultado(numDigitado, func, baseConvertida):
    printLine()
    print(f"O número {numDigitado} em {baseConvertida} é: {func(numDigitado)}")
    printLine(True)

#DECIMAL -> BINARIO
def decimalToBinario(decimal):
    if decimal == 0:
        return '0'
    
    binario = ''

    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2

    return binario

#DECIMAL -> HEXADECIMAL
def decimalToHexadecimal(decimal):
    if decimal == 0:
        return '0'
    
    hexadecimal = ''

    while decimal > 0:
        resto = decimal % 16

        if resto == 10:
            hexadecimal = 'A' + hexadecimal
        elif resto == 11:
            hexadecimal = 'B' + hexadecimal
        elif resto == 12:
            hexadecimal = 'C' + hexadecimal
        elif resto == 13:
            hexadecimal = 'D' + hexadecimal
        elif resto == 14:
            hexadecimal = 'E' + hexadecimal
        elif resto == 15:
            hexadecimal = 'F' + hexadecimal
        else:
            hexadecimal = str(resto) + hexadecimal

        decimal = decimal // 16

    return str(hexadecimal)

#DECIMAL -> OCTAL
def decimalToOctal(decimal):
    if decimal == 0:
        return '0'
    
    octal = ''

    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal = decimal // 8

    return octal

#BINARIO -> DECIMAL
def binarioToDecimal(binario):
    decimal = 0
    expoente = 0

    for bit in reversed(str(binario)):
        decimal += int(bit) * (2 ** expoente)
        expoente += 1

    return str(decimal)

#HEXADECIMAL -> DECIMAL
def hexadecimalToDecimal(hexadecimal):
    decimal = 0
    expoente = 0

    for bit in reversed(str(hexadecimal)):
        if bit == 'A':
            decimal += 10 * (16 ** expoente)
        elif bit == 'B':
            decimal += 11 * (16 ** expoente)
        elif bit == 'C':
            decimal += 12 * (16 ** expoente)
        elif bit == 'D':
            decimal += 13 * (16 ** expoente)
        elif bit == 'E':
            decimal += 14 * (16 ** expoente)
        elif bit == 'F':
            decimal += 15 * (16 ** expoente)
        else:
            decimal += int(bit) * (16 ** expoente)

        expoente += 1

    return str(decimal)

#OCTAL -> DECIMAL
def octalToDecimal(octal):
    decimal = 0
    expoente = 0

    for bit in reversed(str(octal)):
        decimal += int(bit) * (8 ** expoente)
        expoente += 1

    return str(decimal)

def validarBinario(numDigitado):
    while True:
        if all([bit in ['0', '1'] for bit in str(numDigitado)]):
            return numDigitado

        printLine()
        print("Número inválido! O número deve ser binário, contendo apenas 0 e 1.")
        printLine()

        numDigitado = int(input("Digite o número que deseja converter: "))

printIntegrantes()

escolha = printMenu()

while escolha > 0:
    if escolha == 7:
        print("Encerrando o sistema...")
        
        break

    if escolha <= len(opcoesMenus):
        num = int(input("Digite o número que deseja converter: "))

        printLine()
        print(f"Você escolheu a opção: {opcoesMenus[escolha - 1]}")
        printLine(True)

        if escolha == 1:
            printResultado(num, decimalToBinario, "binário")

        elif escolha == 2:
            printResultado(num, decimalToHexadecimal, "hexadecimal")

        elif escolha == 3:
            printResultado(num, decimalToOctal, "octal")

        elif escolha == 4:
            num = validarBinario(num)

            printResultado(num, binarioToDecimal, "decimal")

        elif escolha == 5:
            printResultado(num, hexadecimalToDecimal, "decimal")

        elif escolha == 6:
            printResultado(num, octalToDecimal, "decimal")

        if escolha <= (len(opcoesMenus) - 1):
            escolha = 0

    else:
        print("Opção inválida!")

    escolha = printMenu()