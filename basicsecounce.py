import re
def simpledict(name):
   a=[] 
   with open(name, 'r') as file1:
      #z=0 
      for line in file1:  
        needle1 = (line.strip()).lower()[::-1]
        #z+=1
        if len(needle1)>3:
            a+=[needle1]
   return(a)
def faster(name):
    z=''
    with open(name, 'r') as file1:
        for line in file1:
            z+=line.strip().replace(' ','').lower()
    return(z)
oeis=faster('names')
wordto=simpledict('dic')
def testarrange(fr,to):
    x=[]
    for i in fr:
        x+=[[len(re.findall(i,to)),i]]
    x.sort(key=lambda x: x[0],reverse=True)
    #x.sort(reverse=True)
    #print(x[0:10])
    return(x)

for i in testarrange(stre,oeis):
    print(i)
