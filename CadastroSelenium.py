import logging
import time

import pyautogui as pyautogui
from selenium.webdriver.firefox.options import Options

import geradorPessoas as Gp

# Configurar o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

pessoa = Gp.Pessoa(sex='M', age=26, uf_code='PE')

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

# Contagem de testes bem-sucedidos e mal-sucedidos
num_tests_passed = 0
num_tests_failed = 0

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


#salvar cpf em um arquivo txt
arquivo = open('cpf.txt', 'a')
arquivo.write('\n' + cpf + '\n')
arquivo.close()


from selenium.webdriver import ActionChains, Keys

options = Options()
options.add_argument("--start-maximized")

try:
    # Teste 1: Cadastro de usuário com sucesso
    logging.info('Iniciando teste de cadastro de usuário com dados válidos')

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
    navegador.find_element('xpath', '//*[@id="input_formCadUsuario:cepValidator"]').click()
    navegador.find_element('xpath', '//*[@id="input_formCadUsuario:cepValidator"]').send_keys(cep)
    navegador.find_element('xpath', '//*[@id="formCadUsuario:j_idt27"]').click()
    time.sleep(1)

    navegador.find_element('xpath', '//*[@id="formCadUsuario:j_idt35_input"]').click()
    navegador.find_element('xpath', '//*[@id="formCadUsuario:j_idt35_input"]').send_keys(numeroCasa)
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
    navegador.find_element('xpath', '//*[@id="formCadUsuario:j_idt41"]').click()
    time.sleep(1)
    # #usar lib BY
    mensagemCadastroSucesso = navegador.find_element(By.XPATH, '/html/body/div[5]/span[3]').text

    assert mensagemCadastroSucesso == "Usuario cadastrado com sucesso!"
    logging.info('Teste de cadastro de usuário com dados válidos finalizado com sucesso')
    num_tests_passed += 1

    logging.info('-' * 50)
    # -------------------------------------------------------------------------------------------------------------

    # Teste 2 de login com dados inválidos
    logging.info('Iniciando teste de login com dados inválidos')

    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt12"]').click()
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt12"]').send_keys(cpf)
    time.sleep(0.5)

    # preenche a senha
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').click()
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').clear()
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').send_keys('senhaRuimGG')

    time.sleep(0.5)

    navegador.find_element('xpath', '//*[@id="formLogin:j_idt18"]').click()
    time.sleep(0.5)

    LoginInvalido = navegador.find_element(By.CSS_SELECTOR, '.col-xs-11 > span:nth-child(4)').text
    print(LoginInvalido)
    time.sleep(0.5)
    assert LoginInvalido in "Login ou Senha não conferem"

    logging.info('Teste de login com dados inválidos finalizado com sucesso')

    num_tests_passed += 1

    logging.info('-' * 50)

    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt12"]').clear()
    time.sleep(0.5)
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').clear()

    # -------------------------------------------------------------------------------------------------------------

    # Teste de login com sucesso
    logging.info('Iniciando teste de login com dados válidos')
    #url igual a inicial
    navegador.get("http://localhost:8080/NovoPalib/")

    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt12"]').click()
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt12"]').clear()
    time.sleep(0.5)
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt12"]').send_keys(cpf)
    time.sleep(0.5)

    #preenche a senha
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').click()
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').clear()
    time.sleep(0.5)
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').send_keys(senha)

    time.sleep(0.5)

    navegador.find_element('xpath', '//*[@id="formLogin:j_idt18"]').click()

    msgloginNome = navegador.find_element(By.XPATH, '//*[@id="dtLformMenuCliente:j_idt15"]').text

    print(msgloginNome)
    assert msgloginNome == "Cliente: " + nome


    logging.info('Teste de login com dados válidos finalizado com sucesso')

    num_tests_passed += 1

    logging.info('-' * 50)




except Exception as e:
    # Tratar exceções e contagem de testes falhos
    logging.error("Erro no teste: " + str(e))
    num_tests_failed += 1

finally:
    # Imprimir resultados do teste
    logging.info("\033[1;32mNúmero de testes bem-sucedidos: " + str(num_tests_passed) + "\033[1;0m")
    if num_tests_failed > 0:
        logging.error("\033[1;31mNúmero de testes mal-sucedidos: " + str(num_tests_failed) + "\033[1;0m")
    else:
        logging.info("\033[1;32mTodos os testes foram bem-sucedidos!\033[1;0m")

    # Fechar o navegador
    # navegador.quit()


