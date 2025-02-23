# pip install anticaptchaofficial 
# pip install webdriver_manager 
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# recaptchav2proxyless este trecho de código varia conforme o captcha específico que se deseja quebrar, está na doc oficial
from anticaptchaofficial.recaptchav2proxyless import *
import time
from chave import chave_api
# chave é o arquivo que deve conter a chave da api do anti-captcha.com
# anticaptcha é um serviço pago que possui uma api. Paga-se por captcha quebrado


navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://google.com/recaptcha/api2/demo"
navegador.get(link)


solver = recaptchaV2Proxyless()
# set_verbose - recebe 0 ou 1. Quando 1, envia um registro dos acontecimentos em tempo real, deixando registrado
solver.set_verbose(1)
solver.set_key(chave_api)
solver.set_website_url(link)

# o atributo data-sitekey está normalmente dentro da div pai do captcha e é utilizado para validar o captcha
chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')
solver.set_website_key(chave_captcha)

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print(resposta)
    # preencher o campo do token do captcha - normalmente fica escondido
    # g-recaptcha-response
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string)

time.sleep(100)