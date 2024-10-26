my_set = {1,2,3,4,5,6,7,3,5,6,2,4,1,1,1,1,}
print(my_set)

my_set.add ( 100)
print(my_set)

my_set.remove(7)
print(my_set)


# practic  union . intersectin c, difference 

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# ________________________
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}