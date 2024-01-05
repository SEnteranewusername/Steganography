import re
from itertools import permutations
def openfile(filename):
    m=[]
    with open (filename,'r') as file1:
        for line in file1:
            line=line.strip()
            m+=[line]
    return(m) 
def callstringoutofclass(string):
    return(string)
def lenbased2key(string):
    string=string.split(' ')
    m=[]
    for i in string:
        m+=[len(i)]
    return(m)
def skipbasedkey(string,keym):
    string=[chr for chr in string]
    z,k=0,0
    m=''
    waht=''
    while (z)<len(string):
        m+=string[(int(keym[(k)%len(keym)])+z-1)%len(string)]
        waht+=string[(int(keym[(k)%len(keym)])+z-1)%len(string)]+'no='+str(z)+'no2='+str(k)
        z,k=z+int(keym[(k)%len(keym)]),k+1
        
    print(m)
    print(m[::-1])
def permofkeyorder(keyorder):
    perm = permutations(keyorder)
    m=[]
    
    for i in perm:
        m+=[i]
    
    return(m)
def datebasekey(string):
    string=re.sub(r'[^0-9]','',string)
    suborder=[]
    z=0
    while z<len(string):
        suborder+=[string[z:z+2]]
        z+=2
    return(permofkeyorder(suborder))


def brutekeydate(string):
    string=re.sub(r'[^0-9]','',string)
    sub1=string[0:4]+string[6:8]
    listfortest=[string,sub1,string[::-1],sub1[::-1]]
    z=[]
    for i in listfortest:
        z+=[datebasekey(i)]
       
    return(z)
def brutefunckeystring(string,a):
    for i in a:
        for b in i:
            skipbasedkey(string,b)
def one23(string):
    string=string.strip()
    string=string.split(' ')
    key=[0,2,4,8,1,2,3]
    z=0
    zw=''
    for i in string:
        zw+=i[key[z%(len(key))]]
        z+=1
    print(zw)


#(brutefunckeystring(b,a))

def twokeyfile(file2,file1):
    string=openfile(file1)
    keys=openfile(file2)
    for i in keys:
        a=lenbased2key(i)
        b=lenbased2key(i[::-1])
        for z in string:
##            z=z.replace(' ','')
            skipbasedkey(z,a)
            skipbasedkey(z,b)
            skipbasedkey(z[::-1],a)
            skipbasedkey(z[::-1],b)
            skipbasedkey(z.replace(' ',''),a)
            skipbasedkey(z.replace(' ',''),b)
            skipbasedkey(z.replace(' ','')[::-1],a)
            skipbasedkey(z.replace(' ','')[::-1],b)
def twokeyfileonebyone(file1,file2):
    string=openfile(file1)
    keys=openfile(file2)
    k=0
    while k<len(keys) and k<len(string):
        z=string[k]
        a=lenbased2key(keys[k])
        b=lenbased2key(keys[k][::-1])
##        print(z)
        skipbasedkey(z,a)
        skipbasedkey(z,b)
        skipbasedkey(z[::-1],a)
        skipbasedkey(z[::-1],b)
        k+=1
        
##twokeyfile('shikh','shikh')
##twokeyfileonebyone('keystrparpar','mystrforpar')
def filebrute(name):
 with open (name,'r') as file1:
    for line in file1:
        text=line.strip()
        #keylayoutbrute(fa,text)
        print(lenbased2key(text))
##filebrute('shikh')
def vernumpadfixshiftenc(string,keya):
    keyorder='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
##    keyorder="یهونملگکقفغعظطضصشسژزرذدخحچجثتپبا"[::-1]
##    keya='money'
    z=''
    k=0
    for i in string:
        n=keyorder.index(i)+keyorder.index(keya[k%(len(keya))])
        k+=1
        if n>(len(keyorder)-1):
            n=n-(len(keyorder))
        z+=keyorder[n]
    print(z)
def decvernumpad(string,keya):
    keyorder='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
##    keyorder="یهونملگکقفغعظطضصشسژزرذدخحچجثتپبا"[::-1]

##    keya='money'
    z=''
    k=0
    for i in string:
        n=keyorder.index(i)-keyorder.index(keya[k%(len(keya))])
        k+=1
        if n<0:
             n=n+(len(keyorder))
        z+=keyorder[n]
    print(z)
b='there were some thing in there'
b=b.strip()
b=b.replace(' ','')
x='بدیهم'
##decvernumpad(b,x)
##vernumpadfixshiftenc(b,x)
print('###########################')
a=(brutekeydate('10/08/2582'))
##brutefunckeystring(b,a)
def openfileaslist(name):
    m=[]
    with open(name,'r') as file1:
        for line in file1:
            m+=[line]
    return(m)
