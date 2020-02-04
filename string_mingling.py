# Task: Alternatively Merge two Strings
# The result string’s first character should be the first character of the first string, 
# the second character should be the first character of the second string and so on.
# If you reach at the end of one string another string is still remaining then append the remaining of that string to final string 

# Example: str1 = "Mandy", str2 = "Bawa", result: MBaanwday

def string_mingling(str1, str2):
    result = ""

    max_length = max(len(str1), len(str2))

    for i in range(max_length):
        if i < len(str1):
            result += str1[i]
        if i < len(str2):
            result += str2[i]
    return result


str1 = "Mandy"
str2 = "Bawa"
merged_string = string_mingling(str1, str2)
print(merged_string)
