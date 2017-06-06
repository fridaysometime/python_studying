import random,string

str=string.ascii_letters + string.digits

def gene_token(n,length):
    file=open('token.txt','w')
    for i in range(n):
        token=""
        for j in range(length):
            token+=random.choice(str)
        file.write(token+'\n')
    file.close()

if __name__=='__main__':
     gene_token(200,20)
