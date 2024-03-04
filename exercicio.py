import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1= int(input("digite um numero: "))
# num2= int(input("digite o segundo numero: "))
# soma=(num1 + num2)
# print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num = 18  # Exemplo de entrada
# resultado_resto = num % 5
# print("O resto da divisão por 5 é:", resultado_resto)

# Recebe os números do usuário
# dividendo = int(input("Digite o dividendo: "))
# divisor = int(input("Digite o divisor: "))
# resto = dividendo % divisor # Calcula o resto da divisão
# print("O resto da divisão de", dividendo, "por", divisor, "é:", resto) # Imprime o resultado

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num1= int(input("digite um numero: "))
# num2= int(input("digite o segundo numero: "))
# multiplicacao=(num1 * num2)
# print("o resultado da multiplicação é: ", multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#numero_01 = int(input("digite o primeiro numero: "))
#numero_02 = int(input("digite o segundo numero: ")) 
#resultado = numero_01 // numero_02
#print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#numero_01 = int(input("digite o primeiro numero: "))
#numero_02 = int(input("digite o segundo numero: ")) 
#resultado = numero_01 ** numero_02
#print(resultado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_01 = float(input("digite o primeiro numero: "))
# numero_02 = float(input("digite o segundo numero: ")) 
# resultado = numero_01 + numero_02
# print(resultado)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num_01 = float(input("digite o primeiro numero: "))
# num_02 = float(input("digite o segundo numero: ")) 
# media = (num_01 + num_02) / 5
# print(media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = int(input("digite uma base: "))
# expoente = int(input("digite um expoente: "))
# calculo_potencia = base ** expoente
# print("O resultado desta operação é: ", calculo_potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Enter the Temperature in Celsius :\n"))
# fahrenheit = (1.8 * celsius) + 32
# print(f"{celsius}ºC é igual a {fahrenheit}ºF")

## 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#def calcular_area_do_circulo(raio):
#    area = math.pi * raio**2
#    return area
#
# raio_do_circulo = float(input("Digite o raio do círculo: "))
# area_do_circulo = calcular_area_do_circulo(raio_do_circulo)
# print("A área do círculo é:", area_do_circulo)
#
# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
## area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
# print(f"{area_do_circulo:.2f}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# nome = "marcos"
# conv_maiuscula= nome.upper()
# print(conv_maiuscula)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome_completo = "MArcos Vinicius FErnandes"
# conv_minusculo = nome_completo.lower()
# print(conv_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase= input("insira uma frase: ")
# frase_sem_espacos = frase.strip()
# print(frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(lista_de_dia_mes_ano)
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# nome= "Marcos"
# sobre_nome=" Fernandes"
# print(nome + sobre_nome)


#  python exercicio.py
# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# valor1 = True
# valor2 = False
# resultado_and = valor1 and valor2
# print("Resultado do AND lógico:", resultado_and)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# valor1 = True
# valor2 = False
# resultado_or = valor1 or valor2
# print("Resultado do OR lógico:", resultado_or)


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# Exemplo de entrada
# valor1 = True
# valor2 = False
# resultado_not = not valor1
# print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# num1 = 5
# num2 = 5
# resultado_igualdade = (num1 == num2)
# print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# Exemplo de entrada
#num1 = 8
#num2 = 5
#resultado_diferenca = (num1 != num2)
#print("Resultado da diferença:", resultado_diferenca)


# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     celsius = float(input("Enter the Temperature in Celsius :\n"))
#     fahrenheit = (1.8 * celsius) + 32
#     print(f"{celsius}ºC é igual a {fahrenheit}ºF")
# except ValueError:
#     print("voce não digitou um numero")



# 22: Verificador de Palíndromo
# 
# string = input("digite uma palavra ou frase: ")
# if string.isdigit():
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")
# else:    
#     formatado = string.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")

    
# 23: Calculadora Simples
# tambem podemos resolver isso inicializando resultado antes do bloco try, atribuindo a ele um valor padrão. (NONE)
# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     operador = input("Digite o operador (+, -, *, /): ")
#     if operador == '+':
#         resultado = num1 + num2
#         print("O resultado é:", resultado)
#     elif operador == '-':
#         resultado = num1 - num2
#         print("O resultado é:", resultado)
#     elif operador == '*':
#         resultado = num1 * num2     
#         print("O resultado é:", resultado)
#     elif operador == '/' and num2 != 0:
#         resultado = num1 / num2
#         print("O resultado é: ", resultado) 
#     else:     
#         print("Operador invalido ou divisão por zero.")
#            
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")



# 24: Classificador de Números
# 
# try:
#     num1 = int(input("Digite o primeiro número: "))
#     if num1 > 0:
#         print("O numero digitado é: positivo ") 
#     elif num1 < 0:
#         print("O numero digitado é: negativo ")
#     else:
#         print("O numero digitado é: 0 ")   
#     if num1 % 2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")          
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")


# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")



