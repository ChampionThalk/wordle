
from packages.palavra import Palavra




print("Gostaria de um sugestão de palavra ?")
print("[s/n]")
a = input()
if a == "s":
  palavra= Palavra.random_word()
else:
  palavra = input()


print("\n" * 50 )
print(palavra)
print( "tem" + " " + str(len(palavra)) + " " +"letras.") 
 
c =list(palavra)
praresolver = 1

for chances in range(6):
  tentativa = input()
  if len(tentativa) != len(palavra):
    print("números de casas erradas")
  else:
   acertos = []
   for i in range(len(palavra)):

    if palavra[i] == tentativa[i]:
        acertos.append( (palavra[i].upper()))
    elif tentativa[i] in palavra:
        acertos.append( tentativa[i].lower())
    else:
        acertos.append("_")
   
   if "".join(acertos).lower() == palavra:
    print("".join(acertos))
    print("Resposta correta")
    praresolver += -1
    break
   else:
    print("".join(acertos))

print("Palavra correta:", palavra) if praresolver == 1 else 0