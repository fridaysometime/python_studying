import random,string
import redis

str=string.ascii_letters + string.digits

def gene_token(n,length):
    file=open('token.txt','w')
    for i in range(n):
        token=""
        for j in range(length):
            token+=random.choice(str)
        yield token

def  save_in_redis():
    r=redis.Redis(host='127.0.0.1',port='6379',password='xulin')
    token=gene_token(200,20)
    p=r.pipeline()
    for t in token:
        p.sadd('t',t)
    p.execute()
    return r.scard('t')

if __name__=='__main__':
     save_in_redis()
