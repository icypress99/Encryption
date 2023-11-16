def add_points(p, a, b, xp, yp, xq, yq):
    if not is_on_curve(xp, yp, p, a, b):
        return "P is not on the curve"

    if not is_on_curve(xq, yq, p, a, b):
        return "Q is not on the curve"

    if (xp, yp) == (xq, yq):
        lam = ((3 * xp**2 + a) * pow(2 * yp, -1, p)) % p
    else:
        lam = ((yq - yp) * pow(xq - xp, -1, p)) % p

    xr = (lam**2 - xp - xq) % p
    yr = (lam * (xp - xr) - yp) % p

    return f"({xr}, {yr})"

def prime_checker(num):
    if num < 1:
        return -1
    elif num > 1:
        if num == 2:
            return 1
        for i in range(2, num):
            if num % i == 0:
                return -1
            return 1

def is_on_curve(x, y, p, a, b):
    return (y**2 - (x**3 + a * x + b)) % p == 0


while 1:
    p = int(input("p = "))
    if prime_checker(p) == 1:
        break
    else:
        print("Enter prime number ")
a = int(input("a = "))
b = int(input("b = "))
xp = int(input("xp = "))
yp = int(input("yp = "))
xq = int(input("xq = "))
yq = int(input("yq = "))

result = add_points(p, a, b, xp, yp, xq, yq)

print(result)