##    return(''.join(m))
def keylistmaker(key):
    a=[chr for chr in key]
    b=[chr for chr in key[::-1]]
    c=(' '.join(map(lambda x: x, [key[i:i+2] for i in range(0, len(key), 2)]))).split(' ')
    d=(' '.join(map(lambda x: x, [(key[::-1])[i:i+2] for i in range(0, len(key), 2)]))).split(' ')
    e=[a,b,c,d]
    return(e)
def stringready(string):
    a=string.strip()
    b=string[::-1]
    c=a[::-1]
    z=[]
    d=[string,a,b,c]
    for i in d:
        z+=[i]
        z+=[i.replace(' ','')]
        z+=[i.replace(' ','').replace('...','.')]
    return(d)
def stringlenman(string):
    z=0
    d=[]
    while z<7:
        d+=[string.rjust(z+len(string),'i')]
        d+=[string.ljust(z+len(string),'i')]
        z+=1
    return(d)
def brutetest(string,key):
    key=keylistmaker(key)
    string=stringlenman(string)
    for i in string:
        b=stringready(i)
        for i in b:
            for z in key:
                skipbasedkey(i,z)
##print(stringlenman('abcdedfg'))

def brutesimple(string,key):
    key=keylistmaker(key)
    string=stringready(string)
    for i in string:
        for z in key:
            skipbasedkey(i,z)
def brutesimpler(string,key):
    z=key
    v=key[::-1]
    key=[z,v]
    string=stringready(string)
    for i in string:
        for z in key:
            skipbasedkey(i,z)    
c='444432'

def choosefromword(string,key):
    string=string.split(' ')
    z=0
    nr,er=0,0
    e=''
    f=''
    nn=''
    ee=''
    while z<len(string):
        if int(key[z%(len(key))])<=(len(string[z])-1):
            e+=(string[z])[int(key[z%(len(key))])]
        if (int(key[z%(len(key))])-1)<=(len(string[z])-1):
            f+=(string[z])[int(key[z%(len(key))])-1]

        if int(key[er%(len(key))])<=(len(string[z])-1):
            ee+=(string[z])[int(key[er%(len(key))])]
            er+=1
        if (int(key[nr%(len(key))])-1)<=(len(string[z])-1):
            nn+=(string[z])[int(key[nr%(len(key))])-1]
            nr+=1
        z+=1
    print(e)
    print(f)
    print(nn)
    print(ee)
#brutesimple(a,b)

##brutesimpler(a,b)
#choosefromword(a,b)
    #step-wise
##vernumpadfixshiftenc('wise','step')
##decvernumpad('wise','step')
##z=openfileaslist('thonny')
def extractorcaps(string):
    m=''
    z=''
    
    for i in string:
        if i.isupper():
            if i not in m:
                m+=i
            z+=i
    print(m)
    print(z)

def simpleskip(string,k):
    string=[chr for chr in string]
    z=''
    while len(string)>=3:
        z+=string[k%(len(string)-1)]
        string.pop(k%(len(string)-1))
        k+=k
    print(z)
##simpleskip(string[::-1],3)
##simpleskip(string,3)
def steghiddendetector(string):
    m=''
    z=''
    n=''
    LETTERS="ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
    for i in string:
      if i not in LETTERS:
        if i.isprintable()==False:
            m+=i
            z+=str(ord(i))+' '
        if ord(i)>255:
            n+=str(ord(i))+' '
##    return(m)
##    return(z)
    print(n)
    print(z)
    print(m)
def sorter(string):
    (string.sort(key=len,reverse=True))
    z=0
    m=''
    for i in string:
        print(i[::-1].replace(' ',''),end='')
        for j in i:
            if j not in m:
                m+=j
    print(m)
##        print(z)
##print((['ali','hasan','booooooooob','sa']).sort())
#z=openfileaslist('testpsh')


##zdn=' کتاباش فیکن، تاریخ قمری و شمسی رو قاطی کرده... تازه این فقط یه ایرادشه.'
awwe=lenbased2key(zdn)
##brutesimpler(amme,awwe)
def getword(string):
    string=string.split(' ')
    z=''
    for i in string:
        z+=i[-1:]
    print(z)
getword(qw3)
def getit(name):
    with open(name,'r') as file1:
        m=''
        for line in file1:
            for b in line:
                 if b.isupper():
                     if b not in m:
                            m+=b
        print(m)
##        print(len(m))
#getit('tesp.txt')
#

