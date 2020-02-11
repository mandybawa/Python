# Task:
# Check if the brackets in a string are balanced or not

# A matching pair of brackets is not balanced if the set of brackets it
# encloses are not matched. For example, {[(])} is not balanced because
# the contents in between { and } are not balanced.


def braces(string):
    open_braces = ["[", "{", "("]
    closed_braces = ["]", "}", ")"]
    add_to_matched_list = False
    matched = []

    for i in string:
        if i in open_braces:
            add_to_matched_list = True
            matched.append(i)
        elif i in closed_braces:
            position = closed_braces.index(i)
            if len(matched) > 0 and open_braces[position] == matched[len(matched) - 1]:
                matched.pop()

    if len(matched) == 0 and add_to_matched_list:
        return "BALANCED"
    else:
        return "UNBALANCED"


strings = ["{{", "}}", "[[", ")]", "{}", "()", "[{()}]", "[{{(}]"]
for s in strings:
    print(braces(s))
