from email.mime.multipart import MIMEMultipart as email
from email.mime.text import MIMEText
from smtplib import SMT 

message = email 
message["from"] = "Koji Bello"
message["to"] = "kojibello058@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

# with smtplip.SMTP(host="smtp.gmail.com", post=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("kojibello058@gmail.com", "12407819253")
#     smtp.send_message(message)
#     print("Sent...")
