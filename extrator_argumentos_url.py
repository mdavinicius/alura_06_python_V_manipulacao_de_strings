class Extrator_argumentos_url:
    def __init__(self, url):
        if self.url_e_valida(url):
            self.url = url.lower()
        else:
            raise LookupError('Url inválida!!!')

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moeda_origem, moeda_destino = self.extrair_argumentos()
        return f'Valor: {self.extrai_valor()}\nMoeda Origem: {moeda_origem}\nMoeda Destino: {moeda_destino}'

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def url_e_valida(url):
        if url and url.startswith('https://www.bytebank.com.br'):
            return True
        else:
            return False

    def extrair_argumentos(self):
        busca_moeda_origem = 'moedaorigem='.lower()
        busca_moeda_destino = 'moedadestino='.lower()

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find('&')
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == 'moedadestino':
            self.troca_moeda_origem()
            indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
            indice_final_moeda_origem = self.url.find('&')
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        indice_final_moeda_destino = self.url.find('&valor')
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace('moedadestino', 'real', 1)
        print(self.url)

    def extrai_valor(self):
        busca_valor = 'valor='
        indice_inicial_valor = self.encontra_indice_inicial(busca_valor)
        valor = self.url[indice_inicial_valor:]
        return valor

