import smtplib
print("Provide all the information properly and once!")
mail_id = str(input("Enter your email Id: "))
password = str(input("Enter your password: "))

server= smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login(mail_id, password)
send_to = str(input("Enter email id to send them mail: "))
subject = str(input("Subject: "))
body = str(input("Body: "))
msg=f"Subject:{subject}\n\n{body}"
server.sendmail(mail_id, send_to, msg)
print("Your mail is been sent! ")
server.quit()
