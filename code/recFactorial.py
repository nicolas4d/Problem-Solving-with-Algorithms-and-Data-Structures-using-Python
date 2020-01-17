def factorial(number):
    if number <= 1 :
        return 1
    else :
        return number * factorial(number - 1)

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
