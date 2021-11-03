total = 0
hash_key = "R2YJ"
number_of_slots = 97
for i in range(len(hash_key)):
    ascii_code = ord(hash_key[i])
    total=total+ascii_code

    hash_value=total% number_of_slots
print(hash_value)

#have to change value sin line 2 and 3 depending on q
