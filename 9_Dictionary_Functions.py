d1 = {"Chinmay": "Rice", "Raj": "Breakfast", "Preeti": "Manchurian",
      "Yash": {"B": "Bread", "L": "Roti", "HT": "Bhel", "D": "Dahi"}}

print(d1)
d2 = {"Chinmay": "Rice", "Raj": "Breakfast", "Preeti": "Manchurian",
      "Yash": {"B": "Bread", "L": "Roti", "HT": "Bhel", "D": "Dahi"}}

# d3 and d2 are pointers, so they donot copy the items they just points to that value. So we have to use copy function of dictionary.

d3 = d2

del d3["Yash"]
print(d3)

print(d2.get("Raj"))
d2.update({"Darshil": "Pizza"})
print(d2)
print(d1.keys())
print(d1.items())
