# set

A = {1,2,3,4,5}
B = {4,5,6,7,8}

set_union = A | B
print(set_union)

set_inter = A & B
print(set_inter)

set_diff_ab= A-B
print(set_diff_ab)

set_diff_ba= B-A
print(set_diff_ba)

set_symm_diff= A.symmetric_difference(B)
print(set_symm_diff)
