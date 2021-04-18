import random

names = set()
names.add("Michael")
names.add("Robin")
names.add("Michael")
# sets do not allow duplicates; set elements are always unique
# but you cannot ask for numbered elements of sets (ex. names[3])
print(names)
# to convert set to list and vice versa
names = ["Michael", "Robin", "Sarah"]
names = set(names)
print(names)
names = list(names)
print(names)

r_list = []
for i in range(0, 10):
    n = random.randint(1, 10)
    r_list.append(n)

print(r_list)
r_list = set(r_list)
print(r_list)
# switching r_list to a set removes the duplicates
