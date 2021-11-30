# Brynn Moncur
# CSCI102 - Section D
# Python-TheMaxGapInList

list_size = int(input())
num_list = []
n = int()
diff = int()

while n < list_size:
    list_num = int(input())
    num_list.append(list_num)
    n += 1
    
for i in range(num_list[1], num_list[list_size]):
    for j in range (num_list[1], num_list[list_size]):
        current_max_diff = 0
        diff = abs(i-j)
        if diff > current_max_diff:
            current_max_diff = diff

print(f"Max gap is {current_max_diff}")

           
