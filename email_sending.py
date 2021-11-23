import smtplib

def send_message(message="hello my friend"):

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("dimitar.ivanov.new@gmail.com", "Qazwsxedc@1")
    server.sendmail("dimitar.ivanov.new@gmail.com", "dimiturivanov92@gmail.com", message)

    server.quit()