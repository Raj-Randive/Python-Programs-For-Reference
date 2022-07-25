# Dictionary is nothing but key value pairs.

d2 = []
d3 = ()
print(type(d2))
print(type(d3))

d1 = {}  # Blank Dictionary.
print(type(d1))

d4 = {"Chinmay":"Rice", "Raj":"Breakfast", "Preeti":"Manchurian", "Yash": {"B":"Bread", "L":"Roti", "HT":"Bhel", "D":"Dahi"}}
print(d4)
print(d4["Chinmay"])
print(d4["Raj"])

print("\n")

print(d4["Yash"])
print(d4["Yash"] ["B"])

d4["Aryan"] = "Healthy Food"
d4[404] = "Junk Food"
print(d4)
del d4[404]

print(d4)
