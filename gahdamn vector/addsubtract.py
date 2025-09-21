# +

def addition(x1, y1, x2, y2):

    x = (x1 + x2)
    y = (y1 + y2)

    return x, y

q1 = addition(2, 1, 1, 3 )
q2 = addition(3, 4, 2, 1)
q3 = addition(5, 9, 3, 7)

print("adds")
print(q1)
print(q2)
print(q3)

print()

# -

def substract(x1, y1, x2, y2):
    x = (x1 - x2)
    y = (y1 - y2)

    return x, y

q4 = substract(7, 9, 5, 2)
q5 = substract(9, 3, 8, 2)
q6 = substract(7, 9, 6, 7)

print("subs")
print(q4)
print(q5)
print(q6)

print()
# 3d vector

def threedim(x1, y1, z1, x2, y2, z2):

    xx, yy, zz = (x1 + x2), (y1 + y2), (z1 + z2)

    x, y, z = (x1 - x2),  (y1 - y2), (z1 - z2)
   

    return (xx, yy, zz), (x, y, z)

adds, subs = threedim(4, -2, 1, 1, 0, -3)
print("3d vec additional: ", adds)
print("3d vec substract: ", subs)

