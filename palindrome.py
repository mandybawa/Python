# Task: To check if a string is palindrome or not
# A string is palindrome if reverse of the string is same as the original string.
# Example : "level" is palindrome and "mandy" is not palindrome.

#### Method 1 (by reversing the string)#####
def is_palindrome(string_to_check):
    reversed_str = reversed(string_to_check)
    if list(string_to_check) == list(reversed_str):
        return True
    return False

print(is_palindrome("level")) #return True
print(is_palindrome("mandy")) #return False


#### Method 2 (using recursion) #####
def is_palindrom_using_recursion(string_to_check):
    if len(string_to_check) < 1:
        return True

    if string_to_check[0] == string_to_check[-1]:
        return is_palindrom_using_recursion(string_to_check[1:-1])
    return False

print(is_palindrom_using_recursion("level"))
print(is_palindrom_using_recursion("mandy"))
