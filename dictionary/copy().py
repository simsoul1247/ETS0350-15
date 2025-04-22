original_dict = {
    'name': 'Dagmawi',
    'hobbies': ['reading', 'Watching Movies']
}

copied_dict = original_dict.copy()

print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

copied_dict['hobbies'].append('Watching Football matches')

print("\nAfter modifying the copied dictionary:")
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)