#Syntax of Python Programming language
print("Hello World")

#Comments in python
x=1
#The initial value of x is 1
if x>0:
    print("These are two comments") #print a string
    
    
#Input/Output
txt=input("Type something to test this out:")
print(txt)

#Multiple statements on single line
print("Statement1")
print("Statement2")

print("Statement1");print("Statement2")

#Display the data type of 3.2
a=3.2
print(a,type(a))

#Display the data type of -6778
b=-6778
print(b,type(b))

#display the data type of -11.7
c=-11.7
print(c,type(c))

                        #Complex data type
#Make the complex values using Complex function
x=complex(1,2)
print(x)

z=1+2j
print(z,type(z))

                    #Boolean Data Type
x=True
print(x,type(x))

                           #string Data Type
x="Areeba"
print(x,type(x))

str2="Day's"
print(str2)

                    #Special Characters

print("This is a backslash mark(\\)")
print("This is \t tab key")
print("These are \'single qoutes\'")
print("Theses are the \"double qoutes\" ")
print("This is a newline \n New Line")

                    #String Indices
                    
str1="PYTHON tutorial"
print(str1[1])
print(str1[-1])
print(str1[-9])
print(str1[14])
                    #String Slicing

str1="abcd"
print(str1[0:2])

str2="PYTHON"
print(str2[0:6])

                           #List
list1=[5,12,24]
print(list1)

list2=['Red','Blue',56]
print(list2,type(list2))

list3=['Red',2.3,89]
print(list3,type(list3))

list4=['0']
print(list4)

list5=['RED','GREEN','BLUE','BLACK']
print(list5[0])
print(list5[-4])
print(list5[-1])
print(list5[-2])

list6=['RED','GREEN','BLUE','BLACK']
print(list6[0:3])

print(list6[1:2])



                        #If statement
a=40;
b=6;
if(a>b):
    print("Congratulations!You have passed")
    
else:
    print("You have fail")
 