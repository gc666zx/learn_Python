a = [1,2,3,4,5,6,7,8]
# print(a[:-2])
tem = a[5]
a[5], a[3] = a[3], a[5]
print(a)
print(a[5])
print(tem)