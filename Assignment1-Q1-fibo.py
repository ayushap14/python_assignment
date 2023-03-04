n = int(input("Enter the number of terms: "))

# initialize the first two terms of the sequence
a, b = 0, 1

# print the first n terms of the sequence
for i in range(n):
    print(a, end=" ")
    # compute the next term of the sequence as the sum of the previous two terms
    a, b = b, a + b

