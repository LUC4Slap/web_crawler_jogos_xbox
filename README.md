# Web Crawler

## Feito para pesquisar os jogos que estão em promoção no site da xbox

### Para fazer funcionar pasta rodar o comando

```python
  python3 crawler.py
```

esse comando fara uma busca com o selenium e trara o resultado por enquanto somente da primeira pagina do site os 200 primeiros jogos que estão com alguma promoção ativa e depois enviara um e-mail com uma lista contendo o nome do jogo, preço e um link direto para a pagina do jogo no site.

## TO DO

- [x] Criar Projeto
- [x] Fazer o Scraping da primeira pagina do jogo
- [x] Fazer o parser dos dados puros para um formato fora do html do site
- [x] Fazer a classe para mandar o email
- [x] Fazer uma função na classe de mandar email que converte os dados da lista em uma lista html
- [x] Fazer o scraping das demais paginas
- [ ] Fazer a ação no github actions para executar este codigo uma vez no dia como mostra no video [aqui](https://www.youtube.com/watch?v=dfLKUwb-roA&ab_channel=Codifike).
