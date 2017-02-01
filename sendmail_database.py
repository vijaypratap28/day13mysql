import MySQLdb as m
import smtplib
import getpass


host='localhost'
username='root'
password='root123'
database='mydb'
db_con=m.connect(host,username,password,database)
#db_cur=db_con.cursor()
db_cur=db_con.cursor(m.cursors.DictCursor)
sql="select * from info"
db_cur.execute(sql)
data=db_cur.fetchall()
#print data
str1=""
for line in data:
	print line
	cur = "{id} {name} {qualification} {mobileno}".format(**line)
	str1 = str1 + cur +"\n"
	dictlist=[]
print str1
host="smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username=raw_input("gmail")
password=getpass.getpass()
server.login(username,password)
to=raw_input("to")
sub=raw_input("sub")
#mes=raw_input("messege")
message=str1
server.sendmail(username,to,message)

