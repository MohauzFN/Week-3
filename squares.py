while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n > 0:
            break
        print("Please enter a positive integer")
    except ValueError:
        print("Please enter a positive integer")
i = 0
while i**2<=n:
    if i % 2 == 0:
        print(i**2)
    i = i + 1
