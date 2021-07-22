import forcqa
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo********")
print("*********************************")

print("(1) Forca e (2)Advinhação")

jogo = int(input("qual jogo?"))
if(jogo == 1):
    print("jogando forca")
    forca.jogar_forca()
elif(jogo == 2):
      print("jogando adivinhação")
      adivinhacao.jogar_adivinhacao()
