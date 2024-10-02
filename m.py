import mailtrap as mt

mail = mt.Mail(
    sender=mt.Address(email="hello@demomailtrap.com", name="Mailtrap Test"),
    to=[mt.Address(email="cyrushaykay@gmail.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
    category="Integration Test",
)

client = mt.MailtrapClient(token="d02ddb85964bd00652193400bae0cfd4")
response = client.send(mail)

print(response)