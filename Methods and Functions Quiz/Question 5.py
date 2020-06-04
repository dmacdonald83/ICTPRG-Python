def IsPalindrome(word):
    cleaned = word.replace(' ', '').lower()
    reversed = cleaned[::-1]
    for idx, ch in enumerate(cleaned):
        if reversed[idx] != ch:
            return False
    return True

print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))

