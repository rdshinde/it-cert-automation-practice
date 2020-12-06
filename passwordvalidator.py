def password(string):
    l,u,d,s = 0,0,0,0
    if len(password)>=8:
        for i in string:
            if i.islower():
                l+=1
            if i.isupper():
                u+=1
            if i.isdigit():
                d+=1
            if i in '!@#$%&*\|?/.,:':
                s+=1
    else:
        return False

    if l>= 1 and u>=1 and d>=1 and s>=1:
        return True
    else:
        return False

print(passwordvalidator(input('Enter a password: ')))





#def password(s):
#    return bool(re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8}', s))
