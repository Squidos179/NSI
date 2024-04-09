import string

#for i in range(13):
#    print(" ...", i % 5 + 1, end="")

for i in range(0, 200):
    print(string.ascii_lowercase[i%26], end='')