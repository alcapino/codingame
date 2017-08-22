import sys
import math

def dectobin(n):
    d=n
    b=[]
    while d>=1:
        r = d%2
        b.append(r)
        d = (d-r)/2
    b.reverse()
    return (''.join(str(e) for e in b)).zfill(7)
    
def encode(s):
    r = ""
    curr_num = 2
    switched = False
    strlist = list(s)
    for i in range(len(strlist)):
        switched = False
        if curr_num != strlist[i]:
            curr_num = strlist[i]
            switched = True
        
        if strlist[i] == "1" and switched:
            r += " 0 "
        elif strlist[i] == "0" and switched:
            r += " 00 "
        
        r += "0"
    return r.strip()

message = raw_input()
ch = list(message)
b = []
for i in range(len(ch)):
    dec = ord(ch[i])
    bin = dectobin(dec)
    b.append(bin)
en = encode(''.join(b))
print ""+en
