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
def replacemultipleinrow(string):
    
    m,n,z=[],['','1','2','3'],0
    while z<len(n):
        bo=string
        m+=[bo.replace(' ',n[z])]
        z+=1
    return(m)
def basefa3mpden(text):
    l1="ايآئابپتث123$#?!,.؟٬:٫﷼٪×،*)("
    l2="جچحخدذرزژسشصض456"
    l3="ظطعقغکفگلمنیوهی789"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    waxee=[]
    for i in textew:
        if i in testp1:
            be="1"
            de='3'
        elif i in testp2:
            be="2"
            de='2'
        elif i in testp3:
            be="3"
            de='1'
        else:
            be=i
            de=i
        mexae=mexae+[be]
        waxee=waxee+[de]
   
    a=(replacemultipleinrow(("".join(mexae))))
    b=replacemultipleinrow(("".join(waxee)))
    for c in b:
        a.append(c)
    return(a)
def basefa3Rmpden(text):
    l1="369يئيآاجچحخطظعغ"
    l2="852بپتثدذرزژفقکگلم"
    l3="147سشص.ضنوه?.,!؟ی‌"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    textew=[chr for chr in text]
    mexae=[]
    waxee=[]
    for i in textew:
        if i in testp1:
            be="1"
            de='3'
        elif i in testp2:
            be="2"
            de='2'
        elif i in testp3:
            be="3"
            de='1'
        else:
            be=i
            de=i
        mexae=mexae+[be]
        waxee=waxee+[de]
    a=(replacemultipleinrow(("".join(mexae))))
    b=replacemultipleinrow(("".join(waxee)))
    for c in b:
        a.append(c)
    return(a)
def validtext(aaa):
    a,m,n=0,[],1
    while a<len(aaa):
        e=aaa[a]
        f=aaa[a+1]
        a+=2
        if e==f:
            c=e+f
            if c not in m:
                m+=[c]
                n+=1
                if n>3:
                    a=len(aaa)+1
                    return True
def assignit(string):
    a=['.','!','?']
    b=['1',0,'2',0,'3',0]
    for i in string:
        b[b.index(i)+1]=b[b.index(i)+1]+1
    n,m,f=1,[],0
    while n<=len(b):
        m+=[b[n]]
        n+=2
    m.sort(reverse=True)
    for k in m:
        string=string.replace(b[b.index(k)-1],a[f])
        f+=1
    return(string)
def decodeook(aaa):
    ook=[('+','..'),('-','!!'),('>','.?'),('<','?.'),('[','!?'),(']','?!'),('.','!.'),(',','.!')]
    a,l=0,[]
    
        #return False
    while a<len(aaa):
        b=0
        while b<len(ook):
            if aaa[a:a+2]=='??':
                a=a+2
            
            elif aaa[a:a+2]==ook[b][1]:
                l+=[ook[b][0]]
                a+=2
                b=1000
                
            b+=1    
    return(''.join(l))
def checkvalid2(string):
    c,d,m=0,0,0
    #print(string)
    for i in string:
        if i=='[':
            if d<=c:
                c+=1
                m=1
            else:
                return False
        if i==']':
            d+=1
            m=0
    if d==c and m==0:
        return True
    else:
        return False
def formatter(string,semi):
    
    a=',.+-<>[]'
    b='?!؟.'
    k,z,m=0,[],[]
    for i in string:
        if i in a:
            z+=[(i,k)]
        elif i in b:
            m+=[(i,k)]
        k+=1
    semi=[chr for chr in semi]
    if len(semi)==len(string):
        for f in m:
            semi[f[1]]=f[0]
        return(''.join(semi))
def stepe(string,semi):
    if len(string)==len(semi):
        return(string,semi)
    else:
        string=string.replace(' ','')
        return(string,semi)
def justcheck(ing):
  neee=[ing,ing[::-1]]
  for string in neee:
    m=[]
    for j in (basefa3Rmpden(string)):
        if j not in m:
            m+=[j]
    for z in basefa3mpden(string):
        if z not in m:
            m+=[z]
    for i in m:
       #print(i) 
       lo=assignit(i)
       llll=(stepe(string,lo))
       #print(llll[0])
       #print(llll[1])
       la=formatter(llll[0],llll[1])
       fff=[lo,la]
       for lm in fff:
          
          if len(lm)%2==0:
            a=(decodeook((lm)))
            if checkvalid2(a):
                print('######')
                print(a)
            if checkvalid2(a[::-1]):
                print('######')
                print(a[::-1])

