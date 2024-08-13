def adicao(a, b)
    return a + b

def subtracao(a, b)
    return a - b

def multiplicacao(a, b)
    return a * b

def divisao(a, b)
    return a / b

def calculadora():
    operacao = input("Escolha uma operação (+, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = adicao(num1, num2)
        print("Resultado: ", resultado)
        
    elif operacao == "-":
        resultado = subtracao(num1, num2)
        print("Resultado: ", resultado)
        
    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
        print("Resultado: ", resultado)
        
    elif operacao == "/":
        resultado = divisao(num1, num2)
        print("Resultado: ", resultado)

    else: 
        print("Operação inválida!")

calculadora()
