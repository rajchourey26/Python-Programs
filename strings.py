#Creating the string
print("#Creating the string")

F_name ="Raj "                #Double quote string
print(F_name)
F_Name='RAJ IS FIRST NAME'    #Single quote string
print(F_Name)
S_name='''CHOUREY        
IS THE LASTNAME'''           #Triple quote string use for multiline string
print(S_name)
'''THIS  IS A COMMENT
MULTILINE COMMENT \n'''
print("\n#Indexing of the string")

#Indexing of the string
name="Raj Chourey"
#     R  a  j  _  C  h  o  u  r  e  y
#     0  1  2  3  4  5  6  7  8  9  10 #positive indexing 0-->n-1 |L-->R
#  -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 #negating indexing  -1-->-n |R-->L
#print(name.index("R"))--->0 #use for giving index no.
print(name[0]) #R
print(name[1]) #a
print(name[2]) #j
print(name[3]) #_
print(name[4]) #c
print(name[5]) #h
print(name[6]) #o
print(name[7]) #u
print(name[8]) #r
print(name[9]) #e
print(name[10])#y
#print(name[12])# string index out of range _ IndexError
print("\n #negative index")
                #if you have to convert to negative to positive indexing
print(name[-1]) # 11-1 -->10 #name[10]  # total length - |negative index|
print(name[-2]) # 11-2 -->9 #name[9] 
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])
print(name[-8])
print(name[-9])
print(name[-10])
print(name[-11])