def shaskey(key,string):
    c=(' '.join(map(lambda x: str(int(x,16)), [key[i:i+2] for i in range(0, len(key), 2)]))).split(' ')
    me=''
    xe=''
    mme=''
    xxe=''
    for i in c:
        me+=(string[::-1][int(i)%len(string)])
        xe+=(string[int(i)%len(string)])
        mme+=(string.replace(' ','')[::-1][int(i)%len(string.replace(' ',''))])
        xxe+=(string.replace(' ','')[int(i)%len(string.replace(' ',''))])
    print(me)
    print(xe)
    print(mme)
    print(xxe)
        #print(string[int(i)%len(string)],end='')
        #print(string[::-1][int(i)%len(string)],end='')
##shaskey(mewew[::-1],(grew+string))
##shaskey(mewew,(string+grew))
##twokeyfile('ioi','ioip')
def choosingalphabetidso(string,operator):
    z=''
    for i in string:
        if i==operator[0]:
            z+='s'
        elif i==operator[1]:
            z+='e'
        elif i==operator[2]:
            z+=''
        else:
            z+=i
    print(z)
def choosingalphabetidso2(string,operator):
    z=''
    for i in string:
        if i==operator[0]:
            z+='s'
        if i==operator[1]:
            z+='e'
        if i==operator[2]:
            z=''
    print(z)
choosingalphabetidso('''Sym now?''','td ')
string='''Syslem now?'''
a=re.sub(r'[po]','',string)
b=re.sub(r'[p...]','',string)
print(a)
print(b)
def maper(string):
    e=''
    for i in string:
        e+=str(ord(i))
    return(e)
maper('Cal')
string='''SyssroblemXnow?'''
a=re.sub(r'[prt]','',string)
b=re.sub(r'[po blem...]','',string)
print(a)
print(b)
def mappermulti(string):
    string=string.split('X')
    z=1
    for i in string:
        z=int(maper(i))*679711099101108+z
    print(z)
mappermulti(string)
def baseconverter(base,string):
    d=0
    z=len(base)
    string=string[::-1]
    k=0
    for i in string:
       d+=(int(base.index(i)))*z**k
       k+=1
    print(d)
def keyforbase(string):
    m=''
    for i in string:
        if i not in m:
            m+=i
    return(m)
def stupidbaseconverter(base,string):
    z=''
    k=0
    while k<len(string):
        if int((string)[k:k+2])<len(base):
            z+=base[int((string)[k:k+2])]
            k+=2
        else:
            z+=base[int((string)[k:k+1])]
            k+=1
    print(z)
stupidbaseconverter('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/-*<>|','71452010')
def toupperbase(string,base):
    base=[chr for chr in base]
    a=''
    z=int(string)
    while z>len(base):
        a+=base[z%(len(base))]
        z=(z//len(base))
    if z<=len(base):
            a+=base[z]
    print(a[::-1])
toupperbase('124578//8,'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/-*<>|')
base69='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/-*<>|'
baseerw='''-+xSystem progab45451ldc
Duwnh?XC|.'''
baseconverter(base69,'dolphine')
stupidbaseconverter(base69,'555555555')
def testfile():
 with open ('Neweeeeeew','r') as file21:
   for i in file21:
    me=[i,i[::-1]]
    for line in me:
        line=line.strip()
##       try: 
##        toupperbase(line,base69)
##        toupperbase(line,baseerw)
##        stupidbaseconverter(base69,line)
##        stupidbaseconverter(baseerw,line)
##       except:
##           se=3
(keyforbase('''-+xSystem program problem detected
Do you want to report the problem now?X Cancel|port problem...'''))
testfile()

def modclock(string):
    key=['ab01','23cd','4567ef','89']
    z=[]
    for i in string:
        k=-1
        while k<4:
            if i in key[k]:
                z+=[key.index(i)]
                k+=100
            k+=1
    print(z)
def base12(string):
    a=['11','12','13','14', '21', '22', '23', '24', '31','32', '33', '34', '41','42', '43', '44']
    b='123a456b789ce0fd'
    c='e7410852f963dcba'
    d='147e2680369fabcd'
    e='df0ec987b654a321'
##    e='tabcwxyzdeftabcw'
    le0n=0
    bb=''
    cc=''
    dd=''
    ee=''
    while le0n<(len(string)):
        m=string[le0n:le0n+2]
        
        z=0
       
        while z<len(a):
            if a[z]==m:
                bb=bb+b[z]
                cc=cc+c[z]
                dd=dd+d[z]
                ee=ee+e[z]
                z=20
            z=z+1
        le0n=le0n+2
    ae=[bb,cc,dd,ee]
    for iii in ae:
        modclock(iii)
    
