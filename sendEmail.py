import os
import smtplib
import email.message
from dotenv import load_dotenv

load_dotenv()


class SendEmail(object):
    def __init__(self, coteudo):
        self.conteudo = coteudo
        self.smtp_server = "smtp.gmail.com"
        self.email_login = os.environ.get('LOGIN_EMAIL')
        self.email_password = os.environ.get('PASSWORD_EMAIL')
        self.destinatario = os.environ.get('REMETENT_EMAIL')
        self.subject = 'Jogos na promoção'
        self.port = 587

    def transform_content_in_html(self):
        html = """
        <!doctype html>
        <html lang="pt-br">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Bootstrap demo</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        </head>
        <body>
            <table class="table table-dark table-striped">
            <thead>
                <tr>
                <th>Nome</th>
                <th>Preço</th>
                <th>Link</th>
                </tr>
            </thead>
            <tbody>
        """
        for item in self.conteudo:
            li = f"""
            <tr>
                <td>{item['nome']}</td>
                <td>R${item['price']}</td>
                <td>{item['link']}</td>
            </tr>
            """
            html += li
        html += """
            </tbody>
            </table>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
            </body>
        </html>
        """
        return html

    def send_email(self):
        try:
            message = self.transform_content_in_html()
            msg = email.message.Message()
            msg['Subject'] = self.subject
            msg['From'] = self.email_login
            msg['To'] = self.destinatario
            msg.add_header("Content-Type", "text/html")
            msg.set_payload(message)

            s = smtplib.SMTP(f"{self.smtp_server}: {self.port}")
            s.starttls()
            s.login(self.email_login, self.email_password)
            s.sendmail(msg['From'], [msg['To']],
                       msg.as_string().encode('utf-8'))
            print('Oba, E-mail enviado com sucesso')
        except Exception as error:
            print("Ocorreu um erro")
            print(error)
