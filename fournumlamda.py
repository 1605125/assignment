print("Enter first number ")
f1 = int(input())
print("Enter second number ")
f2 = int(input())
print("Enter third number ")
f3 = int(input())
print("Enter fourth number ")
f4 = int(input())
di = lambda a, b, c, d: a if a > b and a > c and a > d else b if b > c and b > d else c if c > d else d
print("The largest is {}".format(di(f1, f2, f3, f4)))