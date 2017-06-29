f=open('STVincludeYYY.dat','r')
b=f.read()
f.close()
b=b.split('\n')

for i in range(0,len(b)-1):
    b[i]=b[i].split()
    if (b[i][0].find('OW5102',0))>1:
        b[i][1]='XXX XXX'



s=open('seina_wells.txt','r')
se=s.read()
s.close()
se=se.split('\n')
for i in range(0,len(se)):
    se[i]=se[i].strip()
    se[i]=se[i].replace(' ','_')


fout=open('seinabou.csv','+w')

for i in range(0,len(se)):
    for j in range(0,len(b)):
        if ((se[i].find(b[j][1],0))>=0)and(len(se[i])<=len(b[j][1])):
            fout.write(se[i] + ',' + b[j][0] + ',' + b[j][1] +'\n')
        elif 'NO_'+se[i]== b[j][1]:
            fout.write(se[i] + ',' + b[j][0] + ',' + b[j][1] +'\n')

fout.close()




2:2+len(se[i])