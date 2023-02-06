# Web Crawler

![bot](https://files.tecnoblog.net/wp-content/uploads/2018/07/bot-twitter.jpg)

## Feito para pesquisar os jogos que estão em promoção no site da xbox

### Para fazer funcionar pasta rodar o comando

```python
  python3 crawler.py
```

Esse comando fara uma busca com o selenium e trara o resultado de todas as paginas do site, aplicando a quantidade de 200 jogos por pagina e pegando em cada pagina os jogos que estão em promoção e no final de tudo é mandado um e-mail com um tabela que contem todos os jogos que estão com a tag promoção, nesse tabela é mandado o nome do jogo o preço da promoção e o link direto do jogo para não precisar procurar na listagem do site e ja ir direto para a pagina no jogo.

## Confirgura o e-mail

Para conseguir fazer o uso do envio de email tem que criar uma conto no gmail, ativar a opção de autenticação de dois fatores e depois ir em senha de apps e gerar uma senha para que o python possa usar.
![Autenticação de dois fatores](https://snov.io/knowledgebase/wp-content/uploads/2022/12/2022-11-29_14-02-19-1.png)

## TO DO

- [x] Criar Projeto
- [x] Fazer o Scraping da primeira pagina do jogo
- [x] Fazer o parser dos dados puros para um formato fora do html do site
- [x] Fazer a classe para mandar o email
- [x] Fazer uma função na classe de mandar email que converte os dados da lista em uma lista html
- [x] Fazer o scraping das demais paginas
- [ ] Fazer a ação no github actions para executar este codigo uma vez no dia como mostra no video [aqui](https://www.youtube.com/watch?v=dfLKUwb-roA&ab_channel=Codifike).
