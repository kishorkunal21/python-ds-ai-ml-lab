def check_brackets(brackets_check:str):

    if len(brackets_check) %2 != 0:
        return False 

    b_dict = {"}":"{",")":"(","]":"[",}
    brackets = []

    for b in brackets_check:
        print(brackets)
        if b in b_dict.values():
            brackets.append(b)
        else:
            if brackets and brackets[-1]==b_dict.get(b):
                brackets.pop()
    
    return len(brackets) == 0

def check_brackets_optimized(s: str) -> bool:
    """Optimized version with early termination."""
    if len(s) % 2 != 0:  # odd length = invalid
        return False
    
    b_dict = {"}": "{", ")": "(", "]": "["}
    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in b_dict:
            if not stack or stack[-1] != b_dict[char]:
                return False
            stack.pop()

    return len(stack) == 0
        
print(check_brackets("[({})]"))

## O(n) = time and spoace




def get_binary_equivalent(num : int):

    reminders = []

    while num>0 :
        num,rem = divmod(num,2)
        reminders.append(rem)

    print(f'Binary of {num} : {reminders}')  

bq = get_binary_equivalent(242)      



