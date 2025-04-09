list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = list(set(list1) & set(list2))
print(intersection) # Output: [3, 4]
🧠 Explanation:

set(list1) converts the list into a set (removes duplicates).

& means "and", so it gives elements common in both.

list(...) changes the set back to a list.


list1 = [1, 2, 3]
list2 = [3, 4, 5]

union = list(set(list1) | set(list2))
print(union) 


🧠 Explanation:

set(list1) turns list1 into a set: {1, 2, 3}

set(list2) turns list2 into a set: {3, 4, 5}

| is the union operator → joins both sets, removes duplicates.

list(...) turns the result back into a list.