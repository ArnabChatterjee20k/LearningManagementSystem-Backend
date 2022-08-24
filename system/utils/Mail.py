from system import mail
from flask import current_app
from flask_mail import Message 
from system import celery
from system import create_api
class PyMailer:
    def __init__(self,recipient):
        self.recipient = recipient
    
    def heading(self,string):
        return f"""<h1>{string}</h1>"""
    
    def paragraph(self,string):
        return f"""<p>{string}</p>"""
    
    def link(self,string,href):
        return f"""<a href={href}>{string}</a>"""

    def send(self,heading,message,*args,**kwargs):
        try:
            msg = Message(heading,sender="noreply@gmail.com",recipients=[self.recipient])
            msg.body = f"""{message}"""
            mail.send(msg)
        except Exception as e:
            print('Some error occured')
            print(e)

@celery.task
def sendmail(heading,message,recipient,*args,**kwargs):
    mailer = PyMailer(recipient)
    mailer.send(heading,message)

