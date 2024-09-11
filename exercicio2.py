# Captura a frase do usuário
frase = str(input("Digite aqui uma frase: "))
# Transforma a frase em minúsculo
frase = frase.lower()
# Conta a ocorrência da letra "a"
contar = frase.count('a')

if contar >= 1:
    print (f"A letra A aparece na frase {contar} vezes")
else:
    print ("A frase não contém a letra A")
