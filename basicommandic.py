def openfileandread(name):
   a=[]
   z=''
   with open(name, 'r') as file1:  
     for line in file1:
          needle1 = (line.strip())
          needle2=needle1.split('–')
          if len(needle2)>1:
              a=a+[str(needle2[0]).replace(' ','')]+[str(needle2[1])]
              z+=str([str(needle2[0]).replace(' ','')])
   return(a)
def osie(name):
   a=[]
   z=''
   with open(name, 'r') as file1:  
     for line in file1:
          needle1 = (line.strip())
          needle2=needle1.split('–')
          if len(needle2)>1:
              a=a+[str(needle2[0]).replace(' ','')]+[str(needle2[1])]
              z+=str([str(needle2[0]).replace(' ','')])
   return(a)
dicname='cleanfile'
dic=(openfileandread(dicname))
def dictest(string):
    k,z,n,x,fe=0,'',0,len(string),0
    evaluato=''
    info=[]
    for i in dic:
        if k%2==0:
            if i in string:
                evaluato+=i+','
                info=info+[str(i),str(dic[k+1])]
                z=z+i
                n+=1
                fe+=(len(i)**2)
        k+=1        
        if k==len(dic):
            x=((len(z)+fe))/len(string)*n
            if n>1 and x>0:
                print(x,evaluato,info)
                print(string)

def simpledict(name):
   a=[] 
   with open(name, 'r') as file1:
      for line in file1:  
        needle1 = (line.strip()).lower()
        if len(needle1)>3:
            a+=[needle1]
   return(a)
def stringtocheck(name):
    with open(name, 'r') as file1:
      for line in file1:  
        needle1 = (line.strip())
        fix=(re.sub(r'^[a-zAZ]','',needle1)).lower()
        dictest(fix)
        dictest(fix[::-1])
def simpledickchecker(string,dictu):
    z,k,m,l=' ',1,[' ',],len(string)
    for i in dictu:
        if i in string:
            z+=i
            k+=1
            m+=[i]
    if len(m)>7 and (((len(z)*k))/(len(m)*l))>0.50:
        print('source= ',string,'word= ',' '.join(m),k,((len(z)*(len(string)))/(len(m)*k)))
def filecheck(name,dictr):
    dictu=simpledict(dictr)
    with open(name,'r') as file11:
        for line in file11:
            line=(re.sub(r'^[a-zAZ]','',line)).lower()
            simpledickchecker(line,dictu)
            simpledickchecker(line[::-1],dictu)
##filecheck('Newewe','newdic.txt')    
dicname=simpledict('dictionary.txt')
#dicname=simpledict('abstract')
'''
with open('testfile','r') as file2:
    for i in file2:
        simpledickchecker(i.lower(),dicname)
        #dictest(i[::-1].lower())
'''
