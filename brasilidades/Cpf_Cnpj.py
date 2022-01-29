from validate_docbr import CPF, CNPJ

class Documento:
    # isso é um factory (fabrica), depois podemos dividir as classes 
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return cpf_doc(documento)
        elif len(documento) == 14:
            return cnpj_doc(documento)
        else: 
            raise ValueError('Quantidade de digitos invalida')


class cpf_doc:
    def __init__(self, documento):
        if self.valida_cpf(documento):
            self.cpf = documento
        else: 
            raise ValueError('CPF inválido')

    def __str__(self):
        return self.formata_cpf()

# verifica se o cpf tem 11 caracteres
    def valida_cpf(self, documento):
        validador_cpf = CPF()
        return validador_cpf.validate(documento)

# formata o cpf
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class cnpj_doc:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else: 
            raise ValueError('CNPJ inválido')

    def __str__(self):
        return self.formata_cnpj()

# verifica se o cnpj tem 14 caracteres
    def valida_cnpj(self, documento):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(documento)

# formata o cnpj
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)






