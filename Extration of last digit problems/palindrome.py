user_input = int(input("Enter your number to check weather given number is Palindrome or not? :- "))
num = user_input
new_val = 0

while num>0:
    remainder = num % 10
    new_val = (new_val*10) + remainder
    num = num//10

if user_input == new_val:
    print("Given Number is Palindrome")

else:
    print("Given number is not Palindrome!")

