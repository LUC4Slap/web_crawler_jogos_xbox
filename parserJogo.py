from bs4 import BeautifulSoup


class ParserJogo(object):
    def __init__(self, content):
        self.soap = BeautifulSoup(content, 'html.parser')

    def parser_jogo(self):
        busca = self.soap.find_all(
            'div', attrs={'class': 'm-product-placement-item'})
        promos = []

        for item in busca:
            promo = item.find('span', attrs={'class': 'c-badge'})
            if promo == None:
                continue
            promos.append(item)

        parser = []
        for promo in promos:
            try:
                item = {
                    "nome": promo.find('h3', attrs={'class': 'c-subheading-4'}).text,
                    "price": promo.find('span', attrs={'class': 'textpricenew'}).text[3:] or '',
                    "link": promo.find('a', attrs={'class': 'gameDivLink'})['href']
                }

                parser.append(item)
            except Exception as error:
                print("Erro no parser")
                print(error)
                continue

        return parser
