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
        html = "<ul>"
        for item in self.conteudo:
            li = f"""
              <li>
                Nome: <strong>{item['nome']}</strong>
                Preço: {item['price']}
                link: {item['link']}
              </li>
            """
            html += li
        html += "</ul>"
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
