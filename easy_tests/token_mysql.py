import random,string
import mysql.connector

str=string.ascii_letters + string.digits

def gene_token(n,length):
    file=open('token.txt','w')
    for i in range(n):
        token=""
        for j in range(length):
            token+=random.choice(str)
        file.write(token+'\n')
    file.close()
def  save_in_mysqlDB():
    DB=mysql.connector.connect(user='root',password='1',database='test')
    cursor=DB.cursor()
    token=gene_token(200,20)
    for t in token:
        cursor.execute("insert into 't'('t') values(%s)",params=[t])
    DB.commit()
    cursor.close()

if __name__=='__main__':
     save_in_mysqlDB()
