import smtplib

gmail = input("enter your gmail account : ")
password = input("enter your gmail password : ")
receiver = input("enter receiver gmail account : ")
message = input("enter your message : ")

def sending_gmail(gmail , password , receiver , message):

	mail_server = smtplib.SMTP("smtp.gmail.com",587)
	mail_server.starttls()
	mail_server.login(gmail , password)
	mail_server.sendmail(gmail , receiver , message)
	mail_server.quit()
	
sending_gmail(gmail , password , receiver , message)
