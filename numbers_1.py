num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))


if num_1 >= num_2 and num_1 >= num_3:          
    largest = num_1
    if num_2 <= num_3:
        smallest = num_2
    else:
        smallest = num_3
elif num_2 >= num_1 and num_2 >= num_3:
    largest = num_2
    if num_1 <= num_3:
        smallest = num_1
    else:
        smallest = num_3
else:
    largest = num_3
    if num_1 <= num_2:
        smallest = num_1
    else:
        smallest = num_2


print (largest, smallest)