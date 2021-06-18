from ftplib import FTP

hostname = '192.168.0.167'
username = 'orlando'
password = '123mudar'
ftp = FTP(hostname)
ftp.login(user=username,passwd=password)
ftp.cwd('/') 
entries = [] 
ftp.dir(entries.append)
ftp.close() 

for entry in entries:
    print(entry)