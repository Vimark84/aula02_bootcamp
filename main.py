# exemplo typeError

#  try:
#      resultado= len(3)
#      print(resultado)
#  except TypeError as e:
#      print(e)    
#  
#  else:
#      print("tudo ocorreu bem")
#  finally:
#      print("o importante é participar")

######################################################
#  
#  numero = "abc"
#  if isinstance(numero, int):
#      print("A variável é um inteiro.")
#  else:
#      print("A variável não é um inteiro.")
#      
######################################################


try:
    numero = int(input("insira um numero: "))
    if isinstance(numero, int):
        print("a variavel é um inteiro.")
    else:
        print("a variavel não é um inteiro.")
except ValueError:
    print("A entrada não é um número inteiro.")


