

a = int(input('insert a: '))
b = int(input('insert b: '))
c = int(input('insert c: '))

root1 = (-b + (b *b - 4*a*c) ** 0.5)/ (2* a)
root2 = (-b - (b *b - 4*a*c) ** 0.5)/ (2* a)

print(root1)
print(root2)