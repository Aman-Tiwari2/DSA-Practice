# Here we are going to know about tail recusion

# In Tail recursion when first we call function then we do our job 

# Using this print name N Times

'''THIS ONE IS ONLY FOR CONCEPTUAL PART'''

count = 0
def nameN_Times(): # This is know as Tail recursion
    global count
    if count == 4:
        return
    
    count += 1
    nameN_Times() # first call function then
    print("Aman") # do job last 

nameN_Times()
