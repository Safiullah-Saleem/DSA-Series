# ❓ Question 1:
# Replace the third element in the list [10, 20, 30, 40, 50] with the number 99.
# Then print the list before and after the change.
element = [10, 20, 30, 40, 50]
element[2] = 99
print(element) 


# 🚀 Ready for Question 2?
# Append the number 60 to the list [10, 20, 30, 40, 50],
# and print the list before and after appending.
element = [10, 20, 30, 40, 50]
print("Before appending:", element)

element.append(60)
print("After appending:", element)


# 🧠 Ready for Question 3?
# Remove the last element from the list [1, 2, 3, 4, 5] using .pop()
# and print the list after removal.
element =  [1, 2, 3, 4, 5]
print("Before pop:", element)

element.pop()
print("After pop:", element)



# 🚀 On to Question 4:
# Extract the first three elements from the list [100, 200, 300, 400, 500] using slicing
# and print the result.
element = [100, 200, 300, 400, 500] 
sl = element [:3]
print(sl)



# Swap the first and last elements of the list.
# Then print the list before and after the swap.
nums = [1, 2, 3, 4, 5]
print("Before swap:", nums)

# Swap the first and last elements
nums[0], nums[-1] = nums[-1], nums[0]

print("After swap:", nums) 


# Ready for Intermediate Question 2?
# Find the second largest number in the list:
nums = [12, 5, 78, 45, 90, 23]
first_Largest = max(nums)
nums.remove(first_Largest)
second_Largest = max(nums)
print(second_Largest)


# Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8]
element = [1, 2, 3, 4, 5, 6, 7, 8]
sum_even = 0  # Variable to store the sum of even numbers
for num in element:
    if num % 2 == 0:  # Check if the number is even
        sum_even += num  # Add the even number to the sum
print("Sum of even numbers:", sum_even)


# Merge two sorted lists [1, 3, 5] and [2, 4, 6].
list1 = [1, 3, 5] 
list2 = [2, 4, 6]

# Merge the lists
final_Output = list1 + list2
# Sort the merged list
final_Output.sort()
# Print the sorted list
print(final_Output)

# Rotate [1, 2, 3, 4, 5] right by 2 positions.
# Original list
lst = [1, 2, 3, 4, 5]

# Rotate the list right by 2 positions
rotated_lst = lst[-2:] + lst[:-2]

print(rotated_lst)  # Output: [4, 5, 1, 2, 3]

# Check if [1, 2, 3, 2, 1] is a palindrome.
lit = [1, 2, 3, 2, 1]
if lit == lit[::-1]:  # Reverse the list and check
    print("The list is a palindrome!")
else:
    print("The list is not a palindrome.")
    
# Method 2: Using a loop to compare elements

lit = [1, 2, 3, 2, 1]
is_palindrome = True
for i in range(len(lit) // 2):
    if lit[i] != lit[-(i + 1)]:  # Compare corresponding elements
        is_palindrome = False
        break

if is_palindrome:
    print("The list is a palindrome!")
else:
    print("The list is not a palindrome.")
