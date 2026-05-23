# Calculadora simples

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisao por zero"
    return a / b

print("=== Calculadora ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha uma opcao: ")
a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

if opcao == "1":
    print("Resultado:", somar(a, b))
elif opcao == "2":
    print("Resultado:", subtrair(a, b))
elif opcao == "3":
    print("Resultado:", multiplicar(a, b))
elif opcao == "4":
    print("Resultado:", dividir(a, b))
else:
    print("Opcao invalida")