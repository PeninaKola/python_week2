# 1. Create an empty list
my_list = []

# 2. Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Insert value 15 at the second position
my_list.insert(1, 15)

# 4. Extend with another list
my_list.extend([50, 60, 70])

# 5. Remove the last element
my_list.pop()

# 6. Sort the list
my_list.sort()

# 7. Find and print the index of the value 30
index_of_30 = my_list.index(30)
print(index_of_30)