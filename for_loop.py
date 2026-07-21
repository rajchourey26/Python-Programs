#For loops-is used to iterate over a sequence (eg-list,string,range)
# they execute a block of code for each item int the sequence

print(1) 
print(2) 
print(3) 
print(4) 
print(5) 
print(6) 
#or we can use loop -for loop
for i in range(1,7):#for i in range(0,6):#as range function goes from 1 to (7-1) i.e 6 in this case
    print(i)

#table of 5 
for i in range(1,11):
    print("5 X",i,"=",5*i)# , is giving space by default
print("\n")
#Table of 6
for i in range(1,11):
    print("6 X",i,"=",6*i)