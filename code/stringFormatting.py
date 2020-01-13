print("Hello","World", sep="***")
# Hello***World

print("Hello","World", end="***")
# Hello World***>>>

print()
(aName, age) = ("nicolas4d", 30)
print("%s is %d years old." % (aName, age))

itemdict = {"item" : "banana",
            "cost" : 24}
print("The %(item)s costs %(cost)7.1f cents"%itemdict)
# The banana costs    24.0 cents

