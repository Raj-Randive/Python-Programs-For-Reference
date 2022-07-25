grocery = ["Laptop", "PC", "Mobile", "T.V", "Remote", 56]
print(grocery[4])

numbers = [2, 7, 9, 3, 8]
# numbers.sort()  # Changes the original list
# numbers.reverse()  # Changes the original list

# print(numbers[::1]) # By slicing step, original list does not change.

print(len(numbers))
print(max(numbers))
print(min(numbers))

numbers.append(7)
print(numbers)
print("\n")

# Blank List

num = []
num.append(3)
num.append(7)
num.append(5)
num.append(1)
print(num)

print("\n")
num2 = [2, 6, 8, 5, 11]
num2.insert(2, 16)
num2.remove(5)
num2.pop()  # Removes the last element...
print(num2)