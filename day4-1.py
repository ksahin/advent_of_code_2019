def verify_password_rules(n):
    if len(str(n)) != 6:
        return False
    has_same_two_adjacent_digit = False
    never_decrease = True
    for index,c in enumerate(str(n)):
        if index < 5 and c == str(n)[index+1]:
            has_same_two_adjacent_digit = True
        if index < 5 and int(c) > int(str(n)[index+1]):
            never_decrease = False
    
    return (has_same_two_adjacent_digit and never_decrease)
    


start = 372037
end = 905157

numbers = [x for x in range(start, end+1)]

password_candidates = []
for n in numbers:
    if verify_password_rules(n):
        password_candidates.append(n)

print(len(password_candidates))