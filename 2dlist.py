# matrix=[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[0][1])


numbers =[2,2,4,6,6,1,8,9,9,5]
uniqes=[]

for items in numbers:
    if items not in uniqes:
        uniqes.append(items)

print(uniqes)
    
         


