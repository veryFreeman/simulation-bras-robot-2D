import smtplib
import ssl
from email.message import EmailMessage


class MdpOublieView():
    def __init__(self, receiver):
        self.email_receiver = receiver
        self.email_sender = "florentarnaza@gmail.com"
        self.email_password = "bpcgingujcigdfoz"
        self.subject = "Recuperation du mot de passe"
        self.body = """
                    LES IDENTIFIANT DE CONNEXION À L'APPLICATION :
                    
                            Login : root
                            Mot de passe: root
                    """

    def sendMail(self):
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = self.email_receiver
        em['Subject'] = self.subject
        em.set_content(self.body)
        # Add SSL (layer of security)
        context = ssl.create_default_context()
        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())
        
            return True
