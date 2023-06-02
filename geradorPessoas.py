from fordev.generators import people
import re

class Pessoa:
    def __init__(self, sex, age, uf_code):
        pessoa = people(sex=sex, age=age, uf_code=uf_code)
        self.dados = pessoa[0]

    def get_nome(self):
        return self.dados['nome']

    def get_idade(self):
        return self.dados['idade']

    def get_cpf(self):
        self.dados['cpf'] = re.sub('[^0-9]', '', self.dados['cpf'])
        return self.dados['cpf']

    def get_rg(self):
        return self.dados['rg']

    def get_data_nasc(self):
        return self.dados['data_nasc']

    def get_sexo(self):
        return self.dados['sexo']

    def get_signo(self):
        return self.dados['signo']

    def get_mae(self):
        return self.dados['mae']

    def get_pai(self):
        return self.dados['pai']

    def get_email(self):
        return self.dados['email']

    def get_senha(self):
        return self.dados['senha']

    def get_cep(self):
        self.dados['cep'] = re.sub('[^0-9]', '', self.dados['cep'])
        return self.dados['cep']

    def get_endereco(self):
        return self.dados['endereco']

    def get_numero(self):
        return self.dados['numero']

    def get_bairro(self):
        return self.dados['bairro']

    def get_cidade(self):
        return self.dados['cidade']

    def get_estado(self):
        return self.dados['estado']

    def get_telefone_fixo(self):
        return self.dados['telefone_fixo']

    def get_celular(self):
        self.dados['celular'] = re.sub('[^0-9]', '', self.dados['celular'])
        return self.dados['celular']

    def get_altura(self):
        return self.dados['altura']

    def get_peso(self):
        return self.dados['peso']

    def get_tipo_sanguineo(self):
        return self.dados['tipo_sanguineo']

    def get_cor(self):
        return self.dados['cor']

