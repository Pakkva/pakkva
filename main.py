import random, os
p = 0
print(os.walk("BD"))
for i in range(20):
    f = open(f"BD/{random.randint(850,950)}","w")
    f.write(f"{random.randint(1,1000)}")
    f.close

for i in os.walk("BD"):
    for j in i[2]:
        print(j)
        f = open(f"BD/{j}", "r")
        a = f.read
        print(a)
        p += int(a)
        f.close
for i in range(20):
    os.remove(j)
print(p)




