numbers = (1,2,3,4,5,6,7,8,9,10)  #declaring the tuple
count_odd = 0
count_even = 0

for x in numbers:
    if x % 2:
        count_even+=1
    else:
        count_odd+=1

print("numbers of even numbers :",count_even)
print("numbers of odd numbers :",count_odd)        
