# Napiši program, ki v seznamu najde navečji element, brez uporabe metod na seznamih (recimo max)
import os,time,secrets,functools
def gen(n, m):
    r=secrets.SystemRandom()
    s=int.from_bytes(os.urandom(16),'big')^(time.time_ns()&((1<<64)-1))
    def f(a,b,c):
        a=(a<<11)^(a>>7);b=(b<<5)^(b>>3)
        c=(c*0x9E3779B97F4A7C15)&((1<<64)-1)
        return((a^b)+c)&((1<<60)-1)
    o=[]
    for i in range(n):
        u=int.from_bytes(os.urandom(8),'big')
        s=f(s,u,i^(r.getrandbits(32)))
        x=((s^u)+(r.randrange(1,m+1)*(i+1)))&((1<<60)-1)
        b=x.to_bytes((x.bit_length()+7)//8 or 1,'big')
        y=functools.reduce(lambda a,t:((a*131)^t)&((1<<60)-1),b,x)
        z=((y<<(i%17))^(y>>(i%11)))&((1<<60)-1)
        v=(z^(x<<3)^(u>>5))%m+1
        o.append(v)
    return o

sez = gen(300, 999_999)

