# Find the intersection of [1, 2, 3, 4] and [3, 4, 5, 6].
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = list(set(list1) & set(list2))
print(intersection)

# Find the union of [1, 2, 3] and [3, 4, 5] without duplicates.
list1 = [1, 2, 3]
list2 = [3, 4, 5]

union = list(set(list1)|set(list2))
print(sorted(union))

# Find the most frequent element in [1, 2, 2, 3, 3, 3, 4].
nums = [1, 2, 2, 3, 3, 3, 4]

# Step 1: Create a dictionary to count frequency
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1  # If the number is already in the dictionary, add 1 to its count
    else:
        freq[num] = 1  # If it's not in the dictionary, set its count to 1

# Step 2: Find the element with the highest count
most_frequent = None
max_count = 0

for key in freq:  # Loop through all the numbers in the frequency dictionary
    if freq[key] > max_count:  # If the current number's count is higher than max_count
        max_count = freq[key]  # Update max_count
        most_frequent = key  # Update the most frequent number

print(most_frequent)  # Output: 3
        


