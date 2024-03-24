"""
#packing a tuple
address = ("Netherlands", "Amersfoort", "Vathorst", "Zeijerveen 2", "3825RM")

for item in address:
    print(item, end=" ")

#unpacking a tuple
country, city, town, street, postcode = address
print(country, city, town, street, postcode)

#creating tuples without parantheses
mytuple = 53,"cheese",True,5832,False,"cheese2"
print(mytuple)



#nested tuple
nested_tuple = ("cheese", [42,64,43,65], ("cheese", 96))
print(nested_tuple)

print(nested_tuple[0][4])
print(nested_tuple[1][2])
print(nested_tuple[2][1])
print(nested_tuple[:2])
print(nested_tuple[1:])

"""

#negative indexing
negative = (394,32,42,65,45,36)
print(negative[-6:])
print(negative[:])

#type error in tuple
negative[1] = 14
