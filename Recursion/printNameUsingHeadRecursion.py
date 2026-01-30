# Here I write small code in recusion to print AMAN four(4) times.
# This is know as head recursion where we done job first then call function inside function

'''THIS ONE IS ONLY FOR CONCEPTUAL PART'''

count = 0
def nameFourTimes():
    global count
    if count == 5:
        return
    count += 1
    print("Aman")
    nameFourTimes()


nameFourTimes()


    