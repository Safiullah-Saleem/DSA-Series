# Retrieve the first and last elements from [100, 200, 300, 400, 500].
numbers = [100, 200, 300, 400, 500]
first_Element = numbers[0]
last_Element = numbers[-1]
print(first_Element,last_Element)


# Swap the first and last elements of [1, 2, 3, 4, 5].
elements = [1, 2, 3, 4, 5]
elements[0], elements[-1] = elements[-1],elements[0]
print(elements)

# Find the second largest number in [12, 5, 78, 45, 90, 23].

numbers = [12, 5, 78, 45, 90, 23]
first_largest = max(numbers)
numbers.remove(first_largest)
second_largest = max(numbers)
print(second_largest)

# Remove duplicates from [1, 2, 3, 4, 1, 2, 5, 6].
lst = [1, 2, 3, 4, 1, 2, 5, 6]
unique = list(set(lst))
print(unique)   # Output (order may vary): [1, 2, 3, 4, 5, 6]

# other method 
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)   # Output: [1, 2, 3, 4, 5, 6]

# Retrieve every third element from [5, 10, 15, 20, 25, 30, 35, 40].
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
result = numbers[::3]
print(result)


# Extract a sublist [3, 4, 5] from [1, 2, 3, 4, 5, 6].
lst = [1, 2, 3, 4, 5, 6]
sublist = lst[2:5]
print(sublist)



# Find the middle element of [1, 2, 3, 4, 5].
lst = [1, 2, 3, 4, 5]
mid_index = len(lst) // 2
mid_element = lst[mid_index]
print(mid_element)  # Output: 3 

# Replace every even-indexed element with 0 in [1, 2, 3, 4, 5].
elm = [1, 2, 3, 4, 5]
for i in range(0, len(elm), 2):
    elm[i] = 0
print(elm) 


# Retrieve all elements except the last two from [5, 10, 15, 20, 25].
elm = [5, 10, 15, 20, 25]
retrieve = elm[:-2]
print(retrieve)

# Reverse a sublist [3, 4, 5] inside [1, 2, 3, 4, 5, 6].
elms = [1, 2, 3, 4, 5, 6]
sublist = elms[2:5]  # Get the sublist [3, 4, 5]
sublist.reverse()    # Reverse the sublist in place
elms[2:5] = sublist  # Replace the original part of the list with the reversed sublist
print(elms)  # Output: [1, 2, 5, 4, 3, 6]