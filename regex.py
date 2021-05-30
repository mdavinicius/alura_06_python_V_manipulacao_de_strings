import re

# Desafio1 = Puxar os diversos números de telefone com 8 e 9 dígitos, com e sem hífen
email1 = 'Meu número é 1234-1234'
email2 = 'Fale comigo em 1234-1234 esse é meu telefone'
email3 = '91234-1234 é o meu celular'
email4 = 'lalalaalala 9543-1254 lalal a 1234-1234 lalalal 12344568 allalala'

padrao = '[0-9]{4,5}[-]*[0-9]{4}'  # nº de 0 a 9 que aparecem 4 ou 5 vezes, seguidos de hifen, novamente nº de 0 a 9 em 4 vezes
retorno0 = re.search(padrao, email4)
print(retorno0.group())
# para usar o search() na hora do print, precisamos chamar o group(), senão trará o valor na memória, além disso,
# o search puxa apenas o 1º valor encontrado na sentença
print("-----------------------------------")

retorno1 = re.findall(padrao, email1)
retorno2 = re.findall(padrao, email2)
retorno3 = re.findall(padrao, email3)
retorno4 = re.findall(padrao, email4)
print(retorno1, retorno2, retorno3, retorno4)
# com findall(), o valor aprece em formato list e puxa todos os resultados encontrados, for eg, email 4
print("-----------------------------------")


# Desafio2 = Puxar dia da semana e hora

tamanho = []
dias_da_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]
for dia in dias_da_semana:
    tamanho.append(len(dia))
print(tamanho)
print("O tamanho mínimo é {} e o máximo é {}".format(min(tamanho), max(tamanho)))
# os dias da semana tem palavras de 5 a 7 caractereses
print("-----------------------------------")

padrao = '[a-z]{5,7} [0-9]{2}[h]'  # letra de A a Z aparecendo 5 a 7x, espaço, nº 0 a 9 aparecendo 2x seguido de 'h'
frase1 = 'podemos marcar de sair domingo 23h'
frase2 = 'acho que quinta 21h é a melhor hora para a gente ir lá'
frase3 = 'terca 19h é um bom momento para sairmos'

busca1 = re.findall(padrao, frase1)
busca2 = re.findall(padrao, frase2)
busca3 = re.findall(padrao, frase3)

print(busca1, busca2, busca3)