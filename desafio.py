# 1) Solicita ao usuário que digite seu nome
 
try:
     nome = input("Digite seu nome: ")
     # (len) verifica se o nome está vazio e 
     if len(nome.strip()) == 0:
         raise ValueError("O nome não pode estar vazio.")
     # Verifica se há números no nome
     elif any(char.isdigit() for char in nome):
         raise ValueError("O nome não deve conter números.")
     # (strip) remove espaços em branco do início e do final da string 'nome'. 
     else:
         print("Nome válido:", nome.strip())
except ValueError as e:
     print(e)

###############################################################################
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
     salario = float(input("Digite o valor do seu salario: "))
     if salario <= 0:
         print("Salario digitado é negativo ou igual a 0, favor digitar corretamente..")
except ValueError:    
     print("Entrada invalida. Por favor, digite um numero!")

##############################################################################
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus = float(input("Digite o valor do bonus recebido: "))
    if bonus <= 0:
        print("O bonus digitado é negativo ou igual a zero.")
except ValueError:
    print("Entrada invalida. Por favor, digite um numero!")

###############################################################################
# 4) Calcule o valor do bônus final
bonus_recebido = (salario * bonus) + 1000   # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
