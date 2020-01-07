def reverseStr(str):
    if len(str) <= 1 :
        return str
    else :
        return reverseStr(str[1:]) + str[0]

def removeSpaceAndPunctuation(str):
    i = 0
    strLen = len(str)
    punSym = [" ", ",", ';', "'", '.', '’', '-']

    while i < strLen:
        if str[i] in punSym :
            str = str[0:i] + str[i + 1:]
            strLen -= 1
            continue

        i += 1

    return str

def isPalindrome(str):
    str = str.lower()

    newStr = removeSpaceAndPunctuation(str)
    reStr = reverseStr(newStr)

    if reStr == newStr :
        return True
    else :
        return False

print(isPalindrome("kayak"))
print(isPalindrome("aibohphobia"))
print(isPalindrome("Live not on evil"))
print(isPalindrome("Reviled did I live, said I, as evil I did deliver"))
print(isPalindrome("Go hang a salami; I’m a lasagna hog."))
print(isPalindrome("Able was I ere I saw Elba"))
print(isPalindrome("Kanakanak"))
print(isPalindrome("Wassamassaw"))
