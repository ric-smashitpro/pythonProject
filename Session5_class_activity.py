n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1 > n2:
    print("Maximum value is ", n1)
    print("Minimum value is ", n2)
elif n1 < n2:
    print("Minimum value is ", n1)
    print("Maximum value is ", n2)
else:
    print("Only one value: ", n1)