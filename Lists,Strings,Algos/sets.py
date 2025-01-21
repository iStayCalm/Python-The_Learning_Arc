# sets have no order of printing, adding duplicate elemets have no effect 

set1 = {"saad", "is", "calm", "calm"}
set2 = set(["he", "is", "not"])

print(f"set1 : {set1}")
print(f"set2 : {set2}")

print("\n") # Adding to sets 

set1.add(":)")
print(f"added to set1 : {set1}")

print("\n") # Updating in sets 

set2.update(["fr" , ":)"])
print(f"updated set2 : {set2}")

# -:-: SET OPERATIONSS :-:- 

print(f"\n\n-:-: OPERATIONS OF SET :-:- ")
# union : | #

union_set = set1 | set2
print(f"\nUnion of set1 & set2 : {union_set}")

# intersection : & 

intersection_set = set1 & set2
print(f"\nIntersection of a set : {intersection_set}")

# Difference : - 

difference_set = set1 - set2
print(f"\nDifference set 1 - set 2 : {difference_set}")

difference_set = set2 - set1
print(f"\nDifference set 2 - set 1 : {difference_set}")

# Symmetric Difference : ^

symm_diff_set = set1 - set2
print(f"\nSymmeteric Difference : {symm_diff_set}")

# -:-: METHODS :-:-

# Examples of set methods in one line
s1 = {1, 2, 3}; s2 = {3, 4, 5}

s1.add(4)                                       # s1 becomes {1, 2, 3, 4}
s1.remove(2)                                    # s1 becomes {1, 3, 4}
s1.discard(5)                                   # s1 stays {1, 3, 4} (no error if 5 not found)
s1.pop()                                        # Removes an arbitrary element (e.g., 1)
s1.clear()                                      # s1 becomes empty set {}
union_set = s1.union(s2)                        # {3, 4, 5} (union of s1 and s2)
intersect_set = s1.intersection(s2)             # {3} (common in s1 and s2)
diff_set = s2.difference(s1)                    # {4, 5} (in s2, not in s1)
sym_diff_set = s1.symmetric_difference(s2)      # {1, 4, 5} (non-common elements)
print(s1.issubset(s2))                          # True if s1 ⊆ s2
print(s2.issuperset(s1))                        # True if s2 ⊇ s1
print(s1.isdisjoint(s2))                        # True if no common elements
