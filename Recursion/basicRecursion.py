# Here we learn basic concept of recursion 
# Definition - When function call itself in a function then it is called as recusion



# Infinite Recursion - When we not provide any condition it gives this below error

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded



"""
def greet(): # Function Defines here 
    print("Aman")
    greet() # Function calls itself again Know as recursion

greet() # Function call  
"""


# Recursion Syntax 

count = 0 # Global variable for stopping our recursion when condition satisfied
def greet(): 
    global count # if we write variable outside funtion we have to write global to access that funtion
    if count == 4: # Here we write condition where our recursion stops
        return 
    count += 1 # Here we write condition updation so that our condition can stop and give desired output
    print("Aman")
    greet() #Inside function call for recursion 

greet() #Outer call for an function working