justcheck(string)

#its really wierd as i forget where i should not change the ? mark, ! or , that its self in the algo!

def base10Menfa(string):
    a=['','‌1','2بپتث','3ايآ','4سشصض','5دذرزژ','6جچحخ','7نوهی','8فقکگلم','9طظعغ']
    string=[chr for chr in string]
    j=''
    for i in string:
        
        z=0
        while z<10:
            
                
            if i in a[z]:
                j=j+str(z)
                z=10
            z=z+1
            if z==10:
                bbb=[' ']
                if i in bbb:
                    j=j+'!'
                else:
                    j=j+str(i)
    return(j)
    #print(j[::-1])
def stupidtest(string):
    string=[chr for chr in string]
    b=['1','2','3','4','5','6','7','8','9']
    d=''
    for i in string:
        if i in b:
            z=0
            while z<int(i):
                d+='.'
                z+=1
        else:
            d+=i
    print(d)
    
#stupidtest(base10Menfa(string))
def counttap(text):
    l1=" ابچدسطفن"
    l2="پجذشظقه"
    l3="تحرصعکو"
    l4="خزضغگی"
    l5="ثژل"
    l6="م"
    testp1=[chr for chr in l1]
    testp2=[chr for chr in l2]
    testp3=[chr for chr in l3]
    testp4=[chr for chr in l4]
    testp5=[chr for chr in l5]
    testp6=[chr for chr in l6]
    textew=[chr for chr in text]
    mexae=[]
    for i in textew:
        if i in testp1:
            be="1"
        elif i in testp2:
            be="2"
        elif i in testp3:
            be="3"
        elif i in testp4:
            be="4"
        elif i in testp5:
            be="5"
        elif i in testp6:
            be="6"
        else:
            be=i
        mexae=mexae+[be]
    #print(mexae)    
    return("".join(mexae))
#counttap(string)
from itertools import permutations
import re
perm = permutations(['1','2','3','4','5','6'])
ving=['.','!','?',',','','','']
logicalpose=[('1','+'),('3','-')]
perm=['2','4']
remainpose=['<','>','.']
def logicalattack(string):
    z,f=[],[]
    string=string.replace('1','+').replace('3','-')
    perm = permutations(['<','>','.',','])
    pose=['2','4','6']
    bing=string
    for i in perm:
        z+=[bing.replace(pose[0],i[0]).replace(pose[1],i[1]).replace(pose[2],i[2])]
    allpos=['.',',','[',']','<','>','+','-','!','?','.','']
    for L in z:
        for J in allpos:
            f+=[L.replace('5',J)]
    return(f)
def stupidfinaltest(string):
    z,m,k=0,[],0
    ook=[('+','..'),('-','!!'),('>','.?'),('<','?.'),('[','!?'),(']','?!'),('.','!.'),(',','.!')]
    fook=['..','!!','.?','?.','!?','?!','!.','.!']
    while z<len(string):
        if string[z:z+2] in fook:
            m+=[ook[fook.index(string[z:z+2])][0]]
            z+=2
        elif string[z:z+2]=='??':
            z+=2
        else:
            m+=[string[z]]
            z+=1
    return(m)
def testitnow(vy):
    wy=[vy,vy[::-1]]
    ha=[]
    for string in wy:
        for i in logicalattack(counttap(string)):
            if checkvalid2(i):
                ha+=[i]
            if checkvalid2(i[::-1]):
                ha+=[i]
    n=set(ha)
    for ik in n:
        print(ik)
        #my_function(ik)

def my_function(string):
    hello = brainfuck.to_function(string)
    start_time = time.time()
    result = hello()
    elapsed_time = time.time() - start_time
    if elapsed_time > 1 or result:
        print("Function executed successfully.")
    else:
        print("Function took too long to execute or didn't produce any output.")
        #sys.exit(0)
        #break
stupidfinaltest(string)
