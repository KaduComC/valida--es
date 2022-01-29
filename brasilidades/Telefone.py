import re

class Telefone():
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto')

    def valida_telefone(self, telefone):
        # pdoe ou não ter o codigo do pais
        # padrao
        padrao = '([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    # formata a mascara do numero para a presentação
    def format_numero(self):
        padrao = '([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        numero_formatado = f'+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'
        return numero_formatado

    def __str__(self):
        return self.format_numero()