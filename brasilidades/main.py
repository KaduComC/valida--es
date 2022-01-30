import requests
from Cpf_Cnpj import Documento
from Telefone import Telefone
from Datas import Datas
from acesso_cep import Busca_endereco

cep = 76600000

obj_cep = Busca_endereco(cep)
bairro, cidade, uf = obj_cep.acessa_via_CEP()
print(bairro, cidade, uf)
# print(obj_cep)

# # data = Datas()
# # print(data.mes_cadastro())
# # print(data.se())

# # telefone = '5562998651575'
# # telefone_obj = Telefone(telefone)
# # print(telefone_obj)
# # cnpj_ex = '35379838000112'
# # cpf_ex = '07324500129'

# # doc = Documento.cria_documento(cpf_ex)
# # print(doc)

# r = requests.get('https://viacep.com.br/ws/01001000/json/')
# print(r.text)