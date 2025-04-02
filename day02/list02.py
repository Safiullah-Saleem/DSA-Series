# Insert "grape" at index 2 in ["apple", "banana", "cherry"].
furits = ["apple", "banana", "cherry"]
furits.insert(2,"grape")
print(f'Here is the final output after insert a value :{furits}')



# Remove "banana" from ["apple", "banana", "cherry"] using .remove().

val_Rem = ["apple", "banana", "cherry"]
val_Rem.remove("banana")
print(f'Here is the result of val_rem after removing the value:{val_Rem}')

# Check if "python" exists in ["java", "python", "c++"].
chk_Val = ["java", "python", "c++"]
val_Exists = "python" in chk_Val  # ✅ Correct way to check membership
print(f'Here is the output: {val_Exists}')  # Output: True


# Extract every second element from [10, 20, 30, 40, 50].
extra_Ele = [10, 20, 30, 40, 50]
evr_Elm = extra_Ele[::2]
print(f'Here is the final output :{evr_Elm}')


# Convert a string "hello" into a list of characters.
string = "hello"
string_list = list(string)
print(f'Here is the actual list after conversion: {string_list}')  # ✅ Print correct variable


# Convert [1, 2, 3] into a string "123".
list_Cvt = [1, 2, 3]
str_Cvt = "".join(map(str, list_Cvt))  # ✅ Convert each number to string before joining
print(f'Here is the result of this question: {str_Cvt}')  # Output: "123"

# Copy a list without modifying the original.
iteam_list = [1,2,3,4,5]
duplate_Iteam = iteam_list.copy()
print(duplate_Iteam) 

# Find the max and min in [23, 45, 67, 89, 12].
arr = [23, 45, 67, 89, 12]
arr_max = max(arr)
arr_min = min(arr)
print(f'Here is the maximum value  :{arr_max}')
print(f'Here is the minimum value :{arr_min}')

# Remove all elements from [10, 20, 30] using .clear().
remove_List = [10, 20, 30]
remove_List.clear()
print(f'Here is the list after clearing: {remove_List}')  # Output: []

# Get the last three elements from [1, 2, 3, 4, 5, 6] using slicing.
slc = [1, 2, 3, 4, 5, 6]
after_Slc = slc[-3:]  # ✅ Directly gets the last three elements
print(f'Here is the final result: {after_Slc}')  # Output: [4, 5, 6]

