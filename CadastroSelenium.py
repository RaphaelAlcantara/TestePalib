import geradorPessoas as gp
import time

pessoa = gp.Pessoa(sex='M', age=26, uf_code='PE')

nome = pessoa.get_nome()
cpf = pessoa.get_cpf()
telefone = pessoa.get_celular()
cep = pessoa.get_cep()
numeroCasa = pessoa.get_numero()
senha = 'Teste@123'

cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

telefone = telefone.replace('(', '')
telefone = telefone.replace(')', '')
telefone = telefone.replace('-', '')
telefone = telefone.replace(' ', '')

cep = cep.replace('-', '')

#Configuração inicial

from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait #espera o elemento carregar
from selenium.webdriver.common.by import By #localizar elemento
# from selenium.webdriver.support import expected_conditions as EC #espera o elemento carregar
from webdriver_manager.firefox import GeckoDriverManager #pega o driver atual
# from webdriver_manager.chrome import ChromeDriverManager #pega o driver atual
# from selenium.webdriver.chrome.service import Service #executa o menager
from selenium.webdriver.firefox.service import Service #executa o menager

# servico = Service(GeckoDriverManager().install()) # instala o driver do mozila atual
servico = Service(GeckoDriverManager().install()) # instala o driver do chrome atual
# navegador = webdriver.Firefox(service=servico)
navegador = webdriver.Firefox(service=servico)

print(cpf)

from selenium.webdriver import ActionChains, Keys

#entra na url que deseja; obs: o link precisa ser completo com https://
navegador.get("http://localhost:8080/NovoPalib/")

#entra no cadastro
navegador.find_element('xpath', '//*[@id="formLogin:j_idt17"]').click()

#preenche o nome
navegador.find_element('xpath', '//*[@id="input_formCadUsuario:nameValidator"]').send_keys(nome)
ActionChains(navegador).send_keys(Keys.TAB).perform()
time.sleep(1)

#preenche o cpf
navegador.find_element('xpath', '//*[@id="input_formCadUsuario:cpfValidator"]').send_keys(cpf)
ActionChains(navegador).send_keys(Keys.TAB).perform()
time.sleep(1)

#preenche o telefone
navegador.find_element('xpath', '//*[@id="input_formCadUsuario:telefoneValidator"]').send_keys(telefone)
ActionChains(navegador).send_keys(Keys.TAB).perform()
time.sleep(1)

#preenche o cep
navegador.find_element('xpath', '//*[@id="input_formCadUsuario:j_idt27"]').send_keys(cep)
navegador.find_element('xpath', '//*[@id="formCadUsuario:j_idt28"]').click()
time.sleep(1)

navegador.find_element('xpath', '//*[@id="formCadUsuario:j_idt36_input"]').send_keys(numeroCasa)
ActionChains(navegador).send_keys(Keys.TAB).perform()
time.sleep(1)

#preenche a senha

navegador.find_element('xpath', '//*[@id="input_formCadUsuario:senhaValidator"]').send_keys(senha)
ActionChains(navegador).send_keys(Keys.TAB).perform()
time.sleep(1)

#preenche a confirmação de senha

navegador.find_element('xpath', '//*[@id="input_formCadUsuario:senha2Validator"]').send_keys(senha)
time.sleep(0.5)

#Registrar
navegador.find_element('xpath', '//*[@id="formCadUsuario:j_idt42"]').click()

# #usar lib BY
# mensagem = navegador.find_element(By.
# print(mensagem)



#salvar cpf em um arquivo txt
arquivo = open('cpf.txt', 'w')
arquivo.write('\n' + cpf + '\n')
arquivo.close()
