import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from defin_recto2 import*

smtp_port = 587
smtp_server = "smtp.gmail.com"
email_from = "recto.entreprise@gmail.com"

subject = "Alerte securité"

att=[]
fichiers= os.listdir()
for dossier in fichiers:
    if dossier[0:6]== 'picsec':
        att.append(dossier)

def send_emails(email_list,pswd):

    for person in email_list:
        body = f"""
        Attention‼️ 
        Une personne tente de se connecter à votre recto sur votre ordinateur personnel.
            Voici les photos prises par votre camera:
        """
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        #filename = "random_data.csv"
        for dox in att :
            try:
                with open(dox, 'rb') as attachement:
                    # Open the file in python as a binary
                    #attachment= open(att, 'rb')  # r for read and b for binary
                    # Encode as base 64
                    attachment_package = MIMEBase('application', 'octet-stream')
                    attachment_package.set_payload(attachement.read())
                    encoders.encode_base64(attachment_package)
                    attachment_package.add_header('Content-Disposition', f"attachment; filename={dox}")
                    msg.attach(attachment_package)
            
            except Exception as e:
                print("erreur dans l'incertion des fichiers",e)
                pass

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        TIE_server.sendmail(email_from, person, text)

    # Close the port
    TIE_server.quit()