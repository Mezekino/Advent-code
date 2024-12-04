list1=[]
list2=[]
list3=[]
somma=0

input=open("input.txt","r").readlines()

for element in input:
    list1.append(int(element.split("   ")[0]))
    list2.append(int(element.split("   ")[1]))

list1.sort()
list2.sort()

for index in range(len(list1)):
    list3.append(abs(list2[index]-list1[index]))

for num in list3:
    somma+=num

print(somma)