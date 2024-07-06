import re

def isPalindrome(s: str) -> bool:
    s_lower = s.lower()
    cleaned_string = re.sub(r'[^a-z0-9]','', s_lower)
    print(cleaned_string)
    left = 0
    right = len(cleaned_string) - 1
    while left < right:
        if cleaned_string[left] == cleaned_string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))