from email.message import EmailMessage
import ssl
import smtplib
from defin_recto2 import lire_csv_recto

Subject = 'Perte de votre mot de passe'
pswrd = (lire_csv_recto("recto_mail_.csv"))[0]
concombre = (lire_csv_recto("addresse_mailset.rct"))

def send_email(email_list):
    for person in email_list:
        email_sender = 'recto.entreprise@gmail.com'

        body = f"""
        Voici votre mot de passe : 
        {concombre[2]}
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = person
        em['Subject'] = Subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,pswrd)
            smtp.sendmail(email_sender,person,em.as_string())

send_email([concombre[1]])