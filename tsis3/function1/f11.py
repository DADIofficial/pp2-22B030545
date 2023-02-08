def check_palindrome(x):
    for i in range(0, len(x)):
        if x[i] != x[len(x) - i - 1]:
            return "palindrome"
    return "not palindrome"
print(check_palindrome(input()))