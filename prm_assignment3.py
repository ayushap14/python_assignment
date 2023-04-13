n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    element = input("Enter an element: ")
    lst.append(element)

sorted_lst = sorted(lst, key=lambda x: x[-2])

print("Sorted list based on 2nd last character:")
print(sorted_lst)
