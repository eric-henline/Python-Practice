import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []


def list_overlap(a, b):
    for num in b:
        if num in a and num not in c:
            c.append(num)
    return c


print(list_overlap(a, b))

print("This is a buffer line")
c = []
# must import random for this function
x = random.sample(range(20), 8)
y = random.sample(range(20), 5)
print("list x is:", x)
print("list y is:", y)
print("The overlap of list x and y is:", list_overlap(x, y))

# python practice 10
aa = [2, 4, 5]
bb = [3, 5, 7]
cc = [x*y for x in aa for y in bb]
print(cc)
dd = [x*y for x in aa for y in bb if x*y % 2 != 0]
print(dd)

# want to make a list of intersection of a and b using list comprehension
c1_overlap = [x for x in a if x in b]
c1_condensed = []
for num in c1_overlap:
    if num not in c1_condensed:
        c1_condensed.append(num)

print("The list 'c1_overlap' is:", c1_overlap)
print("The list 'c1_condensed' is:", c1_condensed)

xx = random.sample(range(1, 20), 9)
yy = random.sample(range(1, 30), 11)

print("list xx is:", xx)
print("list yy is:", yy)

zz_overlap = [n for n in xx if n in yy]
zz_condensed = []
for num in zz_overlap:
    if num in zz_overlap:
        zz_condensed.append(num)

print("The list 'zz_condensed' is:", zz_condensed)
