user_input = int(input("Enter your number to check number weather number is Armstrong or not? :- "))
num = user_input
lenght = len(str(num))
new_val = 0
while num > 0:
    remainder = num % 10
    new_val = new_val + remainder**lenght
    num = num//10

if user_input == new_val:
    print("Given Number is armstrong")
else:
    print("Given Number is not armstrong")
