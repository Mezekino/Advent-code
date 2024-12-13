list1=[]
safe=0
flag=True
safe=0

input=open("input.txt","r")

for line in input:
    list1.append((line.split()))
    
for riga in range(len(list1)):
    for colonna in range(len(list1[riga])):
        list1[riga][colonna]=int(list1[riga][colonna])

def controlloCrescente(lista):
    flag=True

    for index in range(len(lista)-1):
        if flag==True and ((lista[index+1]-lista[index] >3)or(lista[index+1]-lista[index] <1)):
            flag=False

    return flag

def controlloDecrescente(lista):
    flag=True

    for index in range(len(lista)-1):
        if flag==True and ((lista[index]-lista[index+1] >3)or(lista[index]-lista[index+1] <1)):
            flag=False

    return flag

for item in list1:
    flag1=False
    for index,item1 in enumerate(item):
        copy=item[0:len(item)]
        copy.pop(index)

        if flag1==False:
            if (controlloCrescente(copy) or controlloDecrescente(copy)):
                flag1=True

    if flag1==True:
        safe+=1
print("le combinazioni sicure sono:",safe)