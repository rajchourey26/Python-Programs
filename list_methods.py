
print("\nlist method")
list=[2,3,4,5,6,7]
list01=[8,9,10]
list.append(8) #this will change the original list
list.pop()#it will remove last element here 8
list.insert(1,5)#at index 1 the value 5 is inserted
list.extend(list01)
list.remove(5)#it will remove element 5
list.reverse()
list.sort()
print(list)