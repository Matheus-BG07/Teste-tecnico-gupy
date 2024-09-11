def is_fibonacci(num):

    def is_perfect_square(x):
        y = int(x**0.5)
        return y*y == x
    
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

# Entrada do usuário
num = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
