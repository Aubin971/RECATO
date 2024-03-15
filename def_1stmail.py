from email.message import EmailMessage
import ssl
import smtplib

Subject = 'Alerte securité'

def send_1stmail(email_list,pswd):
    for person in email_list:
        email_sender = 'recto.entreprise@gmail.com'

        body = """
        Attention‼️: 
            Une personne tente de se connecter à votre recto sur votre ordinateur personnel.
                Si il ne s'agit pas de vous, prenez d'immédiates mesures.
                Dans le cas contraire, vous reprendrez le controle de votre application dans 80 secondes
            Dans 1 minute nous vous enverons un second mail avec plusieurs photos prises par la camera de votre ordinateur.
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = person
        em['Subject'] = Subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,pswd)
            smtp.sendmail(email_sender,person,em.as_string())