#string method
#string are immutable
s=" hello world "                        
#s[0]="R" #You cannot that.

     
#upper()
print(s.upper())
#lower()
print(s.lower())
#capitalise()
print(s.capitalize())
#title()
print(s.title())



#lstrip()  l-->left
print(s.lstrip())
#rstrip()  r-->right
print(s.rstrip())
#strip()   remove all starting spaces ,ending spaces
print(s.strip())


#find()
text="python is fun and fun and fun"
print(text.find("is"))  #it will give index of first occurence
#replace()
print(text.replace("fun","great"))  #it will replace all the occurence


#split()  join()
fruits="apple,banana,grapes"
print(fruits.split(",")) #it will convert into list
print(",".join(['apple', 'banana', 'grapes'])) #string.join([['apple', 'banana', 'grapes']])
#it will gives back th string


#checking string prpoerty
text0="12123   "
print(text0.isalnum())# output: false
print(text0.isalpha())# output: false
print(text0.isdigit())# output: false
print(text0.isspace())# output: false