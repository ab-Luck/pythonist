# Python3 code to Demonstrate Remove empty List

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
while [] in test_list :
	test_list.remove([])

# printing result
print("List after empty list removal : " + str(test_list))
