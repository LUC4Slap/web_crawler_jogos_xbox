from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from parserJogo import ParserJogo
from sendEmail import SendEmail
from selenium.common.exceptions import NoSuchElementException

navegador = webdriver.Chrome()

navegador.get('https://www.xbox.com/pt-BR/games/all-games?xr=shellnav')
sleep(20)

# Selecionando 200 por pagina
navegador.find_element(
    By.XPATH, '//*[@id="unique-id-for-paglist-generated-select-menu-trigger"]').click()
select_200 = navegador.find_element(
    By.ID, 'unique-id-for-paglist-generated-select-menu-3').click()
sleep(5)

all = []
while True:
    try:
        next = navegador.find_element(By.CLASS_NAME, 'paginatenext')
    except NoSuchElementException:
        print('Fim da paginação')
        break

    try:
        parse = ParserJogo(navegador.page_source)
        response = parse.parser_jogo()
        all.extend(response)
        print(f"Promoções da pagina: {len(response)}")
        next.click()
        sleep(5)
    except Exception as error:
        print('Fim da paginação')
        break

print(len(all))
email = SendEmail(all)
email.send_email()
