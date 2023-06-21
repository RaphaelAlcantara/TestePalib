import pyautogui as pyautogui
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement

import geradorPessoas as Gp
import time
import logging

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
    mensagem = navegador.find_element(By.XPATH, '/html/body/div[5]/span[3]').text

    assert mensagem == "Usuario cadastrado com sucesso!"
    logging.info('Teste de cadastro de usuário com dados válidos finalizado com sucesso')
    num_tests_passed += 1

    logging.info('-' * 50)

    # Teste de login com sucesso
    logging.info('Iniciando teste de login com dados válidos')

    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt12"]').click()
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt12"]').send_keys(cpf)
    time.sleep(0.5)

    #preenche a senha
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').click()
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').clear()
    navegador.find_element('xpath', '//*[@id="input_formLogin:j_idt14"]').send_keys(senha)

    time.sleep(0.5)

    navegador.find_element('xpath', '//*[@id="formLogin:j_idt18"]').click()

    msgloginNome = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/b[1]').text
    msgloginCpf = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/b[2]').text

    assert msgloginNome == nome
    assert msgloginCpf == cpf

    logging.info('Teste de login com dados válidos finalizado com sucesso')

    num_tests_passed += 1

    logging.info('-' * 50)

    # Teste de adição de livros
    logging.info('Iniciando teste de adição de livros')
    #Entrou no sistema admin
    navegador.find_element('xpath', '/html/body/div[1]/div/div[2]/a[3]').click()
    navegador.find_element('xpath', '//*[@id="formIndexLivro:j_idt7"]').click()
    #Nome do livro
    nomeLivro = 'Livro de teste'
    navegador.find_element('xpath', '//*[@id="input_formCadLivro:TabDadosLivro:j_idt10"]').click()
    navegador.find_element('xpath', '//*[@id="input_formCadLivro:TabDadosLivro:j_idt10"]').send_keys(nomeLivro)
    #Autor do livro
    navegador.find_element('xpath', '//*[@id="input_formCadLivro:TabDadosLivro:j_idt12"]').click()
    navegador.find_element('xpath', '//*[@id="input_formCadLivro:TabDadosLivro:j_idt12"]').send_keys('Autor de teste')
    #Sinopse do livro
    navegador.find_element('xpath', '//*[@id="input_formCadLivro:TabDadosLivro:j_idt14"]').click()
    navegador.find_element('xpath', '//*[@id="input_formCadLivro:TabDadosLivro:j_idt14"]').send_keys('sinopse de teste')
    time.sleep(1)

    #Valor do livro
    navegador.find_element('xpath', '//*[@id="formCadLivro:TabDadosLivro:j_idt16_input"]').click()
    navegador.find_element('xpath', '//*[@id="formCadLivro:TabDadosLivro:j_idt16_input"]').send_keys(Keys.BACK_SPACE * 4)
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="formCadLivro:TabDadosLivro:j_idt16_input"]').send_keys(
        "4,24")


    #Categoria do livro
    navegador.find_element('xpath', '//*[@id="input_formCadLivro:TabDadosLivro:j_idt18"]').click()
    navegador.find_element('xpath', '//*[@id="input_formCadLivro:TabDadosLivro:j_idt18"]').send_keys('categoria de teste')

    #clica no botão proximo
    navegador.find_element('xpath', '//*[@id="formCadLivro:TabDadosLivro:j_idt24"]').click()
    time.sleep(1)

    #fazendo upload da imagem

    upload_img = navegador.find_element('xpath', '//*[@id="formCadLivro:TabUploadsLivro:fotoUploader_label"]')
    upload_img.click()
    time.sleep(1)
    pyautogui.write('G:\ProjetosPython\pythonProject\pythonProject\TestePalib\imgTeste.jpg')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)
    navegador.find_element('xpath', '/html/body/div[2]/div/div/div[2]/form/div/div/div[2]/div/div/div/div/div[1]/div[1]/button[1]/span[2]').click()

    assert navegador.find_element('xpath', '/html/body/div[2]/div/div/div[2]/form/div/div/div[2]/div/div/div/div/h6').text == 'Foto Adicionada'


    #upload do arquivo pdf
    upload_pdf = navegador.find_element('xpath', '//*[@id="formCadLivro:TabUploadsLivro:pdfUploader_label"]')
    upload_pdf.click()
    time.sleep(1)
    pyautogui.write('G:\ProjetosPython\pythonProject\pythonProject\TestePalib\pdfTeste.pdf')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)
    navegador.find_element('xpath', '/html/body/div[2]/div/div/div[2]/form/div/div/div[2]/div/div/div/div/div[2]/div[1]/button[1]/span[2]').click()
    assert navegador.find_element('xpath', '/html/body/div[2]/div/div/div[2]/form/div/div/div[2]/div/div/div/div/h6[2]').text == 'Upload de PDF concluido'

    #clica no botão inserir
    navegador.find_element('xpath', '//*[@id="formCadLivro:TabUploadsLivro:j_idt28"]').click()
    time.sleep(1)

    #verificar se o texto está na página
    assert navegador.find_element('xpath', "//*[contains(text(),'Livro de teste')]")
    num_tests_passed += 1

    logging.info('Teste de adição de livros finalizado com sucesso')
    logging.info('-' * 50)

    navegador.find_element('xpath', '/html/body/div[1]/div/a').click()




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


