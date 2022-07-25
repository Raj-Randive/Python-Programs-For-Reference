mystr = "rAJ is my name. This is Me."
print(len(mystr))
print(mystr[::])
print(mystr[-8:-1:])

# Alpha-numeric string
mystr1 = "RAJ is my name. This is Me."
print(mystr1.isalnum())   #False
mystr2 = "RAJismyname.ThisisMe."
print(mystr2.isalnum())   #False
mystr3 = "RAJismynameThisisMe33"
print(mystr3.isalnum())   #True


print(mystr.endswith("Me."))
print(mystr.endswith("me."))

print(mystr.count("i"))

print(mystr.capitalize()) #Only First Letter CapitalizesMe.
print(mystr1.lower())   #Only First Letter Lowers.
print(mystr1.upper())   #Only First Letter Upper.

print(mystr.find("is"))
print(mystr.replace("is", "are"))

