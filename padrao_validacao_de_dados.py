# -*- coding: utf-8 -*-
"""Padrao_Validacao_De_Dados.ipynb
"""

!pip install validate-docbr

from validate_docbr import CPF,CNPJ

class Documento:  
  @staticmethod
  def cria_documento(documento):
    if len(documento) == 11:
      return DocCpf(documento)
    elif len(documento) == 14:
      return DocCnpj(documento) 
    else:
      raise ValueError("Documento Inválido ou Quantidade de Digitos errada")

class DocCpf:
  def __init__(self,documento):
    if self.valida(documento):
      self.cpf = documento
      print('CPF cadastrado')
    else:
      raise ValueError("Documento Inválido")
  
  def __str__(self):
    return self.formata()

  def valida(self,documento):
      validadorBrasil = CPF()
      return  validadorBrasil.validate(documento)

  def formata(self): # só é necessário o nosso SELF, pois usará o cpf da própria instância
      mascara = CPF()
      return mascara.mask(self.cpf)

class DocCnpj:
  def __init__(self,documento):
    if self.valida(documento):
      self.cnpj = documento
      print('CNPJ cadastrado')
    else:
      raise ValueError("Documento Inválido")

  def __str__(self):
      return self.formata()

  def valida(self,documento):
      validadorBrasil = CNPJ()
      return  validadorBrasil.validate(documento)

  def formata(self): # só é necessário o nosso SELF, pois usará o cpf da própria instância
      mascara = CNPJ()
      return mascara.mask(self.cnpj)

objeto_cnpj = Documento.cria_documento('33014556000196') # coloque um CNPJ real para testar
objeto_cpf = Documento.cria_documento('42365646826') # coloque um CPF real para testar
print(objeto_cnpj)
print(objeto_cpf)

import re

class TelefonesBr:

  def __init__(self,telefone):
    if self.valida_telefone(telefone):
      self.telefone = telefone
    else:
      raise ValueError("Telefone inválido") 

  def valida_telefone(self,telefone):
    padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"  # Padrão em telefone maiores com mask
    resposta = re.search(padrao,telefone)
    if resposta:
      return True # temos que ter o seguinte entendimento para a separação ()
      
    else:
      return False
  def __str__(self):
    return f"seu número formatado: {self.format_numero()}"

  def format_numero(self):
    padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
    resposta = re.search(padrao,self.telefone)
    return f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"

tel = '551183804482'
teste = TelefonesBr(tel)
print(teste )

from datetime import datetime,timedelta
# chamando o método do pacote datetime.today() vemos a hora real
class DatasBr:
  
  def __init__(self):
    self.dt_cadastro = datetime.today()
  
  def __str__(self):
    return self.data_formatada()

  def mes_cadastro(self):
    meses_do_ano = [
        "janeiro","fevereiro","março","abril","maio",
        "junho","julho","agosto","setembro","outubro",
        "novembro","dezembro"
        ]
    return meses_do_ano[self.dt_cadastro.month-1] 
    # número inteiro - mês, então colocamos em uma lista.
  
  def dia_semana(self):
    dia_da_semana = [
        "segunda", "terça","quarta","quinta", "sexta", "sábado","domingo"
    ]
    return dia_da_semana[self.dt_cadastro.weekday()]
    # número inteiro - semana, en~toa colocamos em uma lista a posição que retorna.
  
  def data_formatada(self):
    return self.dt_cadastro.strftime("%d/%m/%Y %H:%M")

  def tempo(self):
    return (datetime.today() + timedelta(days=30)) - self.dt_cadastro # pegando no mesmo instante

hoje = DatasBr()
print(hoje.tempo()) # como já prevemos iria ser o 0:00:00.000085, já é que o mesmo date em instância
# agora com o timedelta(days=30), como se o delta desta data adquirida fosse sempre 30 dias

#API's dentro da programação, uma visão geral do que podemos fazer com ela.
# diferenciação enorme de como utilizar.
import requests
class BuscaEndereco:
  def __init__(self,cep):
    cep = str(cep)
    if self.cep_e_valido(cep):
      self.cep = cep
      print('CEP cadastrado')
    else:
      raise ValueError("CEP inválido")

  def __str__(self):
    return self.formata_cep()

  def formata_cep(self):
    return f"{self.cep[:5]}-{self.cep[5:]}"

  def acessa_via_cep(self):
    r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
    dados = r.json()
    return (
        dados['bairro'],
        dados['localidade'],
        dados['uf']
    ) # retornando uma tupla de valores, que pode lógicamente ser desmembrada

  def cep_e_valido(self,cep):
    if len(cep) == 8:
      return True
    else:
      return False

cep = '04288019' # coloque um CEP real para testar
teste = BuscaEndereco(cep)
bairro,cidade,uf = teste.acessa_via_cep()
print(cidade)