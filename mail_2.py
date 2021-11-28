import smtplib
import optparse

def user_input():

	nesne = optparse.OptionParser()
	nesne.add_option("-g" , "--gmail" , dest = "gmail" , help = "enter your gmail account")
	nesne.add_option("-p" , "--password" , dest = "password" , help = "enter your gmail password")
	nesne.add_option("-r" , "--receiver" , dest = "receiver" , help = "enter receiver gmail account")
	nesne.add_option("-m" , "--message" , dest = "message" , help = "enter your message")

	return nesne.parse_args()
	
def sending_mail(gmail , password , receiver , message):

	mail_server = smtplib.SMTP("smtp.gmail.com" , 587)
	mail_server.starttls()
	mail_server.login(gmail , password)
	mail_server.send(gmail , receiver , message)
	mail_server.quit()
	
(user_inputs , arguments) = user_input()

gmail = user_inputs.gmail
password = user_inputs.password
receiver = user_inputs.receiver
message = user_inputs.message

sending_mail(gmail , password , receiver , message)

