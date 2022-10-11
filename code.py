def reverse(string):
    #length = -(x) in order to later initiate a for loop from the end of the string  
    length = -(len(string)-1) # -1 in order to match index to string length
    #new variable to store reverse string
    new_string = str()  
    #initiate for loop from the end
    for n in range (length):  
       new_string += string[n]   #store reversed string loop by loop
    print (new_string)
x = input("Write a thing ")
reverse(x)
