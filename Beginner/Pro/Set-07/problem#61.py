#One-time pad +1
plain = input()
key = input()
l=[]
nig = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
for i in range(len(plain)):
    l.append(((nig[plain[i]]+nig[key[i]])%26)+1)
print(l)
for k in l:
    for i, j in nig.items():
        if j == k:
            print(i,end="") 
