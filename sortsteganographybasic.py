import re
def listit(string):
    string=[chr for chr in string]
    return(string)
def firstlast(string):
    return(string[0],string[-1])
def ordnum(string):
    return(ord(firstlast(string)[0]),ord(firstlast(string)[1]))
def alphbaword(string):
    string=listit(string)
    string.sort()
    return(''.join(string)) 
def lenobj4(string):
    string=string.split(' ')
    c=[]
    for i in string:
       c+=[{'item':i,'len':len(i)}]
    return(c)
string='they bother me alot, thats why.'

print(alphbaword(string))
print(alphbaword(string))
def ek(string):
    m=''
    for i in string:
        if i not in m:
            m+=i
    return(m)
def lenobj(string):
    string=string.split(' ')
    c=[]
    for i in string:
       c+=[{'item':i,'len':len(i),'alphabet':ek(i),'firsta':firstlast(i)[0],'lastal':firstlast(i)[1],'ordnu':ordnum(i)[0],'ordnumla':ordnum(i)[0]}]
    return(c)
def sortordfa(e):
    return(e['ordnumla'])
def sortoflast(e):
    return(e['ordnumla'])
def sortlen(e):
    return(e['len'])
def sortfirst(e):
    return(e['firsta'])
def sortlast(e):
    return(e['lastal'])
def sortalphabet(e):
    return(e['alphabet'])
def returnfirstitemvalue(e):
    return(e['item'])
def sortedprit(string):
##    z=''
    b=[]
    for i in string:
        b+=i['alphabet']
    print(''.join(b))
string='its not funny.'
def mistrin(string):
    string=string.split(' ')
    m=[]
    for i in string:
        if i not in m:
            m+=[i]
    return(' '.join(m))
def soriti(string):
    semi=['item','len','alphabet','firsta','lastal']
    listit=lenobj(string)
##    print(listit)
    slen=(sorted(listit,key=sortlen))
    sofirst=(sorted(listit,key=sortfirst))
    solast=(sorted(listit,key=sortlast))
    soalphabet=(sorted(listit,key=sortalphabet))
    soitem=(sorted(listit,key=returnfirstitemvalue))
    sortordfae=(sorted(listit,key=sortordfa))
    sortoflaste=(sorted(listit,key=sortoflast))
    superlist=[slen,sofirst,solast,soalphabet,soitem,sortoflaste,sortordfae]
##    listit.sort(key=sortlen)
##    for bbb in superlist:
##    for ccc in soitem:
    for i in superlist:
        sortedprit(i)
soriti(mistrin(string.lower()))


