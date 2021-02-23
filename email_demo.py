import smtplib, ssl, json

recever = 'mgoodaman@gmail.com'

port = 465

with open('/Users/AlexGoodman/Documents/Coding Course/SQL practice/email_credentials.json', 'r') as credentials: 
    creds = json.loads(credentials.read()) 
    password = creds['password'] 
    email_address = creds['email_address']

print(email_address)


message = "Howdy there space cowboy, were you expecting this email?"

context = ssl.create_default_context()

print('creating server')
with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(email_address, password)
    server.sendmail(email_address, recever, message)

print('sent email')