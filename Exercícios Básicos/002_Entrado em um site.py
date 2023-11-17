from selenium import webdriver
import time


# Atribuindo o webdriver a variável para que execute o método de abrir o Chrome #
driver = webdriver.Chrome()

# Chamando o site que se espera encontrar #
driver.get("https://www.youtube.com/")


# Chamando o método de maximizar a tela quando for executado #
driver.maximize_window()


# Tempo em que o site ficará aberto sem executar ações. Contudo não é uma boa prática,
# posteriormente teremos outras maneiras de fazer isso. #
time.sleep(2)
