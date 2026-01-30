user_input = int(input("Enter your number:-"))
num = user_input
rev_number = ''
while num > 0:
    remainder = num % 10
    rev_number = rev_number + str(remainder)
    num = num//10

print(rev_number) 
