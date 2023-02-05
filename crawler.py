from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from parserJogo import ParserJogo

navegador = webdriver.Chrome()

navegador.get('https://www.xbox.com/pt-BR/games/all-games?xr=shellnav')
sleep(20)

# Selecionando 200 por pagina
navegador.find_element(
    By.XPATH, '//*[@id="unique-id-for-paglist-generated-select-menu-trigger"]').click()
select_200 = navegador.find_element(
    By.ID, 'unique-id-for-paglist-generated-select-menu-3').click()
sleep(20)

parse = ParserJogo(navegador.page_source)
response = parse.parser_jogo()
print(response)
