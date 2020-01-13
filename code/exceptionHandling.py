import math

# for i in range(10)
# SyntaxError: invalid syntax (<pyshell#61>, line 1)

anumber = int(input("Please enter an integer "))
# Please enter an integer -23

# print(math.sqrt(anumber))
#     Traceback (most recent call last):
#     File "<pyshell#102>", line 1, in <module>
#     print(math.sqrt(anumber))
#     ValueError: math domain error
#     >>>


try:
    print(math.sqrt(anumber))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(anumber)))

print()
if anumber < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(anumber))
#     Traceback (most recent call last):
#     File "<stdin>", line 2, in <module>
#     RuntimeError: You can't use a negative number
