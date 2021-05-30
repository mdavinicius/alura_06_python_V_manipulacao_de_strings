print("Desafio 1")
# trazer apenas o nº '26'
sobre_mim = 'Meu nome é Rodrigo e minha idade é 26'
print(sobre_mim)
print(len(sobre_mim))  # sem regex - pega a len
print(sobre_mim[35:])  # fatia a lista
print(sobre_mim[len(sobre_mim) - 2:])  # ou, sabendo que o nº são 2 caracteres, faz o len -2
print("-----------------------------------")

print("Desafio 2")
# trazer apenas a palavra 'real' via find
url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'
argumento = 'moedaorigem=real'
index = argumento.find('=')  # com o uso do find() encontramos o '=' na sentença
substring = argumento[index + 1:]  # depois fatiamos a string a partir do '=' até o final
print(substring)
print("-----------------------------------")

print("Desafio 3")
# trazer apenas a palavra 'real' via slip
url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'
argumento = 'moedaorigem=real'
lista_argumentos = argumento.split('=')  # com o uso do slipt() separamos a sentença a partir do '='
print(lista_argumentos)
print(lista_argumentos[1])  # depois pegamos a parte que nos interessa
print("-----------------------------------")

print("Desafio 4")
# trazer o 'real' e 'dolar' com base em uma função criada
from extrator_argumentos_url import Extrator_argumentos_url

url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'
argumentos_url = Extrator_argumentos_url(url)
moeda_origem, moeda_destino = argumentos_url.extrair_argumentos()
print(moeda_origem, moeda_destino)
print("-----------------------------------")

print("Aprendendo função replace()")
string = 'bytebankbytebyte'
string_nova = string.replace('byte', 'rodrigo', 2)  # replace: substitui 'byte' por 'rodrigo' nas 2 primeiras aparições
print(string_nova)
print("-----------------------------------")

print("Desafio 5")
# trazer o 'real' e 'dolar' sendo o que o link foi alterado para 'moedaorigem=moedadestino'
from extrator_argumentos_url import Extrator_argumentos_url

url = 'https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500'

argumentos_url = Extrator_argumentos_url(url)  # inserido um if na função, caso 'moedaorigem=moedadestino' para haver um replace por 'real'
moeda_origem, moeda_destino = argumentos_url.extrair_argumentos()
print(moeda_origem, moeda_destino)
print("-----------------------------------")

print("Desafio 6")
# trazer o 'real' e 'dolar' sendo o que o link foi alterado para com letras em maiúsculo
# e trazer o valor de '1500'
from extrator_argumentos_url import Extrator_argumentos_url

url = 'https://www.bytebank.com.br/cambio?moedaORiGem=moedadestino&moedadestino=dolar&valor=1500'

argumentos_url = Extrator_argumentos_url(url)  # função ajustada para após validação da url, colocar tudo em lower
moeda_origem, moeda_destino = argumentos_url.extrair_argumentos()
valor = argumentos_url.extrai_valor()
print(moeda_origem, moeda_destino, valor)
print("-----------------------------------")

print("Desafio 7")
# verficar se a url é realmente 'https://www.bytebank.com.br'
from extrator_argumentos_url import Extrator_argumentos_url

url = 'https://www.bitebank.com.br/cambio?moedaORiGem=moedadestino&moedadestino=dolar&valor=1500'
# argumentos_url = Extrator_argumentos_url(url)  # dará erro, pois a url não idêntica ao parâmetro
print("-----------------------------------")

print("Desafio 8")
# verficar o tamanho do argumentos_url
from extrator_argumentos_url import Extrator_argumentos_url

url = 'https://www.bytebank.com.br/cambio?moedaORiGem=moedadestino&moedadestino=dolar&valor=1500'

argumentos_url = Extrator_argumentos_url(url)
print(len(argumentos_url))  # simplesmente usar o len() para pegaro tamanho da url toda
print("-----------------------------------")

print("Desafio 9")
# compara 2 var com a mesma url e fazer dar True
from extrator_argumentos_url import Extrator_argumentos_url

url = 'https://www.bytebank.com.br/cambio?moedaORiGem=moedadestino&moedadestino=dolar&valor=1500'

argumentos_url = Extrator_argumentos_url(url)
argumentos_url2 = Extrator_argumentos_url(url)
print("Vai dar erro: ", argumentos_url == argumentos_url2)  # assim dará False pois são objetos alocados na memória diferentes
argumentos_url2 = argumentos_url
print("Vai dar certo: ", argumentos_url == argumentos_url2)  # assim dará True, pois estou copiando um objeto em outro
print("-----------------------------------")

print("Desafio 10")
# printe moeda origem, destino e valor de forma formatada usando o objeto sem método algum
from extrator_argumentos_url import Extrator_argumentos_url

url = 'https://www.bytebank.com.br/cambio?moedaORiGem=moedadestino&moedadestino=dolar&valor=1500'

argumentos_url = Extrator_argumentos_url(url)
moeda_origem, moeda_destino = argumentos_url.extrair_argumentos()
valor = argumentos_url.extrai_valor()
print(argumentos_url)  # sai formatado graças ao método __str__