
print("\nlist method")

list=[2,3,4,5,6,7]

list01=[8,9,10]

list.append(8) #this will change the original list  [2, 3, 4, 5, 6, 7, 8]
 
list.pop()#it will remove last element here 8  [2, 3, 4, 5, 6, 7]

list.insert(1,5)#at index 1 the value 5 is inserted  [2, 5, 3, 4, 5, 6, 7]

list.extend(list01)#[2, 5, 3, 4, 5, 6, 7, 8, 9, 10]

list.remove(5)#it will remove element 5  [2, 3, 4, 5, 6, 7, 8, 9, 10]

list.reverse()#it will reverse the whole the list  [10, 9, 8, 7, 6, 5, 4, 3, 2]

list.sort()#it sort by default ascending  [2, 3, 4, 5, 6, 7, 8, 9, 10]


print(list)