original_list = [1, 2, [4, 7]]
copied_list = original_list.copy()
# Modification
copied_list[0] = 10 
copied_list[3][0] = 40 
 
print("Original List:", original_list)
print("Copied List:", copied_list)
print("Modified Copied List:", copied_list)