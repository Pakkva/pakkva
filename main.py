import random
for i in range(20):
    f = open(f"BD/{i}.txt", "w")
    f.write(f"{random.randint (0, 1000)}")
    f.close()


