# 🔰 Beginner (20 Questions)
# Create a list with five numbers and print it.

numbers = [1, 2, 3, 4, 5]
print(f"Here is the list of numbers: {numbers}")

# Replace the third element in [10, 20, 30, 40, 50] with 99.
numbers = [10, 20, 30, 40, 50]
print("Before:", numbers)  # Shows original list
numbers[2] = 99  # Update the third element
print("After:", numbers)  # Shows modified list


# Append 60 to [10, 20, 30, 40, 50].
numbers = [10, 20, 30, 40, 50]
print(f"Here is the list number before: {numbers}")  
numbers.append(60)  # ✅ Append 60 to the list
print(f"Here is the list number after append: {numbers}") 

# Remove the last element from [1, 2, 3, 4, 5] using .pop().
remove_Number = [1, 2, 3, 4, 5]
remove_Number.pop()  # ✅ Removes the last element (5)
print(f"Here is the final list after pop: {remove_Number}")


# Extract the first three elements from [100, 200, 300, 400, 500] using slicing.

slice_list = [100, 200, 300, 400, 500]  
sliced_result = slice_list[:3]  # ✅ Extracts first three elements
print(f'Here is the list after slice: {sliced_result}')


# Reverse [10, 20, 30, 40, 50] using .reverse().
rev_Order = [10, 20, 30, 40, 50]
rev_Order.reverse()
print(f'Here is the list after reverse :{rev_Order}')


rev_Order = [10, 20, 30, 40, 50]
reversed_list = rev_Order[::-1]  # ✅ Slicing method to reverse
print(f'Here is the list after reverse: {reversed_list}')


# Sort [8, 3, 10, 1, 7] in ascending order.
order_Srt = [8, 3, 10, 1, 7]
order_Srt.sort()
print(f'Here is the list after sort :{order_Srt}')


# 🔸 Alternative Approach (Without Modifying Original List)
# If you want to return a new sorted list without modifying the original:

order_Srt = [8, 3, 10, 1, 7]
sorted_list = sorted(order_Srt)  # ✅ `sorted()` creates a new sorted list
print(f'Here is the list after sort: {sorted_list}')


# Find the index of "apple" in ["banana", "apple", "cherry"].
Ind_Chk = ["banana", "apple", "cherry"]
pnt_Chk = Ind_Chk.index("apple")
print(f'Here is the final output:{pnt_Chk}')


# ✅ Solution: Using try-except
# We use try-except to handle the error gracefully and prevent the program from crashing.

Ind_Chk = ["banana", "cherry"]  # No "apple" in the list
try:
    pnt_Chk = Ind_Chk.index("apple")  # 🔍 Try to find "apple"
    print(f'Here is the final output: {pnt_Chk}')
except ValueError:  
    print("Error: 'apple' is not in the list!")  # 🛑 Handle the error



# Count how many times "dog" appears in ["cat", "dog", "dog", "fish"].
sum_Chk = ["cat", "dog", "dog", "fish"]
total_Chk = sum_Chk.count("dog")  # ✅ Simply count occurrences
print(f'Here is the final output: {total_Chk}')

# Merge [1, 2, 3] and [4, 5, 6] using .extend().
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)  # ✅ Correct: Modifies list1 directly
print(f'Here is the final output: {list1}')  # ✅ Print list1

# ✔ Use .extend() when you want to modify the original list.
# ✔ Use list1 + list2 when you need a new list.
