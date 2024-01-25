from math import sqrt,pow
def equacao2g(a,b,c):
    delta = pow(b, 2) - 4 * a * c
    if delta < 0:
        return False
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        r = [x1,x2]
        return r