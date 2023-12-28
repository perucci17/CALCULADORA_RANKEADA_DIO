def saldoVitorias (vitorias, derrotas):
      saldo_vitoria = vitorias - derrotas
      return saldo_vitoria

suas_vitorias = eval(input(" Digite o seu número de vitórias: "))
suas_derrotas = eval(input("Digite o seu número de derrotas: "))

res = saldoVitorias(suas_vitorias, suas_derrotas)



if res <= 10:
      print((' O heroi tem saldo de ' + str(res) + " e está no nível ferro "))
if res >= 11 and res <= 20:
      print((' O heroi tem saldo de ' + str(res)+ " e está no nível bronze "))
if res >= 21 and res <= 50:
      print((' O heroi tem saldo de ' + str(res) + " e está no nível prata "))
if res >= 51 and res <= 80:
      print((' O heroi tem saldo de ' + str(res) + " e está no nível ouro "))
if res >= 81 and res <= 90:
      print((' O heroi tem saldo de ' + str(res) + " e está no nível diamante "))
if res >= 91 and res <= 100:
      print((' O heroi tem saldo de ' + str(res) + " e está no nível lendário "))
if res >= 101:
      print((' O heroi tem saldo de ' + str(res) + " e está no nível imortal "))

 


