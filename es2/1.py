list1=[]
safe=0
flag=True

input=open("input.txt","r")

for line in input:
    list1.append((line.split()))
    
for riga in range(len(list1)):
    for colonna in range(len(list1[riga])):
        list1[riga][colonna]=int(list1[riga][colonna])

def controlloCrescente(lista):
    flag=True
    for index in range(len(lista)-1):
        if flag==True:
            if lista[index]>lista[index+1] or ((lista[index+1]-lista[index])==0) or ((lista[index+1]-lista[index])>3):
                flag=False
    return flag

def controlloDecrescente(lista):
    flag=True
    for index in range(len(lista)-1):
        if flag==True:
            if lista[index]<lista[index+1] or ((lista[index]-lista[index+1])==0) or ((lista[index]-lista[index+1])>3):
                flag=False
    return flag

for index in range(len(list1)):
    if list1[index][0]>list1[index][1]:
        if controlloDecrescente(list1[index]):
            safe=safe+1
    else:
        if controlloCrescente(list1[index]):
            safe=safe+1

print(safe)