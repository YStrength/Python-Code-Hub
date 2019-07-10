rows = int(input())
pwds = []
for i in range(rows):
    pwds.append(str(input()))
for i in range(rows):
    pwd = pwds[i]
    e_digit = False
    e_alpha = False
    e_illegal = False
    if len(pwd) < 6:
        print('Your password is tai duan le.')
    else:
        for c in pwd:
            if c.isalpha() == True:
                e_alpha = True
            elif c.isdigit() == True:
                e_digit = True
            elif c == '.':
                pass
            else:
                e_illegal = True
        if e_alpha == False:
            print('Your password needs zi mu.')
        elif e_digit == False:
            print('Your password needs shu zi.')
        elif e_illegal == True:
            print('Your password is tai luan le.')
        else:
            print('Your password is wan mei.')