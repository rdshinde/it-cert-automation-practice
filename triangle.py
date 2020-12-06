def is_triangle(a, b, c):
    if a>=b and a>=c :
        if a< b+c:
            return True
        elif a==b+c:
            return False
        else:
            return False
    if b>=c and b>=a:
        if b<c+a:
            return True
        elif b==a+c:
            return False
        else:
            return False
    if c>=a and c>=b:
        if c<a+b:
            return True
        elif c==a+b:
            return False
        else :
            return False
