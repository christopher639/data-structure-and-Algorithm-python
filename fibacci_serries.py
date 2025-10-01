list  = []
a ,b = 0 ,1
while a < 10:
    print(a )
    list.append(a)
    a ,b = b, a+b 
print(list)
print(sum(list))