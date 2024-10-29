number = int(input("Enter any number"))
sum_of_odd_numbers = 0

for i in range (number):
    if i%2 != 0:
        sum_of_odd_numbers = sum_of_odd_numbers + i

c
print(f"The sum of odd numbers in the number you entered is {sum_of_odd_numbers}")