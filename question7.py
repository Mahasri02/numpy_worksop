# create a list as below
output=[[1,2,3],[4,5,6],[7,5,3,2,3,[2,[3]]]]
a=[1,2,3]
b=[4,5,6]
c=[7,5,3,2,3]
d=[2]
e=[3]

# use these lists to create another list which will look like the list output in line 2

# use append method to do this.
output = []

# Append the lists a, b, and c to output
output.append(a)
output.append(b)

# Append list e to list d
d.append(e)

# Append list d to list c
c.append(d)

# Finally, append the modified list c to output
output.append(c)

# The output list now looks like the required structure
print(output)
