print ('seja bem vindo a calculadora')
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

while True:
    print("\nSelecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if escolha == '1':
            print(num1, "+", num2, "=", adicionar(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtrair(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", dividir(num1, num2))
    elif escolha == '5':
        break
    else:
        print("Entrada inválida. Por favor, digite uma opção válida.")
