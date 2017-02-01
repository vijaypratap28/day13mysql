import MySQLdb
import smtplib
import getpass


localhost="localhost"
user="root"
password="root123"
database="mydb"

con=MySQLdb.connect(localhost,user,password,database)

cursor=con.cursor()

cursor.execute("select * from info;")
con.commit()
data=cursor.fetchall()
mail_str=''
print "Id:-\t name:-\t Email:-\t"
sr=''
for row in data:
	line="%s\t %s\t %s"%(row[0],row[1],row[2])
	sr=sr+line+'\n'
print sr
host="smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo
username=raw_input("gmail\n")
password=getpass.getpass()
server.login(username,password)
to=raw_input("to\n")
sub=raw_input("sub\n")
mes=data
message="subject: %s\n\n%s"%(sub,sr)
server.sendmail(username,to,message)
con.close()


